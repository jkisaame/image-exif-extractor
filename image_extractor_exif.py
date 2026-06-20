import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import scrolledtext
from PIL import Image
from PIL.ExifTags import TAGS

class ExifExtractorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image EXIF Extractor")
        # FIX: Changed invalid string operator to standard Tkinter geometry 'x'
        self.root.geometry("700x500")
        self.root.minsize(600, 400)
        
        self.image_path = None
        self.exif_data_dict = {}

        self.create_widgets()

    def create_widgets(self):
        # Top Frame for Buttons
        button_frame = tk.Frame(self.root, pady=10)
        button_frame.pack(fill=tk.X)

        # FIX: Corrected padding parameters from 'px/py' to 'padx/pady'
        self.btn_select = tk.Button(button_frame, text="Select Image File", command=self.select_image, padx=10, pady=5)
        self.btn_select.pack(side=tk.LEFT, padx=20)

        self.btn_extract = tk.Button(button_frame, text="Extract EXIF Data", command=self.extract_exif, state=tk.DISABLED, padx=10, pady=5)
        self.btn_extract.pack(side=tk.LEFT, padx=10)

        # File Label Indicator
        self.lbl_file = tk.Label(self.root, text="No image selected", fg="gray", anchor="w", padx=20)
        self.lbl_file.pack(fill=tk.X)

        # Text Box Frame for Results
        text_frame = tk.Frame(self.root, pady=10, padx=20)
        text_frame.pack(fill=tk.BOTH, expand=True)

        self.txt_display = scrolledtext.ScrolledText(text_frame, wrap=tk.WORD, font=("Courier", 10))
        self.txt_display.pack(fill=tk.BOTH, expand=True)

    def select_image(self):
        file_types = [("Image Files", "*.jpg *.jpeg *.png *.tiff *.webp"), ("All Files", "*.*")]
        selected_file = filedialog.askopenfilename(title="Select an Image", filetypes=file_types)
        
        if selected_file:
            self.image_path = selected_file
            self.lbl_file.config(text=f"Selected: {os.path.basename(selected_file)}", fg="black")
            self.btn_extract.config(state=tk.NORMAL)
            self.clear_display()

    def clear_display(self):
        self.txt_display.config(state=tk.NORMAL)
        self.txt_display.delete('1.0', tk.END)
        self.txt_display.config(state=tk.DISABLED)

    def extract_exif(self):
        if not self.image_path:
            return

        self.exif_data_dict.clear()
        self.txt_display.config(state=tk.NORMAL)
        self.txt_display.delete('1.0', tk.END)

        try:
            with Image.open(self.image_path) as img:
                # Retrieve EXIF data
                info = img._getexif()
                
                if info is None:
                    output_text = "No embedded EXIF metadata found in this image."
                else:
                    output_text = f"--- EXIF Metadata for {os.path.basename(self.image_path)} ---\n\n"
                    for tag, value in info.items():
                        decoded_tag = TAGS.get(tag, tag)
                        self.exif_data_dict[decoded_tag] = value
                        output_text += f"{decoded_tag}: {value}\n"
                    
                    self.save_exif_to_file()

                self.txt_display.insert(tk.END, output_text)
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read image metadata:\n{str(e)}")
            
        finally:
            self.txt_display.config(state=tk.DISABLED)

    def save_exif_to_file(self):
        if not self.exif_data_dict:
            return
            
        # Determine paths
        img_dir = os.path.dirname(self.image_path)
        img_name, _ = os.path.splitext(os.path.basename(self.image_path))
        output_filename = f"{img_name}_exif.txt"
        output_filepath = os.path.join(img_dir, output_filename)

        try:
            with open(output_filepath, "w", encoding="utf-8") as txt_file:
                txt_file.write(f"Metadata Extracted from: {self.image_path}\n")
                txt_file.write("="*50 + "\n")
                for key, val in self.exif_data_dict.items():
                    txt_file.write(f"{key}: {val}\n")
            
            messagebox.showinfo("Success", f"EXIF metadata successfully extracted and saved to:\n{output_filepath}")
        except Exception as e:
            messagebox.showerror("Save Error", f"Could not save text file:\n{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExifExtractorApp(root)
    root.mainloop()