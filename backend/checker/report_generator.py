import json

def generate_reports(errors, warnings, node_info, output_dir="reports"):
    report = {
        "status": "FAIL" if errors else "PASS",
        "errors": errors,
        "warnings": warnings,
        "nodes": node_info
    }

    with open(f"{output_dir}/report.json", "w") as f:
        json.dump(report, f, indent=2)

    with open(f"{output_dir}/report.txt", "w") as f:
        f.write(f"STATUS: {report['status']}\n\n")
        f.write("ERRORS:\n")
        for e in errors:
            f.write(str(e) + "\n")
        f.write("\nWARNINGS:\n")
        for w in warnings:
            f.write(str(w) + "\n")
