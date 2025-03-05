import pdfplumber

# pass it through pdfplumber to extract text and tables
def pdfplumber_extraction(pdf_loc):
    text = ""
    with pdfplumber.open(pdf_loc) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    print("Reading document completed")
    return text