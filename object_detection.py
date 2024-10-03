import cv2
import torch

class ObjectDetector:
    def __init__(self):
        # Load the YOLOv5 model
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

    def detect_objects(self, frame):
        # Perform object detection
        results = self.model(frame)
        detections = results.pred[0]

        # List to store detected objects
        detected_objects = []

        # Draw bounding boxes and labels on the frame
        for det in detections:
            if det[4] >= 0.5:  # Confidence threshold
                x1, y1, x2, y2, conf, cls = det
                label = f"{self.model.names[int(cls)]} {conf:.2f}"
                detected_objects.append(label)

                # Draw bounding box on the frame
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)
                cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        return frame, detected_objects
