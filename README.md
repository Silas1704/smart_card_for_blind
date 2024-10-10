

---

# Smart Cap for the Visually Impaired

## Overview

The Smart Cap project assists visually impaired individuals by offering real-time object detection, face recognition, text reading, and voice-guided navigation. Using a combination of camera technology and AI-based image processing, the cap provides audio feedback for environmental awareness and navigation assistance.

## Features

- **Object Detection**: Detects objects around the user using the YOLOv5 algorithm and provides audio feedback.
- **Face Recognition**: Identifies known individuals and informs the user who is nearby.
- **Text Detection and Reading**: Detects text in the environment and reads it aloud using Pygame's text-to-speech functionality.
- **Voice-Guided Navigation**: Provides real-time direction guidance using GPS and voice commands.

## Tech Stack

- **Hardware**:
  - Raspberry Pi (or laptop)
  - Camera Module (or laptop camera)

- **Software**:
  - **YOLOv5**: For object detection
  - **OpenCV**: For computer vision tasks like face recognition
  - **Tesseract OCR**: For text detection and reading
  - **Pygame**: For text-to-speech functionality
  - **Python**: Primary programming language
  - **geopy & GPS modules**: For location and navigation
  - **Google Maps API / OpenStreetMap API**: For navigation assistance

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/smart-cap-project.git
   ```

2. **Set up the environment**:
   - Install dependencies using `pip`:
     ```bash
     pip install -r requirements.txt
     ```

3. **Set up YOLOv5**:
   - Clone the YOLOv5 repository:
     ```bash
     git clone https://github.com/ultralytics/yolov5
     ```
   - Follow YOLOv5 setup instructions.

4. **Install Pygame**:
   - For text-to-speech functionality:
     ```bash
     pip install pygame
     ```

5. **Connect Camera**:
   - If using Raspberry Pi, connect the Pi Camera Module.
   - If using a laptop, ensure the webcam is properly configured.

## Usage

1. **Run Object Detection**:
   - Detect objects and get audio feedback:
     ```bash
     python main.py
     ```

2. **Run Face Recognition**:
   - Recognize faces from the `known_faces` folder:
     ```bash
     python recognize_faces.py
     ```

3. **Run Text Detection**:
   - Detect and read aloud text using Pygame:
     ```bash
     python text_to_speech.py
     ```

4. **Run Navigation**:
   - Start GPS-based navigation assistance:
     ```bash
     python navigate.py
     ```



## Future Enhancements

- Integrate CLIP model for better image-text understanding.
- Enhance navigation with real-time obstacle avoidance.
- Add multi-language support for text reading and speech.

## Contributing

Contributions are welcome! Fork the repository and create a pull request with any improvements or features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

This version includes the use of **Pygame** for text-to-speech functionality in the text reading feature.
