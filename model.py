import os
from ultralytics import YOLO

# Get the absolute path of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to your data.yaml file
data_yaml_path = os.path.join(script_dir, "data.yaml")

# Verify that the data.yaml file exists
if not os.path.exists(data_yaml_path):
    raise FileNotFoundError(f"data.yaml not found at {data_yaml_path}")

# Load a pretrained model
model = YOLO("yolov8_model/yolov8n.pt")  # Load pretrained YOLOv8n model

# Use the model with the absolute path to data.yaml
results = model.train(data=data_yaml_path, epochs=30, lr0=0.01)

print("Training completed. Results:", results)
