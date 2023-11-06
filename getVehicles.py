import os
import xml.etree.ElementTree as ET

root_dir = input("resources directory:")
output_file = "vehicles.txt"

with open(output_file, "w") as f:
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".meta") and file.startswith("vehicle"):
                file_path = os.path.join(subdir, file)
                tree = ET.parse(file_path)
                root = tree.getroot()
                for model_name in root.iter('modelName'):
                    f.write(f'"{model_name.text}",\n')
    