## =================================================
#
# Fits any network box selected around their contents, with additional padding.
# Selecting a node inside a network box also fits that box.
#
# Hotkey: Ctrl-Shift-O 
#
# Settings:
# --------------------------------------------------

HORIZONTAL_PADDING = 0.8

VERTICAL_PADDING = 0.8

## =================================================



PADDING = hou.Vector2(HORIZONTAL_PADDING, VERTICAL_PADDING)


def padBox(box):
    box.fitAroundContents()
    
    position = box.position()
    size = box.size()
    bounds = hou.BoundingRect(
            position - PADDING, 
            position + size + PADDING)
    box.setBounds(bounds)
    
    



def main():
    
    # Find any boxes selected or boxes containing the selected nodes.
    boxes = set()
    for item in hou.selectedItems():
        if item.networkItemType() == hou.networkItemType.NetworkBox:
            boxes.add(item)
        else:
            parent_box = item.parentNetworkBox()
            if parent_box:
                boxes.add(parent_box)
    
    # Pad boxes.
    for box in boxes:
        padBox(box)

            
main()



#def createBox():
#    desktop = hou.ui.curDesktop()
#    pane = desktop.paneTabUnderCursor()
#    context = pane.pwd()
#    box = context.createNetworkBox()
#    return box