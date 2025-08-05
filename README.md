# CombineNCERTzippedPDFsZIPsIntoOne
Combine multiple NCERT zips that have split PDFs into one file on Windows with one click.

# NCERT Zipped PDF Merger

> ⚠️ **AI-generated Notice**: This tool was built with significant assistance from AI (ChatGPT by OpenAI) and is not entirely original work. The final result has been tested and refined for practical use.

## 📚 Purpose

This tool is specifically designed to **combine split NCERT textbook PDF files that are stored inside ZIP archives**. It processes multiple `.zip` files in a folder, each containing parts of a book (e.g., `book-1.pdf`, `book-2.pdf`, etc.), and merges them into a single PDF file for each archive.

It is **not a general-purpose PDF merger**, but a **purpose-built utility for NCERT book distribution formats**, which are often split into parts and zipped.

---

## 🔧 Features

- 📦 Supports batch processing of multiple `.zip` files in a directory.
- 🔍 Automatically extracts ZIPs and detects PDF parts.
- 🔗 Merges PDF parts in order into a single PDF per book.
- 🚫 Skips any broken or corrupt zip/PDFs and shows errors at the end.
- 🪄 Simple terminal interface with a real-time progress bar.
- 🧪 Tested on real-world NCERT ZIPs downloaded from official/state sites.

---

## 📁 How to Prepare Your Folder

* Place all `.zip` files in one folder named `zips`.
* Each `.zip` should contain split parts of a single NCERT book (PDF format).
* Example:

  ```
  Class10-History.zip/
    ├── history-1.pdf
    ├── history-2.pdf
    └── history-3.pdf
  ```

## 🖥️ Installation & Usage

### Option 1: 📦 Use the Windows Executable

If you don’t have Python or pip installed:

1. Go to the [Releases](https://github.com/ni6hant/CombineNCERTzippedPDFsZIPsIntoOne/releases) section.
2. Download the latest `.exe` file.
3. Place all your zips in a folder named "zips" and move the .exe file.
4. The zips folder and the .exe should be in the same location. Note: .exe file is not inside the zips folder.
5. Double-click to run.

✅ No installation required.

---

### Option 2: 🐍 Run from Python source (`.py`)

1. **Install Python** (if not already installed):  
   [Download Python](https://www.python.org/downloads/)

2. **Install required packages**:
   ```bash
   pip install PyPDF2 tqdm
    ```

3. **Run the script**:

   ```bash
   python ncert_zip_pdf_merger.py
   ```




After running, the folder will contain:

* Extracted folders for each ZIP.
* One combined `.pdf` per ZIP (e.g., `Class10-History_merged.pdf`).

---

## ❗ Limitations

* Only works on ZIP files containing **PDF files**.
* Does not support password-protected or encrypted ZIPs/PDFs.
* File ordering assumes consistent naming (e.g., `book-1.pdf`, `book-2.pdf`).

---

## 📜 License

MIT License — free to use, modify, and distribute.
Attribution appreciated.

---

## 🤖 Built with Help from AI

This project was built with assistance from [ChatGPT (GPT-4)](https://openai.com/chatgpt).
All logic, error handling, and user experience were designed through AI-guided iterations.

```
