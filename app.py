from flask import Flask, render_template, request, jsonify
from detector import CarDetector
import cv2
import numpy as np
import base64
import datetime

app = Flask(__name__)
detector = CarDetector('runs/detect/train2/weights/best.pt')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    try:
        image_data = request.json['image']
        if image_data.startswith('data:image'):
            image_data = image_data.split(',')[1]
            img_bytes = base64.b64decode(image_data)
        else:
            img_bytes = image_data.encode()

        img = cv2.imdecode(np.frombuffer(img_bytes, np.uint8), cv2.IMREAD_COLOR)

        detections = detector.detect_spaces(img)
        processed_img = detector.draw_boxes(img, detections)

        empty_count, occupied_count, total_count = detector.count_spaces(detections)

        _, buffer = cv2.imencode('.jpg', processed_img)
        img_base64 = base64.b64encode(buffer).decode('utf-8')

        return jsonify({
            'image': f'data:image/jpeg;base64,{img_base64}',
            'empty_spaces': empty_count,
            'occupied_spaces': occupied_count,
            'total_spaces': total_count
        })

    except Exception as e:
        print(f"Error during detection: {str(e)}")
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)