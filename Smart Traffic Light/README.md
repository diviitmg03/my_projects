# 🚦 Smart Traffic Management System

## 📖 About the Project
This Smart Traffic Management System is designed to optimize waiting times at traffic intersections by utilizing real-time vehicle detection. The system employs a combination of Arduino, YOLOv5, and Python to create an efficient, dynamic, and cost-effective solution for modern traffic challenges.

---

## 🛠 Features
- Real-time vehicle detection using YOLOv5.
- Dynamic control of traffic lights based on traffic density.
- Cost-effective setup leveraging phone cameras for video input.
- Modular and scalable design for future enhancements.

---

## 💻 Technologies Used
- **Hardware:** Arduino Uno, LEDs, Breadboard, Jumper wires.
- **Software:** Arduino IDE, YOLOv5, Python, OpenCV, DroidCam.

---

## 📋 Prerequisites
Ensure the following are installed:
- [Arduino IDE](https://www.arduino.cc/en/software)
- YOLOv5 repository (`pip install torch torchvision`).
- Python 3.7+ and required libraries (`opencv-python`, `Pillow`, etc.).

## 🔧 Hardware Requirements
- **Arduino Uno:** For controlling the LEDs.
- **LEDs and Resistors:** Simulating traffic lights.
- **Breadboard and Jumper Wires:** Circuit prototyping.
- **Phone Camera:** Capturing real-time traffic data.
- **Laptop:** Processing and decision-making unit.

## 🛠 Software Setup

### 📷 Step 1: Setup Camera
- Ensure your phone and laptop are connected to the same Wi-Fi network.
- Use DroidCam to stream the phone's camera feed to the laptop.

### 🚗 Step 2: Model Car Detection
- Use YOLOv5 for real-time vehicle detection.

### 🔌 Step 3: Arduino Setup
- Connect the Arduino to the laptop via a MicroUSB cable.
- Upload the provided Arduino code using the Arduino IDE.

## 🚀 Usage
- Power up the Arduino Uno and ensure all connections are secure.
- Run the Python script for real-time traffic detection and signal control.
- Observe the dynamic changes in the traffic lights based on the density of vehicles on each lane.


The detailed report of this project can be found in [report](report.pdf)