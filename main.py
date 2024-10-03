import cv2
from text_to_speech import text_to_speech  # Import the text_to_speech function
from ocr_detection import detect_text  # Import the OCR function
from object_detection import ObjectDetector  # Import the ObjectDetector class

def main():
    # Initialize the object detector
    object_detector = ObjectDetector()

    # Open the camera
    cap = cv2.VideoCapture(0)  # 0 for laptop camera

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Detect objects in the frame
        frame, detected_objects = object_detector.detect_objects(frame)

        # Check for detected objects
        if detected_objects:
            # Convert detected object names to speech
            for obj in detected_objects:
                text_to_speech(obj)

        # Use the OCR function to detect text
        detected_text = detect_text(frame)
        
        if detected_text.strip():  # Check if any text is detected
            text_to_speech(detected_text)  # Read aloud the detected text

        # Show the output frame
        cv2.imshow('Object Detection', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
