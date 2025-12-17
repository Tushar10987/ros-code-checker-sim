import os
import time
import subprocess

PREVIEW_DIR = os.path.abspath("backend/static/preview")
PREVIEW_FILE = os.path.join(PREVIEW_DIR, "frame.png")


def run_simulation():
    print("[SIM] Starting Gazebo preview...")

    os.makedirs(PREVIEW_DIR, exist_ok=True)

    # Start Gazebo
    subprocess.Popen(["gazebo", "--verbose"])
    time.sleep(6)

    # Spawn robot
    subprocess.run([
        "gz", "model",
        "--spawn-file", "backend/simulator/robot/simple_arm.sdf",
        "--model-name", "simple_arm"
    ])

    # Spawn cube
    subprocess.run([
        "gz", "model",
        "--spawn-file", "backend/simulator/models/cube.sdf",
        "--model-name", "cube"
    ])

    # Allow rendering
    time.sleep(4)

    print("[SIM] Please CLICK on the Gazebo window now...")

    # Capture the active window using ImageMagick
    subprocess.run([
        "import",
        "-window", "root",
        PREVIEW_FILE
    ])

    print("[SIM] Screenshot saved at:", PREVIEW_FILE)


if __name__ == "__main__":
    run_simulation()

