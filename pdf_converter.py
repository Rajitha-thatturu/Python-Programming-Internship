import os
import fitz  # PyMuPDF library for working with PDFs
from PIL import Image

def convert_pdf_to_text(pdf_path, text_path):
    """
    Converts a PDF file to plain text and saves it to a text file.
    :param pdf_path: Path to the input PDF file
    :param text_path: Path to save the output text file
    """
    try:
        doc = fitz.open(pdf_path)  # Open the PDF document
        text = ""
        for page in doc:
            text += page.get_text("text")  # Extract text from each page
        with open(text_path, "w", encoding="utf-8") as txt_file:
            txt_file.write(text)  # Save extracted text to a text file
        print(f"Text extracted and saved to {text_path}")
    except Exception as e:
        print(f"Error converting PDF to text: {e}")

def convert_pdf_to_images(pdf_path, images_folder):
    """
    Converts each page of a PDF to images (PNG format) and saves them to a specified folder.
    :param pdf_path: Path to the input PDF file
    :param images_folder: Folder to save the output images
    """
    try:
        doc = fitz.open(pdf_path)  # Open the PDF document
        os.makedirs(images_folder, exist_ok=True)  # Create the output folder if it doesn't exist
        for page_num, page in enumerate(doc):
            image_path = os.path.join(images_folder, f"page_{page_num + 1}.png")
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # Increase resolution for better quality
            img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
            img.save(image_path, format="PNG")  # Save each page as a PNG image
        print(f"Images saved to {images_folder}")
    except Exception as e:
        print(f"Error converting PDF to images: {e}")

# Example usage:
if __name__ == "__main__":
    input_pdf = "example.pdf"
    output_text = "example.txt"
    output_images = "images"

    convert_pdf_to_text(input_pdf, output_text)
    convert_pdf_to_images(input_pdf, output_images)
