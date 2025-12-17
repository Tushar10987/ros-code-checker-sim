import os

def find_ros_packages(base_path):
    packages = []

    for root, dirs, files in os.walk(base_path):
        if "package.xml" in files:
            packages.append(root)

    return packages


def check_ros_structure(pkg_path):
    errors = []

    if not os.path.exists(os.path.join(pkg_path, "package.xml")):
        errors.append("Missing package.xml")

    if not (
        os.path.exists(os.path.join(pkg_path, "setup.py")) or
        os.path.exists(os.path.join(pkg_path, "CMakeLists.txt"))
    ):
        errors.append("Missing setup.py or CMakeLists.txt")

    return errors
