import os
from PyPDF2 import PdfMerger

def combine_pdfs_in_directory(directory_path):
    # Ensure the provided path is valid
    if not os.path.isdir(directory_path):
        print("Invalid directory path.")
        return

    # List all PDF files in the directory
    pdf_files = [f for f in os.listdir(directory_path) if f.lower().endswith('.pdf')]
    pdf_files.sort()  # Sort alphabetically

    if not pdf_files:
        print("No PDF files found in the directory.")
        return

    # Initialize PdfMerger
    merger = PdfMerger()

    # Append each PDF
    for pdf in pdf_files:
        pdf_path = os.path.join(directory_path, pdf)
        merger.append(pdf_path)

    # Output file path
    output_path = os.path.join(directory_path, "combined_output.pdf")
    merger.write(output_path)
    merger.close()

    print(f"Combined PDF saved to: {output_path}")

dir = r"C:\Users\Piyus\OneDrive\Desktop\ksk docs"
combine_pdfs_in_directory(dir)
