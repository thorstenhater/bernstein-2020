#!/usr/bin/env python3

from dataclasses import dataclass

@dataclass
class parameters:
    cm: float = None
    tempK:        float = None
    Vm:   float = None
    rL:    float = None

def load_allen_fit(fit):
    from collections import defaultdict
    import json

    with open(fit) as fd:
        fit = json.load(fd)

    param = defaultdict(parameters)
    mechs = defaultdict(dict)
    for block in fit['genome']:
        mech   = block['mechanism'] or 'pas'
        region = block['section']
        name   = block['name']
        value  = float(block['value'])
        if name.endswith('_' + mech):
            name = name[:-(len(mech) + 1)]
        else:
            if mech == "pas":
                # transform names and values
                if name == 'cm':
                    param[region].cm = value/100.0
                elif name == 'Ra':
                    param[region].rL = value
                elif name == 'Vm':
                    param[region].Vm = value
                elif name == 'celsius':
                    param[region].tempK = value + 273.15
                else:
                    raise Exception(f"Unknown key: {name}")
                continue
            else:
                raise Exception(f"Illegal combination {mech} {name}")
        if mech == 'pas':
            mech = 'default_pas'
        mechs[(region, mech)][name] = value

    param = [(r, vs) for r, vs in param.items()]
    mechs = [(r, m, vs) for (r, m), vs in mechs.items()]

    default = parameters(None, # not set in example file
                         float(fit['conditions'][0]['celsius']) + 273.15,
                         float(fit['conditions'][0]['v_init']),
                         float(fit['passive'][0]['ra']))

    erev = []
    for kv in fit['conditions'][0]['erev']:
        region = kv['section']
        for k, v in kv.items():
            if k == 'section':
                continue
            ion = k[1:]
            erev.append((region, ion, float(v)))

    return default, param, erev, mechs

def plot_results(model):
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    import seaborn as sns
    import numpy as np

    spikes   = model.spikes
    times    = model.traces[0].time[:]
    voltages = model.traces[0].value[:]

    fg, ax = plt.subplots()
    ax.scatter(spikes, np.zeros_like(spikes) - 40, color=sns.color_palette()[1], zorder=20, label='Spike')
    ax.plot(times, voltages, label='Potential')
    ax.bar(200, 140, 1000, -120, align='edge', label='Stimulus', color='0.8')
    ax.set_xlabel('t/ms')
    ax.set_ylabel('U/mV')
    ax.set_xlim(left=0, right=1400)
    ax.set_ylim(top=20, bottom=-100)
    ax.legend(loc='best')
    plt.savefig("arbor.pdf", bbox_inches='tight')
