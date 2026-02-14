
from pdf2image import convert_from_path # PDF reader
import pytesseract                      # Image scanner and returns text


# Makes sure you have a certain file name in the dataset
pdf_path = "data/syllabi/syllabi_redacted/pdf/1. Syllabus 2023.pdf" 

print(f"I am starting to read: {pdf_path}...")

# Here I convert PDFs to images
# We set dpi=300 for higher image resolution
images = convert_from_path(pdf_path, dpi=300)

full_text = ""

for i, image in enumerate(images):
    print(f"  Reading page {i + 1}...")
    
    # This scans the image and returns a string of text
    page_text = pytesseract.image_to_string(image)
   
    full_text += f"\n--- Start of Page {i + 1} ---\n"
    full_text += page_text

# Saves the text to a .txt file
with open("collected_info.txt", "w") as f:
    f.write(full_text)

print("Finished! Open 'collected_info.txt' to see the result.")