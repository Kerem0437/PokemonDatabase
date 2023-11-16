import os
import shutil
import numpy as np
from PIL import Image, ImageEnhance
import imgaug.augmenters as iaa
import time

# Define the source and destination directories
source_dir = "C:\\Users\\kerem\\OneDrive\\Desktop\\Clean\\2-ConvertToPngRenameAndResize"
dest_dir = "C:\\Users\\kerem\\OneDrive\\Desktop\\Clean\\3-NormalizeAugmentSharpen"

# Augmentation and enhancement setup
augmenter = iaa.Sequential([
    iaa.Fliplr(0.5),  # Horizontal flips
    iaa.Affine(rotate=(-30, 30))  # Rotation
])

# Function to process the images within a subfolder
def process_images(folder_path, dest_folder_path, folder_name, current_number, total_number):
    #print(f"Starting to process images in {folder_path}")

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        #print(f"Processing file: {file}")

        with Image.open(file_path) as img:
            # Normalize
            img_array = np.array(img) / 255.0

            # Augment
            img_array_aug = augmenter.augment_image(img_array)

            # Enhance
            img_enhanced = Image.fromarray((img_array_aug * 255).astype(np.uint8))
            enhancer = ImageEnhance.Sharpness(img_enhanced)
            img_sharpened = enhancer.enhance(2.0)

            # Save to destination
            new_path = os.path.join(dest_folder_path, file)
            img_sharpened.save(new_path, 'PNG')
            #print(f"Saved processed image to: {new_path}")

    elapsed_time = time.time() - start_time
    print(f"Processed '{folder_name}' ({current_number}/{total_number}). Time elapsed: {elapsed_time:.2f} seconds")

start_time = time.time()

# Copy all contents from source to destination
print("Copying files from source to destination...")
if not os.path.exists(dest_dir):
    shutil.copytree(source_dir, dest_dir, dirs_exist_ok=True)
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
    folder_path = os.path.join(source_dir, folder)
    dest_folder_path = os.path.join(dest_dir, folder)
    if os.path.isdir(folder_path):
        current_folder += 1
        process_images(folder_path, dest_folder_path, folder, current_folder, total_folders)

print("Image processing for all folders completed.")
