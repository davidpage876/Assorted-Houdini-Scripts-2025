# For each selected object create equivalent "object merge" nodes
# linked together with a "merge" node contained in a geo at object level. 

H_SPACING = 3.2
V_SPACING = 4
paths = []

# Collect object paths to merge.
for node in hou.selectedNodes():
    path = f"{node.path()}/OUT"
    paths.append(path)

merged_container = hou.node("obj").createNode("geo")
merged_container.setName("MergedContainer")

# Create object merge nodes for each path.
nodes = []
num_created = 0
for path in paths:
    node = merged_container.createNode("object_merge")
    node.move((num_created * H_SPACING, 0))
    node.parm("objpath1").set(path)
    nodes.append(node)
    num_created += 1

# Create merge node and connect up object merge nodes as inputs.
merge_node = merged_container.createNode("merge")
merge_node.move((H_SPACING * (len(nodes) - 0.5) / 2.0, -V_SPACING))
for i, node in enumerate(nodes):
    merge_node.setInput(i, node)
merge_node.setSelected(True)
merge_node.setDisplayFlag(True)
merge_node.setRenderFlag(True)
