import json
import os

notebooks = [
    r"audio processing\Q2.Code.ipynb",
    r"image processing\Image.part1.ipynb",
    r"image processing\image.part2.ipynb"
]

workspace_root = "."

for nb_path in notebooks:
    full_path = os.path.join(workspace_root, nb_path)
    print(f"\n==================================================")
    print(f"Analyzing Notebook: {nb_path}")
    print(f"==================================================")
    if not os.path.exists(full_path):
        print("File not found!")
        continue
    
    with open(full_path, "r", encoding="utf-8") as f:
        try:
            nb = json.load(f)
        except Exception as e:
            print(f"Error loading JSON: {e}")
            continue
            
    print(f"Number of cells: {len(nb.get('cells', []))}")
    for idx, cell in enumerate(nb.get('cells', [])):
        cell_type = cell.get('cell_type', '')
        source = cell.get('source', [])
        source_str = "".join(source) if isinstance(source, list) else str(source)
        first_line = source_str.split("\n")[0] if source_str else ""
        print(f"Cell {idx+1}: {cell_type} | Length: {len(source_str)} chars")
        if first_line:
            print(f"  First line: {first_line[:100]}")
