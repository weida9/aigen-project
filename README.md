# YOLO Object Detection Web App

## Overview

This project is a simple web-based application that performs real-time object detection using the YOLO (You Only Look Once) model. The frontend is built with HTML and Tailwind CSS, while the backend is powered by Flask and OpenCV. The application streams live video from the user's webcam and detects objects using a YOLO model.

## Features

- Real-time object detection using YOLOv8.
- Flask-based web server for streaming the video feed.
- OpenCV for handling video input and drawing bounding boxes.
- Web interface for displaying the detection results.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.7+
- pip (Python package manager)
- Flask
- OpenCV (cv2)
- PyTorch
- Ultralytics YOLOv8

## Installation

### 1. Clone the Repository

```sh
git clone https://github.com/your-repository/yolo-web-app.git
cd yolo-web-app
```

### 2. Install Dependencies

```sh
pip install flask opencv-python torch ultralytics
```

### 3. Download the YOLO Model

The application uses `yolov8n.pt` (a pre-trained YOLOv8 model). If not already downloaded, use the following command:

```sh
from ultralytics import YOLO
YOLO("yolov8n.pt")
```

## Usage

### 1. Start the Flask Server

Run the following command to start the Flask backend:

```sh
python main.py
```

This will start the server on `http://localhost:5000/`.

### 2. Open the Web Interface

Open your web browser and go to:

```
http://localhost:5000/
```

This will display the live object detection video feed.

## File Structure

```
yolo-web-app/
│── main.py           # Flask backend with YOLO object detection
│── index.html        # Frontend web page for video streaming
│── requirements.txt  # Dependencies list (optional)
```

## How It Works

1. The Flask server captures video frames using OpenCV.
2. The YOLO model processes each frame and detects objects.
3. The detected objects are drawn with bounding boxes.
4. The processed frames are streamed to the frontend as a live video feed.

## Configuration

- Modify the confidence threshold (`conf=0.4`) and IOU threshold (`iou=0.5`) in `main.py` to adjust detection sensitivity.
- The application defaults to using GPU if available; otherwise, it falls back to CPU.

## Troubleshooting

- **Camera Not Found:** Ensure your webcam is properly connected.
- **Module Not Found:** Ensure all dependencies are installed using `pip install -r requirements.txt`.
- **Server Not Running:** Check for errors in the terminal and ensure port 5000 is available.

## License

This project is open-source under the MIT License.

## Author

Developed by Anak Agung Gde Weida Ksatriawarma.

