# ROS Code Checker and Simulation Preview Tool

## Overview
This project is a **ROS/ROS2 Code Validation and Simulation Preview System** designed to automatically check robotic arm ROS code for correctness and safety, and then visualize it in a Gazebo-based simulation through a minimal web interface.

The tool reflects real-world robotics workflows:
- Static code validation
- ROS package structure verification
- Safety heuristics
- Simulation-based preview
- Structured reporting

---

## Features

### 1. ROS Code Checker
- Accepts a **ZIP file** containing a ROS/ROS2 package
- Performs:
  - Python syntax checks (via `flake8`, non-blocking warnings)
  - C++ syntax checks (`g++ -fsyntax-only`)
  - ROS package structure validation (`package.xml`, `setup.py` / `CMakeLists.txt`)
  - ROS node analysis (publishers, subscribers, services)
  - Basic motion-safety heuristics
- Generates:
  - Human-readable text report
  - Structured JSON report

---

### 2. Simulation Preview (Gazebo)
- Launches **Gazebo Classic** with:
  - Simple robotic arm model
  - Cube object in the scene
- Spawns models deterministically
- Captures a **simulation preview image** (Wayland-safe screen capture)
- Designed for stability across systems

---

### 3. Minimal Web Interface
- Upload ROS package ZIP
- View checker report (PASS / FAIL with warnings)
- Automatically trigger simulation on PASS
- Display simulation preview image

---


---

## Requirements

### System
- Ubuntu 20.04 / 22.04
- Python 3.8+
- ROS 2 (Humble recommended)
- Gazebo Classic (11)
- GNOME desktop (for Wayland-safe screenshots)

### Python Dependencies
pip install flask flake8


How to Run
1. Clone Repository
git clone https://github.com/Tushar10987/ros-code-checker-sim.git
cd ros-code-checker-sim

2. Start the Web Application
python3 backend/app.py

Open in browser:
http://127.0.0.1:5000










