# Reorders inputs for the selected node based on their horizontal position. 

nodes = hou.selectedNodes()

for node in nodes:
    input_nodes = node.inputs()
    sorted_inputs = sorted(input_nodes, key=lambda x: x.position().x())
    for i, input in enumerate(sorted_inputs):
        node.setInput(i, input)
