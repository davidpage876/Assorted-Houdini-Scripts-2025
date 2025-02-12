# Stagger selected object transforms in obj space along the x axis from biggest to smallest.

SPACING = 1

# Sort by width.
sorted_nodes = sorted(hou.selectedNodes(), 
        key=lambda node: node.node("OUT").geometry().boundingBox().sizevec().x(),
        reverse=True)

# Position objects.
current_x = 0.0
for node in sorted_nodes:
    bounds = node.node("OUT").geometry().boundingBox()
    width = bounds.sizevec().x()
    
    node.parm("tx").set(current_x + width / 2.0)    
    current_x += width + SPACING
