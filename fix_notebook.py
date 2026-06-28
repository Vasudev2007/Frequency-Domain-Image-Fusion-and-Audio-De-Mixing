import os
import json

nb_path = "image_fusion/notebook/image.part2.ipynb"

if os.path.exists(nb_path):
    with open(nb_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Fix the escaped quotes inside the JSON string
    content = content.replace('\\"chihuahua_cropped_resized.jpg\\"', '\\"../data/cat_gray.jpg\\"')
    content = content.replace('\\"Trisha_resized.jpg\\"', '\\"../data/dog_gray.jpg\\"')
    
    with open(nb_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully restored cat and dog images in image.part2.ipynb!")
else:
    print("Could not find the notebook at", nb_path)
