import utils
import arbor

# read in geometry
segment_tree = arbor.load_swc_allen('cell.swc', no_gaps=False) # (2)
morphology = arbor.morphology(segment_tree)
# assign names to regions defined by SWC (3) and center of soma (4)
labels = arbor.label_dict({'soma': '(tag 1)', 'axon': '(tag 2)',
                           'dend': '(tag 3)', 'apic': '(tag 4)',
                           'center': '(location 0 0.5)'})
cell = arbor.cable_cell(morphology, labels)
# Discretisation: impose a maximum length per compartment of 20 um
cell.compartments_length(20)
# Attach stimulus and spike detector (4 a b)
cell.place('center', arbor.iclamp(200, 1000, 0.15))
cell.place('center', arbor.spike_detector(-40))

# Assign electro-physical parameters, loaded from Allen Brain Atlas (1)
defaults, region_parameters, ions, mechanisms = utils.load_allen_fit('fit.json')
# Set defaults
cell.set_properties(tempK=defaults.tempK, Vm=defaults.Vm,
                    cm=defaults.cm, rL=defaults.rL)
# Override defaults by region (3 a)
for region, vs in region_parameters:
    cell.paint(region, tempK=vs.tempK, Vm=vs.Vm, cm=vs.cm, rL=vs.rL)
# Set reversal potentials (3 b)
for region, ion, e in ions:
    cell.paint(region, arbor.ion(ion, rev_pot=e))
cell.set_ion('ca',
             int_con=5e-5, ext_con=2.0,
             method=arbor.mechanism('default_nernst/x=ca'))
# Assign ion dynamics (3 b)
for region, mech, values in mechanisms:
    cell.paint(region, arbor.mechanism(mech, values))

# Set up runnable simulation with mechanism catalogues default + allen
model = arbor.single_cell_model(cell)
catalogue = arbor.allen_catalogue()
catalogue.extend(arbor.default_catalogue(), 'default_')
model.properties.catalogue = catalogue
# Attach voltage probe (4 c)
model.probe('voltage', 'center', frequency=200000)

# Run simulation and plot voltages + spikes
model.run(tfinal=1400, dt=0.005)
utils.plot_results(model)
