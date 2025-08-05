import os
import zipfile
import shutil
from PyPDF2 import PdfMerger
from tqdm import tqdm

# === CONFIGURATION ===
input_dir = 'zips'           # Folder containing .zip files
output_dir = 'output_pdfs'   # Folder to save final combined PDFs
temp_dir = 'temp_unzip'      # Temporary folder to extract each ZIP

# Create output directory if not exists
os.makedirs(output_dir, exist_ok=True)

# Collect errors
errors = []

# Get all ZIP files in the input directory
zip_files = [f for f in os.listdir(input_dir) if f.lower().endswith('.zip')]

for zip_file in tqdm(zip_files, desc="Processing ZIP files"):
    zip_path = os.path.join(input_dir, zip_file)
    base_name = os.path.splitext(zip_file)[0]

    try:
        # Step 1: Extract ZIP
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        os.makedirs(temp_dir, exist_ok=True)

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)

        # Step 2: Find and sort PDFs
        pdf_files = [f for f in os.listdir(temp_dir) if f.lower().endswith('.pdf')]

        if not pdf_files:
            raise Exception("No PDFs found in ZIP.")

        first_file = [f for f in pdf_files if f.lower().endswith('1ps.pdf')]
        if not first_file:
            raise Exception("No 1ps.pdf file found.")

        remaining = [f for f in pdf_files if f != first_file[0]]
        remaining.sort()  # Sort numerically/alphabetically

        ordered_files = first_file + remaining

        # Step 3: Merge PDFs
        merger = PdfMerger()
        for pdf_name in ordered_files:
            merger.append(os.path.join(temp_dir, pdf_name))

        output_path = os.path.join(output_dir, base_name + '_combined.pdf')
        merger.write(output_path)
        merger.close()

    except Exception as e:
        errors.append(f"{zip_file}: {e}")

    finally:
        # Clean up
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)

# === Summary ===
print("\n✅ All ZIPs processed.")
if errors:
    print("\n❌ Errors encountered:")
    for err in errors:
        print(" -", err)
else:
    print("🎉 No errors!")
