import PyPDF2
import pytesseract
import cv2
import os
from pdf2image import convert_from_path


# encoded text extraction
def extract_encoded_pdf_text(pdf_file, page_start, page_end):
    pdf = PyPDF2.PdfReader(pdf_file)
    text = ''
    for page_num in range(page_start, page_end):
        text += pdf \
            .getPage(page_num) \
            .extract_text()
    print(text)
    return text

# scanned text extraction
def extract_pdf_to_images(pdf_file, page_start, page_end, image_dir=r"images"):
    with open(pdf_file, 'rb') as file:
        input_pdf = PyPDF2.PdfReader(pdf_file)
        output_pdf = PyPDF2.PdfWriter()

        for page_num in range(page_end-page_start):
            page = input_pdf.pages[page_num]
            output_pdf.add_page(page)

        with open('output.pdf', 'wb') as output_file:
            output_pdf.write(output_file)

    with open('output.pdf', 'rb') as file:
        pages = convert_from_path('output.pdf')   
        for i, page in enumerate(pages):
            page.save(f"{image_dir}/page_{i+1}.jpg", 'JPEG')
       
def extract_text_from_image(image_dir=r'images'):
    text = ''
    for image_file in os.listdir(image_dir):
        if image_file.endswith('.jpg'):
            image_path = os.path.join(image_dir, image_file)
            image = cv2.imread(image_path)    
            text += pytesseract.image_to_string(image) + '\n'
    print(text)
    return text

# chunk processing and file saving
def split_text(text, chunk_size):
    chunks = []
    current_chunk = ''
    words = text.split()
    print(words)
    for word in words:
        if len(current_chunk) + len(word) <= chunk_size:
            current_chunk += word + ' '
        else:
            chunks.append(current_chunk)
            current_chunk = word + ' '
    chunks.append(current_chunk)
    return chunks

def save_text_to_file(chunks, filename):
    with open(filename, 'w') as f:
        for chunk in chunks:
            f.write(chunk + '\n')

# processing 
def extraction_method():
    valid_options = ['scanned','encoded']
    user_input = 'encoded' #input("Enter extraction method: 'scanned' or 'encoded' ")
    return user_input
    while user_input not in valid_options:
        print("Enter either encoded or scanned.")
        user_input = input("Enter extraction method: 'scanned' or 'encoded' ")
    return user_input

# user input
def user_input(extraction_method):
    pdf_file = 'examples/test.pdf' #input("Enter the PDF's directory': ")
    page_start = 30 #int(input("Enter the starting page number: "))
    page_end = 60 #int(input("Enter the ending page number: "))
    chunk_size = 400 #int(input("Enter the desired chunk size (in words): "))
    filename = 'test' #input("Enter the text file name: ")

    text = ''
    if extraction_method == 'encoded':
        try:
            text = extract_encoded_pdf_text(pdf_file, page_start, page_end)
        except:
            print("File could not be found.")
    elif extraction_method == 'scanned':
        try:
            extract_pdf_to_images(pdf_file, page_start, page_end)
            for page_num in range(page_start, page_end):
                text += extract_text_from_image(page_num=page_num)
        except: 
            print("Scanned file could not be found.")
    chunks = split_text(text, chunk_size)
    save_text_to_file(chunks, filename) 
    print('Your file has been sent to your local directory.')


# program
if __name__ == '__main__':
    #user_input(extraction_method())
    extract_pdf_to_images('X:/Files/Programming/Projects/text_extraction_tool/examples/test.pdf', 50,53)



        