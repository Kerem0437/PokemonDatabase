import os
import shutil
from PIL import Image
import time
import cairosvg


# Define the source and destination directories
source_dir = "C:\\Users\\kerem\\PokemonDatabase\\Code\\Clean Images and make cvs\\Testvalidation"
dest_dir = "C:\\Users\\kerem\\PokemonDatabase\\Code\\Clean Images and make cvs\\TestVal2"
# Function to process the images within a subfolder
def process_images(folder_path, folder_name, current_number, total_number):
    #print(f"Starting to process images in {folder_path}")
    
    for file in os.listdir(folder_path):
        if file.lower().endswith('.svg'):
            file_path = os.path.join(folder_path, file)
            new_name = f"{os.path.splitext(file)[0]}.png"
            new_path = os.path.join(folder_path, new_name)
            cairosvg.svg2png(url=file_path, write_to=new_path)
            #print(f"Converted SVG to PNG: {new_path}")
            os.remove(file_path)  # Remove the original .svg file

    # First pass: Convert .jpeg to .png
    for file in os.listdir(folder_path):
        if file.lower().endswith('.jpeg'):
            file_path = os.path.join(folder_path, file)
            with Image.open(file_path) as img:
                new_name = f"{os.path.splitext(file)[0]}.png"
                new_path = os.path.join(folder_path, new_name)
                img.save(new_path, 'PNG')
                #print(f"Converted and saved: {new_path}")
            os.remove(file_path)  # Remove the original .jpeg file

    # Second pass: Resize and rename all images
    for i, file in enumerate(os.listdir(folder_path)):
        file_path = os.path.join(folder_path, file)
        with Image.open(file_path) as img:
            img = img.resize((256, 256), Image.Resampling.LANCZOS)
            new_name = f"{os.path.basename(folder_path)}_{i}.png"
            new_path = os.path.join(folder_path, new_name)
            img.save(new_path, 'PNG')
            if file_path != new_path:  # Avoid deleting the new file
                os.remove(file_path)
            #print(f"Resized and renamed: {new_path}")
    
    print(f"Processed '{folder_name}' ({current_number}/{total_number})")
    elapsed_time = time.time() - start_time
    print(f"Time elapsed for processing '{folder_name}': {elapsed_time:.2f} seconds")


start_time = time.time()
# Copy all contents from source to destination
print("Copying files...")
if not os.path.exists(dest_dir):
    shutil.copytree(source_dir, dest_dir)
else:
    for item in os.listdir(source_dir):
        s_item = os.path.join(source_dir, item)
        d_item = os.path.join(dest_dir, item)
        if os.path.isdir(s_item):
            shutil.copytree(s_item, d_item, dirs_exist_ok=True)
        else:
            shutil.copy2(s_item, d_item)
print("Copying completed.")

# Process images in each subfolder of the destination directory
print("Starting image processing...")
total_folders = sum(os.path.isdir(os.path.join(dest_dir, d)) for d in os.listdir(dest_dir))
current_folder = 0

for folder in os.listdir(dest_dir):
    folder_path = os.path.join(dest_dir, folder)
    if os.path.isdir(folder_path):
        current_folder += 1
        process_images(folder_path, folder, current_folder, total_folders)

print("Image processing for all folders completed.")
