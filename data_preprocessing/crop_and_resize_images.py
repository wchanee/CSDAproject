import cv2
import os

def crop_and_resize_image(img, crop_coords, size=(500, 500)):
    # Crop image using crop coordinates (x, y, width, height)
    x, y, w, h = crop_coords
    cropped_img = img[y:y+h, x:x+w]
    # Resize image
    resized_img = cv2.resize(cropped_img, size, interpolation=cv2.INTER_AREA)
    return resized_img

def preprocess_images(input_dir, output_dir, crop_coords, size=(500, 500)):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for root, _, files in os.walk(input_dir):
        # Determine the relative path to create the same structure in the output directory
        relative_path = os.path.relpath(root, input_dir)
        output_subdir = os.path.join(output_dir, relative_path)

        # Create subdirectories in the output directory if they don't exist
        if not os.path.exists(output_subdir):
            os.makedirs(output_subdir)

        for file in files:
            if file.lower().endswith('.jpg'):
                input_path = os.path.join(root, file)
                output_path = os.path.join(output_subdir, file)

                try:
                    img = cv2.imread(input_path)

                    # Crop and resize image
                    processed_img = crop_and_resize_image(img, crop_coords, size)

                    # Save processed image
                    cv2.imwrite(output_path, processed_img)

                    print(f"Cropped and resized {input_path} and saved to {output_path}")
                except Exception as e:
                    print(f"Error processing {input_path}: {e}")

# Define the paths
input_directory = os.path.join(os.path.dirname(__file__), '../dataset')
output_directory = os.path.join(os.path.dirname(__file__), '../data_preprocessing/cropped_resized_dataset')

# Define the crop coordinates (x, y, width, height)
crop_coordinates = (50, 50, 500, 500)  # Example coordinates, adjust as needed

# Run the preprocessing process
preprocess_images(input_directory, output_directory, crop_coordinates)

print("Image cropping and resizing completed.")
