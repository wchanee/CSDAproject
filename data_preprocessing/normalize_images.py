import cv2
import os

# Function to normalize images to [0, 1] range
def normalize_image(img):
    return img.astype('float32') / 255.0

def normalize_images(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for root, _, files in os.walk(input_dir):
        # Determine the relative path to create the same structure in the output directory
        relative_path = os.path.relpath(root, input_dir)
        output_subdir = os.path.join(output_dir, relative_path)

        if not os.path.exists(output_subdir):
            os.makedirs(output_subdir)

        for file in files:
            if file.lower().endswith('.jpg'):
                input_path = os.path.join(root, file)
                output_path = os.path.join(output_subdir, file)

                try:
                    img = cv2.imread(input_path)

                    # Normalize image
                    img_normalized = normalize_image(img)

                    # Save normalized image
                    cv2.imwrite(output_path, img_normalized * 255.0)

                    print(f"Normalized {input_path} and saved to {output_path}")
                except Exception as e:
                    print(f"Error processing {input_path}: {e}")

# Define the paths
input_directory = os.path.join(os.path.dirname(__file__), '../dataset')
output_directory = os.path.join(os.path.dirname(__file__), '../normalized_dataset')

# Run the normalization process
normalize_images(input_directory, output_directory)

print("Image normalization completed.")
