from flask import Flask, render_template, request
import os
import subprocess

app = Flask(__name__)

UPLOAD_DIR = "uploads"
REPORT_DIR = "reports"
PREVIEW_DIR = "web/static/preview"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(PREVIEW_DIR, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    report = None
    image = None

    if request.method == "POST":
        file = request.files["zipfile"]
        zip_path = os.path.join(UPLOAD_DIR, file.filename)
        file.save(zip_path)

        # Run checker
        subprocess.run([
            "python3",
            "backend/checker/run_checker.py",
            zip_path
        ])

        with open("reports/report.txt") as f:
            report = f.read()

        # If PASS → run simulation
        if "STATUS: PASS" in report:
            subprocess.run([
                "python3",
                "backend/simulator/run_simulation.py"
            ])

            image = "preview/frame.png"

    return render_template(
        "index.html",
        report=report,
        image=image
    )

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)

