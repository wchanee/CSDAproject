import cv2
import os
import numpy as np

def detect_outliers(img, threshold=2.5):
    mean_intensity = np.mean(img)
    std_intensity = np.std(img)

    # Define a threshold based on mean and standard deviation
    lower_threshold = mean_intensity - threshold * std_intensity
    upper_threshold = mean_intensity + threshold * std_intensity

    # Identify outliers (values outside the threshold range)
    outliers_mask = np.logical_or(img < lower_threshold, img > upper_threshold)

    return outliers_mask

def resolve_outliers(img, outliers_mask, method='median'):
    if method == 'median':
        # Replace outliers with median pixel value of non-outliers
        img_no_outliers = img.copy()
        non_outliers = img[~outliers_mask]
        median_value = np.median(non_outliers)
        img_no_outliers[outliers_mask] = median_value
        return img_no_outliers
    else:
        raise ValueError(f"Unsupported method: {method}. Choose 'median'.")

def preprocess_images_with_outlier_detection(input_dir, output_dir, threshold=2.5, method='median'):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith('.jpg'):
                input_path = os.path.join(root, file)
                output_path = os.path.join(output_dir, file)

                try:
                    img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

                    # Detect outliers
                    outliers_mask = detect_outliers(img, threshold)

                    # Resolve outliers
                    img_no_outliers = resolve_outliers(img, outliers_mask, method)

                    # Save processed image
                    cv2.imwrite(output_path, img_no_outliers)

                    print(f"Processed {input_path}, resolved outliers, and saved to {output_path}")
                except Exception as e:
                    print(f"Error processing {input_path}: {e}")

# Define the paths
input_directory = os.path.join(os.path.dirname(__file__), '../cropped_resized_dataset')
output_directory = os.path.join(os.path.dirname(__file__), '../data_preprocessing/outlier_images')

# Run the preprocessing process with outlier detection and resolution
preprocess_images_with_outlier_detection(input_directory, output_directory, threshold=2.5, method='median')

print("Image preprocessing with outlier detection and resolution completed.")
