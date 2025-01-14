import os
import cv2

# Define the path to your dataset folder
dataset_dir = '/dataset'  # Update this path to point to your dataset folder

# Function to compare images pixel-wise
def compare_images(img1_path, img2_path):
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    if img1.shape == img2.shape:
        difference = cv2.subtract(img1, img2)
        b, g, r = cv2.split(difference)
        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            return True  # Images are identical
    return False  # Images are not identical


# List to store duplicate image paths
duplicate_images = []

# Iterate through subfolders in the dataset directory
for subdir in ['test', 'train', 'valid']:
    subfolder_path = os.path.join(dataset_dir, subdir)
    if os.path.isdir(subfolder_path):
        print(f"Processing images in folder: {subdir}")

        # Loop through all files in the subfolder
        for i, filename1 in enumerate(os.listdir(subfolder_path)):
            if filename1.endswith('.jpg'):
                image_path1 = os.path.join(subfolder_path, filename1)

                for j, filename2 in enumerate(os.listdir(subfolder_path)):
                    if j > i and filename2.endswith('.jpg'):  # Compare only with subsequent images
                        image_path2 = os.path.join(subfolder_path, filename2)

                        # Compare images pixel-wise
                        if compare_images(image_path1, image_path2):
                            duplicate_images.append(image_path2)

# Remove duplicate images
for dup_image in duplicate_images:
    os.remove(dup_image)
    print(f"Removed duplicate image: {dup_image}")

print("Duplicate image cleaning completed.")
