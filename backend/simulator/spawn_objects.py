import subprocess
import os

def spawn_cube():
    sdf_path = os.path.abspath(
        "backend/simulator/models/cube.sdf"
    )

    print("[SIM] Spawning cube from SDF:", sdf_path)

    subprocess.run([
        "ros2", "run", "gazebo_ros", "spawn_entity.py",
        "-entity", "cube",
        "-file", sdf_path,
        "-x", "0.5",
        "-y", "0",
        "-z", "0.5"
    ])

