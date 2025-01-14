from PIL import Image
import os

def analyze_image_metadata(image_path):
    # Open the image
    with Image.open(image_path) as img:
        # Get image metadata
        width, height = img.size
        file_size = os.path.getsize(image_path)
        color_mode = img.mode

        # Print the metadata
        print(f'Image: {os.path.basename(image_path)}')
        print(f' - Resolution: {width}x{height}')
        print(f' - File Size: {file_size} bytes')
        print(f' - Color Mode: {color_mode}')
        print()


# Define the path to your dataset directory
dataset_dir = '/Users/wchanee/Desktop/APU Degree CS spec Data Analytics/YEAR 3/FYP/FYP_Project/dataset'

# Iterate through each subdirectory in the dataset directory
subdirs = ['train', 'valid', 'test']
for subdir in subdirs:
    subdir_path = os.path.join(dataset_dir, subdir)
    for root, _, files in os.walk(subdir_path):
        for filename in files:
            if filename.endswith('.jpg'):
                image_path = os.path.join(root, filename)
                analyze_image_metadata(image_path)
