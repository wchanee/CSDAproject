import cv2
import os
import matplotlib.pyplot as plt


def plot_histogram(image_path):
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Calculate the histogram
    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

    # Plot the histogram
    plt.figure()
    plt.title(f'Histogram for {os.path.basename(image_path)}')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.plot(histogram)
    plt.xlim([0, 256])
    plt.show()


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
                plot_histogram(image_path)
