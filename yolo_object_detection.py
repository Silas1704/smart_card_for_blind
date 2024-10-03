import cv2
import torch
from gtts import gTTS
import os
import time

# Load the YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Function to convert text to speech using gTTS
def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    filename = "output.mp3"
    tts.save(filename)
    os.system(f"start {filename}")  # Change "start" to "open" for macOS or "xdg-open" for Linux

# Open the camera
cap = cv2.VideoCapture(0)  # 0 for laptop camera

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Perform object detection
    results = model(frame)
    detections = results.pred[0]

    # Draw bounding boxes and labels on the frame
    for det in detections:
        if det[4] >= 0.5:  # Confidence threshold
            x1, y1, x2, y2, conf, cls = det
            label = f"{model.names[int(cls)]} {conf:.2f}"
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)
            cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
            
            # Convert detected object name to speech
            text_to_speech(model.names[int(cls)])

    # Show the output frame
    cv2.imshow('Object Detection', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()
