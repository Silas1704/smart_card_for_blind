import cv2
import pytesseract

def preprocess_image(frame):
    # frame = cv2.flip(frame, 1)  # Flip around the y-axis (horizontal flip)
    
    # gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # binary_frame = cv2.adaptiveThreshold(gray_frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    #                                      cv2.THRESH_BINARY, 11, 2)
    # return binary_frame
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding to binarize the image
    binary_frame = cv2.adaptiveThreshold(gray_frame, 255, 
                                         cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY, 11, 2)
    return binary_frame

def detect_text(frame):
    processed_frame = preprocess_image(frame)

    # Perform OCR using Tesseract
    custom_config = r'--oem 3 --psm 6'
    detected_text = pytesseract.image_to_string(processed_frame, config=custom_config)

    return detected_text


# def test_text_detection(image_path):
#     if image_path.endswith(('.png', '.jpg', '.jpeg')):
#         # Load the image
#         frame = cv2.imread(image_path)

#         if frame is None:
#             print(f"Error: Could not read image '{image_path}'. Please check the path.")
#             return

#         # Detect text
#         detected_text = detect_text(frame)

#         # Print the detected text
#         print(f"Detected text in '{image_path}':")
#         print(detected_text.strip())  # Strip to remove leading/trailing whitespace
#         print("-" * 40)  # Separator

# # Example usage
# if __name__ == "__main__":
#     # Update this to the path of the image you want to test
#     image_path = "text.jpeg"  # Use forward slashes or double backslashes
#     test_text_detection(image_path)