import zipfile
import os
import shutil

def extract_zip(zip_path, extract_dir="workspace"):
    # Clean old workspace
    if os.path.exists(extract_dir):
        shutil.rmtree(extract_dir)

    os.makedirs(extract_dir, exist_ok=True)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)

    return extract_dir
