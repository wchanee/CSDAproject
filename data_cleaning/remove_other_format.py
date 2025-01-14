import os

# Define the path to your dataset folder
dataset_dir = '/dataset'

# List of subfolders in the dataset directory
subfolders = ['test', 'train', 'valid']

# Function to clean non-JPG files from a given directory
def clean_non_jpg_files(directory):
    # Get a list of all files in the directory
    all_files = os.listdir(directory)

    # Filter out only the JPG files
    jpg_files = [f for f in all_files if f.lower().endswith('.jpg')]

    # Remove non-JPG files
    for file in all_files:
        if file not in jpg_files:
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Removed {file_path}")

# Iterate through each subfolder and clean non-JPG files
for subfolder in subfolders:
    subfolder_path = os.path.join(dataset_dir, subfolder)
    if os.path.isdir(subfolder_path):
        print(f"Cleaning non-JPG files in folder: {subfolder}")
        clean_non_jpg_files(subfolder_path)

print("Data cleaning completed. Only JPG files are retained.")