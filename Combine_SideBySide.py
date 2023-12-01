from PIL import Image
import os

# Directory where the images are located
IMAGE_DIR = "C:\\Users\\kerem\\Pokemon\\Clean Images"

# Image filenames
image_filenames = ["Image1.png", "Image2.png", "Image3.png"]
# Convert filenames to full paths
image_paths = [os.path.join(IMAGE_DIR, filename) for filename in image_filenames]

# Open the images
images = [Image.open(image_path) for image_path in image_paths]

# Check if images are of the desired size
for img in images:
    if img.size != (256, 256):
        raise ValueError("One or more images are not of size 256x256 pixels.")

# Create an empty image with the required size (256x1024) wtih 4 images side by side 
# 
final_image = Image.new('RGB', (768, 256))


# Place each image into the final_image
for index, image in enumerate(images):
    final_image.paste(image, (index*256, 0))

# Save the final_image in the IMAGE_DIR
final_image_path = os.path.join(IMAGE_DIR, "final.png")
final_image.save(final_image_path)

print(f"Image saved at {final_image_path}")
