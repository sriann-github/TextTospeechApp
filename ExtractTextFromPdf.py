import PyPDF2

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

# pdf_path = "sample.pdf"
# extracted_text = extract_text_from_pdf(pdf_path)
# print(f"Extracted text: {extracted_text}")


# For documents: Use libraries like PyPDF2 for PDF and python-docx for Word documents to extract text.