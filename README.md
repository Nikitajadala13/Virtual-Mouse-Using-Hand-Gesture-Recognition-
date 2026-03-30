# 🖱️ Virtual Mouse Using Hand Gesture Recognition

### 📌 Abstract
- This project implements a virtual mouse system using computer vision and hand gesture recognition. It allows users to control the computer cursor and perform actions such as clicking, scrolling, dragging, and taking screenshots without using a physical mouse. The system uses a webcam to detect hand movements and gestures in real time with the help of MediaPipe and OpenCV. By mapping finger positions to mouse actions, the project provides a touchless and intuitive human-computer interaction experience.

### 📖 Introduction
- This project demonstrates a virtual mouse system that tracks hand landmarks and interprets finger positions to perform mouse operations. It eliminates the need for physical hardware and enhances accessibility, especially in situations where touchless interaction is preferred.

### 🎯 Objectives
- To develop a virtual mouse using hand gestures.
- To detect and track hand landmarks using computer vision techniques.
- To map finger gestures to mouse actions like move, click, scroll, drag, and drop.
- To create a smooth and responsive cursor movement using interpolation and smoothing.
- To provide a touchless human-computer interaction system.

### ⚙️ Methodology
- Requirement Analysis: Identify gestures and corresponding mouse operations (move, click, scroll, etc.).
- Design Phase: Design gesture mappings based on finger combinations.

#### Development Phase:
- Use OpenCV to capture webcam input.
- Use MediaPipe to detect hand landmarks.
- Process finger positions to identify gestures.
- Use PyAutoGUI to control mouse actions.
- Apply smoothing techniques for stable cursor movement.

- Testing Phase: Test gesture accuracy, responsiveness, and performance under different lighting conditions.
- Deployment Phase: Run locally on a system with a webcam. Can be shared via GitHub.

### 💡 Proposed System
The proposed system replaces a physical mouse with hand gestures detected via a webcam.

#### Key Features:
- Cursor Movement: Controlled by index finger.
- Left Click: Index + Middle finger.
- Right Click: Middle finger.
- Double Click: Index + Middle + Ring finger.
- Scrolling:
- Scroll Up → Index + Ring
- Scroll Down → Middle + Ring
- Drag and Drop:
- Drag → Thumb + Index
- Drop → Index + Pinky
- Screenshot: Closed fist gesture
This system provides a real-time, touch-free interface for interacting with a computer.

### ⚙️ System Requirements
#### 🔹 Hardware Requirements:
- Processor: Intel i3 or above
- RAM: Minimum 4GB (8GB recommended)
- Webcam: Required for hand tracking
- Storage: At least 500MB free space
- Display: 1366x768 resolution or higher

#### 🔹 Software Requirements:
- Operating System: Windows / Linux / macOS
- Python Version: Python 3.7 or above
- IDE/Editor: VS Code / PyCharm / Jupyter Notebook
- Libraries:
- opencv-python
- mediapipe
- numpy
- pyautogui

### 👨‍💻 Tech Stack
- Python
- OpenCV (Computer Vision)
- MediaPipe (Hand Tracking)
- NumPy (Mathematical Operations)
- PyAutoGUI (Mouse Control Automation)

### 🖥️ Platform
- Desktop Application (Windows/Linux/macOS)
- Uses Webcam for real-time interaction

### 🚀 Innovation & Contribution
- Replaces traditional mouse with gesture-based control.
- Enables touchless interaction, useful in hygiene-sensitive environments.
- Demonstrates real-time hand tracking using MediaPipe.
- Implements smoothing for stable cursor movement.
- Provides additional features like screenshot capture using gestures.
- Can be extended with AI-based gesture recognition and custom controls.
