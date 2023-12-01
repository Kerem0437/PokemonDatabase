import os
import shutil
from PIL import Image

# Define the source and destination directories
source_dir = "C:\\Users\\kerem\\PokemonDatabase\\Code\\Misc\\Val"
dest_dir = "C:\\Users\\kerem\\PokemonDatabase\\Code\\Misc\\Validation"

# Function to process (copy) the images from subfolders of source_dir to dest_dir
def process_images(folder_path, folder_name, current_number, total_number):
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        new_path = os.path.join(dest_dir, file)

        # Copy the image to dest_dir without renaming
        shutil.copy2(file_path, new_path)
        print(f"Copied {file} to {new_path}")

    print(f"Processed '{folder_name}' ({current_number}/{total_number})")

# Ensure dest_dir exists
if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

# Process images in each subfolder of the source directory
print("Starting image processing...")
total_folders = sum(os.path.isdir(os.path.join(source_dir, d)) for d in os.listdir(source_dir))
current_folder = 0

for folder in os.listdir(source_dir):
    folder_path = os.path.join(source_dir, folder)
    if os.path.isdir(folder_path):
        current_folder += 1
        process_images(folder_path, folder, current_folder, total_folders)

print("Image processing for all folders completed.")
