from ultralytics import YOLO
import cv2
import numpy as np
from parking_manager import ParkingManager

class CarDetector:
    def __init__(self, model_path='runs/detect/train2/weights/best.pt'):
        self.model = YOLO(model_path)
        self.class_names = ['space-empty', 'space-occupied']
        self.parking_manager = ParkingManager()

    def preprocess_image(self, image):
        return cv2.resize(image, (640, 640))

    def detect_spaces(self, image):
        preprocessed_image = self.preprocess_image(image)
        results = self.model(preprocessed_image)
        detections = results[0].boxes.data.cpu().numpy()
        return self.post_process_detections(detections)

    def post_process_detections(self, detections, confidence_threshold=0.25, iou_threshold=0.45):
        high_conf_detections = detections[detections[:, 4] > confidence_threshold]
        return self.non_max_suppression(high_conf_detections, iou_threshold)

    def non_max_suppression(self, boxes, iou_threshold):
        return boxes

    def draw_boxes(self, image, detections):
        for det in detections:
            x1, y1, x2, y2, conf, cls = det
            class_name = self.class_names[int(cls)]
            color = (0, 255, 0) if class_name == 'space-empty' else (0, 0, 255)
            cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)
            label = f'{class_name}: {conf:.2f}'
            cv2.putText(image, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        return image

    def count_spaces(self, detections):
        empty_count = sum(1 for det in detections if int(det[5]) == 0)  # 'space-empty' has class index 0
        occupied_count = sum(1 for det in detections if int(det[5]) == 1)  # 'space-occupied' has class index 1
        total_count = empty_count + occupied_count
        return empty_count, occupied_count, total_count