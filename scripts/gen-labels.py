import arbor
from arbor import mpoint

def is_collocated(l, r):
    return l[0]==r[0] and l[1]==r[1]

def write_morphology(name, morph):
    string = 'tmp = ['.format(name)
    for i in range(morph.num_branches):
        first = True
        sections = '['
        for seg in morph.branch_segments(i):
            if not first:
                if is_collocated((seg.prox.x, seg.prox.y), (last_dist.x, last_dist.y)):
                    sections += ', '
                else:
                    sections += '], ['

            first = False
            p = seg.prox
            d = seg.dist
            sections += 'Segment(({}, {}, {}), ({}, {}, {}), {})'.format(p.x, p.y, p.radius, d.x, d.y, d.radius, seg.tag)
            last_dist = seg.dist
        sections += ']'

        string += '\n    [{}],'.format(sections)
    string += ']\n'
    string += '{} = representation.make_morph(tmp)\n\n'.format(name)
    return string

# Describe the morphologies

mnpos = arbor.mnpos

# The morphology used for all of the region/locset illustrations
label_tree = arbor.segment_tree()
label_tree.append(mnpos, mpoint(0,   0.0, 0, 2.0), mpoint( 4,  0.0, 0, 2.0), tag=1)
label_tree.append(0,     mpoint(4,   0.0, 0, 0.8), mpoint( 8,  0.0, 0, 0.8), tag=3)
label_tree.append(1,     mpoint(8,   0.0, 0, 0.8), mpoint(12, -0.5, 0, 0.8), tag=3)
label_tree.append(2,     mpoint(12, -0.5, 0, 0.8), mpoint(20,  4.0, 0, 0.4), tag=3)
label_tree.append(3,     mpoint(20,  4.0, 0, 0.4), mpoint(26,  6.0, 0, 0.2), tag=3)
label_tree.append(2,     mpoint(12, -0.5, 0, 0.5), mpoint(19, -3.0, 0, 0.5), tag=3)
label_tree.append(5,     mpoint(19, -3.0, 0, 0.5), mpoint(24, -7.0, 0, 0.2), tag=3)
label_tree.append(5,     mpoint(19, -3.0, 0, 0.5), mpoint(23, -1.0, 0, 0.2), tag=3)
label_tree.append(7,     mpoint(23, -1.0, 0, 0.2), mpoint(26, -2.0, 0, 0.2), tag=3)
label_tree.append(mnpos, mpoint(0,   0.0, 0, 2.0), mpoint(-7,  0.0, 0, 0.4), tag=2)
label_tree.append(9,     mpoint(-7,  0.0, 0, 0.4), mpoint(-10, 0.0, 0, 0.4), tag=2)

label_morph = arbor.morphology(label_tree)

# The label morphology with some gaps (at start of dendritic tree and remove the axon hillock)
label_tree = arbor.segment_tree()
label_tree.append(mnpos, mpoint(0,   0.0, 0, 2.0), mpoint( 4,  0.0, 0, 2.0), tag=1)
label_tree.append(0,    mpoint(5,   0.0, 0, 0.8), mpoint( 8,  0.0, 0, 0.8), tag=3)
label_tree.append(1,    mpoint(8,   0.0, 0, 0.8), mpoint(12, -0.5, 0, 0.8), tag=3)
label_tree.append(2,    mpoint(12, -0.5, 0, 0.8), mpoint(20,  4.0, 0, 0.4), tag=3)
label_tree.append(3,    mpoint(20,  4.0, 0, 0.4), mpoint(26,  6.0, 0, 0.2), tag=3)
label_tree.append(2,    mpoint(12, -0.5, 0, 0.5), mpoint(19, -3.0, 0, 0.5), tag=3)
label_tree.append(5,    mpoint(19, -3.0, 0, 0.5), mpoint(24, -7.0, 0, 0.2), tag=3)
label_tree.append(5,    mpoint(19, -3.0, 0, 0.5), mpoint(23, -1.0, 0, 0.2), tag=3)
label_tree.append(7,    mpoint(23, -1.0, 0, 0.2), mpoint(26, -2.0, 0, 0.2), tag=3)
label_tree.append(mnpos, mpoint(-2,  0.0, 0, 0.4), mpoint(-10, 0.0, 0, 0.4), tag=2)

detached_morph = arbor.morphology(label_tree)

