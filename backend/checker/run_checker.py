from zip_handler import extract_zip
from syntax_checker import check_python_files, check_cpp_files
from ros_structure_checker import find_ros_packages, check_ros_structure
from node_analyzer import analyze_ros_nodes
from safety_checker import safety_checks
from report_generator import generate_reports
import os
import sys


def run(zip_path):
    # Extract ZIP
    workspace = extract_zip(zip_path)

    errors = []
    warnings = []

    # -----------------------------
    # Python checks (WARNINGS ONLY)
    # -----------------------------
    python_warnings = check_python_files(workspace)
    warnings.extend(python_warnings)

    # -----------------------------
    # C++ checks (REAL ERRORS)
    # -----------------------------
    cpp_errors = check_cpp_files(workspace)
    errors.extend(cpp_errors)

    # -----------------------------
    # ROS package structure check
    # -----------------------------
    packages = find_ros_packages(workspace)
    if not packages:
        errors.append("No ROS package found")

    for pkg in packages:
        structure_errors = check_ros_structure(pkg)
        errors.extend(structure_errors)

    # -----------------------------
    # ROS node analysis
    # -----------------------------
    node_info = analyze_ros_nodes(workspace)

    # -----------------------------
    # Safety heuristics (WARNINGS)
    # -----------------------------
    safety_warnings = safety_checks(workspace)
    warnings.extend(safety_warnings)

    # -----------------------------
    # Generate reports
    # -----------------------------
    os.makedirs("reports", exist_ok=True)
    generate_reports(errors, warnings, node_info)

    print("Report generated in /reports")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 run_checker.py <path_to_zip>")
        sys.exit(1)

    zip_path = sys.argv[1]
    run(zip_path)

