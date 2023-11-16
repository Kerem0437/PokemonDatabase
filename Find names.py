import os
import shutil
from PIL import Image

# Define the source and destination directories
source_dir = "C:\\Users\\kerem\\OneDrive\\Desktop\\Image Dataset\\1-Original"
dest_dir = "C:\\Users\\kerem\\OneDrive\\Desktop\\Image Dataset\\2-ConvertToPngRenameAndResize"

# Step 1: Copy folders from source to destination
if not os.path.exists(dest_dir):
    shutil.copytree(source_dir, dest_dir)

# Function to process the images
def process_images(folder_path):
    # Iterate through each file in the folder
    for i, file in enumerate(os.listdir(folder_path)):
        # Check if the file is a JPEG image
        if file.lower().endswith('.jpeg'):
            file_path = os.path.join(folder_path, file)
            # Open the image
            with Image.open(file_path) as img:
                # Convert to PNG and resize
                img = img.convert('RGB').resize((256, 256), Image.ANTIALIAS)
                # Define the new file name
                new_name = f"{os.path.basename(folder_path)}_{i}.png"
                new_path = os.path.join(folder_path, new_name)
                # Save the new image
                img.save(new_path, 'PNG')
                # Delete the original file
                os.remove(file_path)

# Step 2 and 3: Process each folder inside the destination directory
for folder in os.listdir(dest_dir):
    folder_path = os.path.join(dest_dir, folder)
    if os.path.isdir(folder_path):
        process_images(folder_path)

print("Images processing completed.")