# soma with "stacked cylinders"
stacked_tree = arbor.segment_tree()
stacked_tree.append(mnpos, mpoint(0,   0.0, 0, 0.5), mpoint( 1,  0.0, 0, 1.5), tag=1)
stacked_tree.append(0,    mpoint(1,   0.0, 0, 1.5), mpoint( 2,  0.0, 0, 2.5), tag=1)
stacked_tree.append(1,    mpoint(2,   0.0, 0, 2.5), mpoint( 3,  0.0, 0, 2.5), tag=1)
stacked_tree.append(2,    mpoint(3,   0.0, 0, 2.5), mpoint( 4,  0.0, 0, 1.2), tag=1)
stacked_tree.append(3,    mpoint(4,   0.0, 0, 0.8), mpoint( 8,  0.0, 0, 0.8), tag=3)
stacked_tree.append(4,    mpoint(8,   0.0, 0, 0.8), mpoint(12, -0.5, 0, 0.8), tag=3)
stacked_tree.append(5,    mpoint(12, -0.5, 0, 0.8), mpoint(20,  4.0, 0, 0.4), tag=3)
stacked_tree.append(6,    mpoint(20,  4.0, 0, 0.4), mpoint(26,  6.0, 0, 0.2), tag=3)
stacked_tree.append(5,    mpoint(12, -0.5, 0, 0.5), mpoint(19, -3.0, 0, 0.5), tag=3)
stacked_tree.append(8,    mpoint(19, -3.0, 0, 0.5), mpoint(24, -7.0, 0, 0.2), tag=3)
stacked_tree.append(8,    mpoint(19, -3.0, 0, 0.5), mpoint(23, -1.0, 0, 0.2), tag=3)
stacked_tree.append(10,   mpoint(23, -1.0, 0, 0.2), mpoint(26, -2.0, 0, 0.2), tag=3)
stacked_tree.append(mnpos, mpoint(0,   0.0, 0, 0.4), mpoint(-7,  0.0, 0, 0.4), tag=2)
stacked_tree.append(12,   mpoint(-7,  0.0, 0, 0.4), mpoint(-10, 0.0, 0, 0.4), tag=2)

stacked_morph = arbor.morphology(stacked_tree)

# spherical cell with radius 2 μm
tree = arbor.segment_tree()
tree.append(mnpos, mpoint(-2, 0, 0, 2), mpoint(2, 0, 0, 2), tag=1)
sphere_morph = arbor.morphology(tree)

# single branch: one tapered segment
tree = arbor.segment_tree()
tree.append(mnpos, mpoint(0, 0, 0, 1), mpoint(10, 0, 0, 0.5), tag=3)
branch_morph1 = arbor.morphology(tree)

# single branch: multiple segments, continuous radius
tree = arbor.segment_tree()
tree.append(mnpos, mpoint( 0.0,  0.0,  0.0, 1.0), mpoint( 3.0,  0.2,  0.0, 0.8), tag=1)
tree.append(0,     mpoint( 3.0,  0.2,  0.0, 0.8), mpoint( 5.0, -0.1,  0.0, 0.7), tag=2)
tree.append(1,     mpoint( 5.0, -0.1,  0.0, 0.7), mpoint( 8.0,  0.0,  0.0, 0.6), tag=2)
tree.append(2,     mpoint( 8.0,  0.0,  0.0, 0.6), mpoint(10.0,  0.0,  0.0, 0.5), tag=3)
branch_morph2 = arbor.morphology(tree)

# single branch: multiple segments, gaps
tree = arbor.segment_tree()
tree.append(mnpos, mpoint( 0.0,  0.0,  0.0, 1.0), mpoint(3.0,  0.2,  0.0, 0.8), tag=1)
tree.append(0,     mpoint( 3.0,  0.2,  0.0, 0.8), mpoint(5.0, -0.1,  0.0, 0.7), tag=2)
tree.append(1,     mpoint( 6.0, -0.1,  0.0, 0.7), mpoint(9.0, 0.0,  0.0, 0.6), tag=2)
tree.append(2,     mpoint( 9.0,  0.0,  0.0, 0.6), mpoint(11.0, 0.0,  0.0, 0.5), tag=3)
branch_morph3 = arbor.morphology(tree)

