# Toolshelf script to allow switching between light and dark viewport background with
# a hotkey.

def main():
    desktop = hou.ui.curDesktop()
    pane = desktop.paneTabOfType(hou.paneTabType.SceneViewer)
    
    if not pane:
        return
    
    settings = pane.curViewport().settings()
    scheme = settings.colorScheme()
    if scheme == hou.viewportColorScheme.Light:
        settings.setColorScheme(hou.viewportColorScheme.Dark)
    else:
        settings.setColorScheme(hou.viewportColorScheme.Light)

    
main()