import subprocess
import os

def spawn_robot():
    sdf_path = os.path.abspath(
        "backend/simulator/robot/simple_arm.sdf"
    )

    print("[SIM] Spawning robot (SDF visual-only):", sdf_path)

    subprocess.run([
        "gazebo", "--verbose", sdf_path
    ])