# single branch: multiple segments, discontinuous radius
tree = arbor.segment_tree()
tree.append(mnpos, mpoint( 0.0,  0.0,  0.0, 1.0), mpoint( 3.0,  0.2,  0.0, 0.8), tag=1)
tree.append(0,     mpoint( 3.0,  0.2,  0.0, 0.8), mpoint( 5.0, -0.1,  0.0, 0.7), tag=2)
tree.append(1,     mpoint( 5.0, -0.1,  0.0, 0.7), mpoint( 8.0,  0.0,  0.0, 0.5), tag=2)
tree.append(2,     mpoint( 8.0,  0.0,  0.0, 0.3), mpoint(10.0,  0.0,  0.0, 0.5), tag=3)
branch_morph4 = arbor.morphology(tree)

tree = arbor.segment_tree()
tree.append(mnpos, mpoint( 0.0, 0.0, 0.0, 1.0), mpoint(10.0, 0.0, 0.0, 0.5), tag= 3)
tree.append(0,     mpoint(15.0, 3.0, 0.0, 0.2), tag= 3)
tree.append(0,     mpoint(15.0,-3.0, 0.0, 0.2), tag= 3)
yshaped_morph = arbor.morphology(tree)

tree = arbor.segment_tree()
tree.append(mnpos, mpoint(-3.0, 0.0, 0.0, 3.0), mpoint( 3.0, 0.0, 0.0, 3.0), tag=1)
tree.append(0, mpoint( 4.0, -1.0,  0.0, 0.6), mpoint(10.0,  -2.0,  0.0, 0.5), tag=3)
tree.append(1, mpoint(15.0, -1.0,  0.0, 0.5), tag=3)
tree.append(2, mpoint(18.0, -5.0,  0.0, 0.3), tag=3)
tree.append(2, mpoint(20.0,  2.0,  0.0, 0.3), tag=3)
ysoma_morph1 = arbor.morphology(tree)

tree = arbor.segment_tree()
tree.append(mnpos, mpoint(-3.0, 0.0, 0.0, 3.0),   mpoint( 3.0, 0.0, 0.0, 3.0), tag=1)
tree.append(0,     mpoint( 4.0, -1.0,  0.0, 0.6), mpoint(10.0,-2.0,  0.0, 0.5), tag=3)
tree.append(1,     mpoint(15.0, -1.0,  0.0, 0.5), tag= 3)
tree.append(2,     mpoint(18.0, -5.0,  0.0, 0.3), tag= 3)
tree.append(2,     mpoint(20.0,  2.0,  0.0, 0.3), tag= 3)
tree.append(0,     mpoint( 2.0,  1.0,  0.0, 0.6), mpoint(12.0, 4.0,  0.0, 0.5), tag=3)
tree.append(5,     mpoint(18.0,  4.0,  0.0, 0.3), tag= 3)
tree.append(5,     mpoint(16.0,  9.0,  0.0, 0.1), tag= 3)
tree.append(mnpos, mpoint(-3.5,  0.0,  0.0, 1.5), mpoint(-6.0,-0.2,  0.0, 0.5), tag=2)
tree.append(8,     mpoint(-15.0,-0.1,  0.0, 0.5), tag=2)
ysoma_morph2 = arbor.morphology(tree)

tree = arbor.segment_tree()
tree.append(mnpos, mpoint(-3.0, 0.0, 0.0, 3.0),   mpoint( 3.0, 0.0, 0.0, 3.0), tag=1)
tree.append(0,     mpoint( 3.0,  0.0,  0.0, 0.6), mpoint(9.0,-1.0,  0.0, 0.5), tag=3)
tree.append(1,     mpoint(14.0,  0.0,  0.0, 0.5), tag= 3)
tree.append(2,     mpoint(17.0, -4.0,  0.0, 0.3), tag= 3)
tree.append(2,     mpoint(19.0,  3.0,  0.0, 0.3), tag= 3)
tree.append(0,     mpoint( 3.0,  0.0,  0.0, 0.6), mpoint(13.0, 3.0,  0.0, 0.5), tag=3)
tree.append(5,     mpoint(19.0,  3.0,  0.0, 0.3), tag= 3)
tree.append(5,     mpoint(17.0,  8.0,  0.0, 0.1), tag= 3)
tree.append(mnpos, mpoint(-3.0,  0.0,  0.0, 1.5), mpoint(-5.5,-0.2,  0.0, 0.5), tag=2)
tree.append(8,     mpoint(-14.5,-0.1,  0.0, 0.5), tag=2)
ysoma_morph3 = arbor.morphology(tree)

