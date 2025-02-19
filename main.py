import cv2
import torch
import random
from ultralytics import YOLO
from flask import Flask, Response, render_template

app = Flask(__name__)

# Load YOLO model
model = YOLO("yolov8n.pt").to("cuda" if torch.cuda.is_available() else "cpu")

# Dictionary to store unique colors for each detected object category
color_map = {}

def get_color(label):
    if label not in color_map:
        color_map[label] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return color_map[label]

def generate_frames():
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        # Perform YOLO detection
        results = model(frame, conf=0.4, iou=0.5)

        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                label = model.names[int(box.cls[0])]
                conf = box.conf[0].item()
                color = get_color(label)

                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        # Encode frame as JPEG
        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    cap.release()

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
