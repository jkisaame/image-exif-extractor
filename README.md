# Image EXIF Extractor

A lightweight, cross-platform graphical user interface (GUI) utility written in Python that allows users to easily extract embedded EXIF metadata from images and save it to a text file.

This repository supports development across Windows x86 and Windows ARM64 architectures, with binaries compiled via PyInstaller.

## Features
* **Simple GUI:** Intuitive layout built entirely with native Python interface components.
* **Automated Extraction:** Instantly reads and decodes standard EXIF tags (e.g., camera model, shutter speed, GPS data) from selected images.
* **Auto-Save Functionality:** Automatically exports extracted metadata to a formatted `.txt` file in the same directory as the source image.
* **Open Source:** Released under the GPL 3.0 License.

---

## Technical Specifications & Dependencies

### Prerequisites
To run the source code directly, you need **Python 3.x** installed on your system.

### Standard Libraries Used
These packages come pre-installed with Python and require no extra installation:
* `os` — Manages file paths, directory matching, and file naming structures.
* `tkinter` / `ttk` — Handles the window layout, configuration settings, and button actions.
* `filedialog` / `messagebox` — Powers the native OS file selectors and popup notifications.
* `scrolledtext` — Provides the scrollable, read-only text area for reviewing metadata in the GUI.

### Third-Party Dependencies
The application relies on the **Pillow (PIL)** library for robust image handling and metadata querying. Install it via pip:

```bash
pip install Pillow
