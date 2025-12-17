import subprocess
import time

def launch_gazebo():
    print("[SIM] Launching Gazebo (visual-only, stable mode)...")

    subprocess.Popen(
        ["gazebo", "--verbose"]
    )

    time.sleep(5)

