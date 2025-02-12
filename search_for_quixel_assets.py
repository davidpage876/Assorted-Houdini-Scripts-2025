import os
from pathlib import Path


# Search the given directory for Quixel assets and returns paths to the
# available geometry and material maps as a dictionary.
# 
# If recursive is true search subdirectories for additional assets. 
#
def search_for_asset(dir, recursive=True):
    assets_found = []
    files = [path for path in os.listdir(dir) if os.path.isfile(os.path.join(dir, path))]
    dirs = [path for path in os.listdir(dir) if os.path.isdir(os.path.join(dir, path))]
    
    # Search for asset files.
    found = False
    name = ""
    mesh = ""
    base_color = ""
    roughness = ""
    metal = ""
    normal = ""
    displacement = ""
    ao = ""
    for file in files:
        
        # Search for geometry.
        if any(s in file for s in ["_High.fbx", "_LOD0.fbx", "_Mid.fbx", "_Low.fbx"]):
            name = Path(file).stem
            mesh = os.path.join(dir, file)
            found = True
        
        # Search for textures.
        if any(s in file for s in ["_BaseColor.jpg", "_BaseColor", "_Albedo.jpg", "_Albedo"]):
            base_color = os.path.join(dir, file)
        if any(s in file for s in ["_Roughness.jpg", "_Roughness"]):
            roughness = os.path.join(dir, file)
        if any(s in file for s in ["_Metal.jpg", "_Metal"]):
            metal = os.path.join(dir, file)
        if any(s in file for s in ["_Normal_LOD0.jpg", "_Normal_LOD0", "_Normal.jpg", "_Normal"]):
            normal = os.path.join(dir, file)
        if any(s in file for s in ["_Displacement.jpg", "_Displacement"]):
            displacement = os.path.join(dir, file)
        if any(s in file for s in ["_AO.jpg", "_AO"]):
            ao = os.path.join(dir, file)
        
    # Create asset if found.
    if found:
        asset = {
            "name": name,
            "mesh": mesh,
            "base_color": base_color,
            "roughness": roughness,
            "metal": metal,
            "normal": normal,
            "displacement": displacement,
            "ao": ao,
        }
        assets_found.append(asset)
    
    # Recursively search subfolders if no asset was found.
    elif recursive:
        for subdir in dirs:
            assets_found_in_subdir = search_for_asset(os.path.join(dir, subdir), recursive)
            for asset in assets_found_in_subdir:
                assets_found.append(asset)
            
    return assets_found

