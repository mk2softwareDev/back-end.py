from PIL import Image
import os


def convert_to_jpeg(file_path):
    # check if the file exists
    if not os.path.isfile(file_path):
        raise ValueError(f"File {file_path} does not exist.")

    # get the file extension
    file_extension = os.path.splitext(file_path)[1].lower()

    # check if the file extension is supported
    if file_extension not in ['.png', '.jpg', '.jpeg', '.bmp', '.gif']:
        raise ValueError(f"File extension {file_extension} is not supported.")

    # open the image and convert it to JPEG
    with Image.open(file_path) as img:
        img = img.convert('RGB')
        new_file_path = os.path.splitext(file_path)[0] + '.jpeg'
        img.save(new_file_path, 'JPEG', quality=90)

    # return the path of the new JPEG file
    return new_file_path
#TO-pdf
import subprocess
import os


def convert_to_pdf(file_path):
    # check if the file exists
    if not os.path.isfile(file_path):
        raise ValueError(f"File {file_path} does not exist.")

    # get the file extension
    file_extension = os.path.splitext(file_path)[1].lower()

    # check if the file extension is supported
    if file_extension not in ['.doc', '.docx', '.ppt', '.pptx', '.odt', '.ods', '.odp', '.xls', '.xlsx']:
        raise ValueError(f"File extension {file_extension} is not supported.")

    # convert the file to PDF using unoconv
    subprocess.run(['unoconv', '-f', 'pdf', file_path])

    # get the path of the new PDF file
    pdf_file_path = os.path.splitext(file_path)[0] + '.pdf'

    # check if the PDF file was created
    if not os.path.isfile(pdf_file_path):
        raise ValueError("PDF conversion failed.")

    # return the path of the new PDF file
    return pdf_file_path


from fpdf import FPDF
import os


def convert_to_pdf(file_path):
    # Get the name and extension of the file
    file_name, file_extension = os.path.splitext(file_path)

    # Check if the file is already a PDF
    if file_extension.lower() == '.pdf':
        return file_path

    # Create a new PDF object
    pdf = FPDF()

    # Add a page to the PDF
    pdf.add_page()

    # Set the font and font size
    pdf.set_font('Arial', size=12)

    # Read the file contents
    with open(file_path, 'rb') as f:
        file_contents = f.read()

    # Add the file contents to the PDF
    pdf.cell(200, 10, txt=file_contents)