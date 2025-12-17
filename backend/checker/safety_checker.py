import os

def safety_checks(base_path):
    warnings = []

    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    code = f.read()

                # Infinite loop without sleep
                if "while True" in code and "sleep" not in code:
                    warnings.append({
                        "file": file_path,
                        "warning": "Infinite loop without sleep"
                    })

                # Unsafe joint limits
                if "JointTrajectory" in code and "3.14" in code:
                    warnings.append({
                        "file": file_path,
                        "warning": "Joint value near or exceeding limits"
                    })

    return warnings