regions  = {
            'empty': '(nil)',
            'all': '(all)',
            'tag1': '(tag 1)',
            'tag2': '(tag 2)',
            'tag3': '(tag 3)',
            'tag4': '(tag 4)',
            'soma': '(region "tag1")',
            'axon': '(region "tag2")',
            'dend': '(join (region "tag3") (region "tag4"))',
            'radlt5': '(radius_lt (all) 0.5)',
            'radle5': '(radius_le (all) 0.5)',
            'radgt5': '(radius_gt (all) 0.5)',
            'radge5': '(radius_ge (all) 0.5)',
            'rad36':  '(intersect (radius_gt (all) 0.3) (radius_lt (all) 0.6))',
            'branch0': '(branch 0)',
            'branch3': '(branch 3)',
            'cable_1_01': '(cable 1 0 1)',
            'cable_1_31': '(cable 1 0.3 1)',
            'cable_1_37': '(cable 1 0.3 0.7)',
            'proxint':     '(proximal_interval (locset "proxint_in") 5)',
            'proxintinf':  '(proximal_interval (locset "proxint_in"))',
            'distint':     '(distal_interval   (locset "distint_in") 5)',
            'distintinf':  '(distal_interval   (locset "distint_in"))',
            'lhs' : '(join (cable 0 0.5 1) (cable 1 0 0.5))',
            'rhs' : '(branch 1)',
            'and': '(intersect (region "lhs") (region "rhs"))',
            'or':  '(join      (region "lhs") (region "rhs"))',
          }
locsets = {
            'root': '(root)',
            'term': '(terminal)',
            'rand_dend': '(uniform (region "dend") 0 50 0)',
            'loc15': '(location 1 0.5)',
            'uniform0': '(uniform (tag 3) 0 9 0)',
            'uniform1': '(uniform (tag 3) 0 9 1)',
            'branchmid': '(on_branches 0.5)',
            'distal':  '(distal   (region "rad36"))',
            'proximal':'(proximal (region "rad36"))',
            'distint_in': '(sum (location 1 0.5) (location 2 0.7) (location 5 0.1))',
            'proxint_in': '(sum (location 1 0.8) (location 2 0.3))',
            'loctest' : '(distal (complete (join (branch 1) (branch 0))))',
            'restrict': '(restrict  (terminal) (tag 3))',
          }

labels = {**regions, **locsets}
d = arbor.label_dict(labels)

# Create a cell to concretise the region and locset definitions
cell = arbor.cable_cell(label_morph, d)

################################################################################
# Output all of the morphologies and reion/locset definitions to a Python script
# that can be run during the documentation build to generate images.
################################################################################
f = open('inputs.py', 'w')
f.write('import representation\n')
f.write('from representation import Segment\n')

f.write('\n############# morphologies\n\n')
f.write(write_morphology('label_morph',    label_morph))
f.write(write_morphology('detached_morph', detached_morph))
f.write(write_morphology('stacked_morph',  stacked_morph))
f.write(write_morphology('sphere_morph',   sphere_morph))
f.write(write_morphology('branch_morph1',  branch_morph1))
f.write(write_morphology('branch_morph2',  branch_morph2))
f.write(write_morphology('branch_morph3',  branch_morph3))
f.write(write_morphology('branch_morph4',  branch_morph4))
f.write(write_morphology('yshaped_morph',  yshaped_morph))
f.write(write_morphology('ysoma_morph1',   ysoma_morph1))
f.write(write_morphology('ysoma_morph2',   ysoma_morph2))
f.write(write_morphology('ysoma_morph3',   ysoma_morph3))

f.write('\n############# locsets\n\n')
for label in locsets:
    locs = [(l.branch, l.pos) for l in cell.locations(label)]
    f.write('ls_{}  = {{\'type\': \'locset\', \'value\': {}}}\n'.format(label, locs))

f.write('\n############# regions\n\n')
for label in regions:
    comps = [(c.branch, c.prox, c.dist) for c in cell.cables(label)]
    f.write('reg_{} = {{\'type\': \'region\', \'value\': {}}}\n'.format(label, comps))

f.close()

