import subprocess
import os

def check_python_files(base_path):
    """
    Run flake8, but treat ALL output as warnings, not errors.
    """
    warnings = []

    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)

                result = subprocess.run(
                    ["flake8", file_path],
                    capture_output=True,
                    text=True
                )

                if result.stdout:
                    warnings.append({
                        "file": file_path,
                        "warning": result.stdout.strip()
                    })

    return warnings


def check_cpp_files(base_path):
    """
    C++ syntax errors ARE real errors.
    """
    errors = []

    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith(".cpp"):
                file_path = os.path.join(root, file)

                result = subprocess.run(
                    ["g++", "-fsyntax-only", file_path],
                    capture_output=True,
                    text=True
                )

                if result.stderr:
                    errors.append({
                        "file": file_path,
                        "error": result.stderr.strip()
                    })

    return errors

