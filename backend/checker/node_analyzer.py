import ast
import os

def analyze_ros_nodes(base_path):
    nodes_info = []

    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)

                try:
                    with open(file_path, "r") as f:
                        tree = ast.parse(f.read())
                except Exception:
                    continue

                publishers = []
                subscribers = []
                services = []

                for node in ast.walk(tree):
                    if isinstance(node, ast.Call):
                        if hasattr(node.func, "attr"):
                            if node.func.attr == "create_publisher":
                                publishers.append(file)
                            if node.func.attr == "create_subscription":
                                subscribers.append(file)
                            if node.func.attr == "create_service":
                                services.append(file)

                if publishers or subscribers or services:
                    nodes_info.append({
                        "file": file_path,
                        "publishers": len(publishers),
                        "subscribers": len(subscribers),
                        "services": len(services)
                    })

    return nodes_info
