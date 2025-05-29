import torch
import cv2
import os

# Load YOLOv5 model from torch hub
model = torch.hub.load('ultralytics/yolov5', 'custom', path='models/helmet_yolov5.pt')  # Add your model path

# Run detection on an image
def detect(image_path):
    img = cv2.imread(image_path)
    results = model(img)
    results.print()
    results.show()

if __name__ == "__main__":
    image_path = "images/sample.jpg"  # Replace with your image path
    detect(image_path)
