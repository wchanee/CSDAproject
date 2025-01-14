from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a yolov8 model from scratch

# Use the model
results = model.train(data="data.yaml", epochs=15)