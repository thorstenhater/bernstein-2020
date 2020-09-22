#!/usr/bin/env python3

import sys
from collections import defaultdict
import json
from dataclasses import dataclass

# import arbor

@dataclass
class parameters:
    membrane_capacitance: float = None
    temperature_K:        float = None
    membrane_potential:   float = None
    axial_resistivity:    float = None

def load_allen_fit(fit):
    with open(fit) as fd:
        fit = json.load(fd)

    param = defaultdict(dict)
    mechs = defaultdict(dict)
    for block in fit['genome']:
        mech   = block['mechanism'] or 'pas'
        region = block['section']
        name   = block['name']
        if name.endswith('_' + mech):
            name = name[:-(len(mech) + 1)]
        else:
            if mech == "pas":
                param[region][name] = float(block['value'])
                continue
        if mech == 'pas':
            mech = 'default_pas'
        mechs[(region, mech)][name] = float(block['value'])

    param = [(r, parameters(vs)) for r, vs in param.items()]
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

swc      = 'cell.swc'
current  = 0.15
t_start  = 200
t_stop   = 1200

default_parameters, region_parameters, reversal_potentials, mechanisms = load_allen_fit('fit.json')

"""
# Label regions and interesting places
# labels = arbor.label_dict({'soma': '(tag 1)',
                           # 'axon': '(tag 2)',
                           # 'dend': '(tag 3)',
                           # 'apic': '(tag 4)',
                           # 'center': '(location 0 0.5)'})

# Build a cell from data
# segment_tree = arbor.load_swc_allen(swc, no_gaps=False)
# morphology   = arbor.morphology(segment_tree)
# cell         = arbor.cable_cell(morphology, labels)

# Attach Clamp and Detector
cell.place('center', arbor.iclamp(t_start, t_stop - t_start, current))
cell.place('center', arbor.spike_detector(-40))

# Set discretisation
cell.compartments_length(20)

#
cell.set_properties(tempK=T, Vm=Vm, rL=ra)
for region, values in cond.items():
    cell.paint(region, cm=values["cm"]/100, rL=values["Ra"])

# Set reversal potentials
for region, ion, e in erev:
    cell.paint(region, arbor.ion(ion, rev_pot=e))

cell.set_ion('ca', int_con=5e-5, ext_con=2.0, method=arbor.mechanism('default_nernst/x=ca'))

# Mechanisms
for mech, region, values in mechanisms:
    m = arbor.mechanism(mech, values)
    cell.paint(region, m)

# Run the simulation, collecting voltages
model = arbor.single_cell_model(cell)

default = arbor.default_catalogue()
catalogue = arbor.allen_catalogue()
catalogue.extend(default, 'default_')
model.properties.catalogue = catalogue

model.probe('voltage', 'center', frequency=200000)

model.run(tfinal=t_start + t_stop, dt=1000/200000)

spikes   = np.array(model.spikes)
times    = model.traces[0].time[:]
voltages = model.traces[0].value[:]
"""
