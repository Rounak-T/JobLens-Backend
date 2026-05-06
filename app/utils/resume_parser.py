'''
Functions:
- Accepts file
- Detects if it's a PDF or DOCX
- Extract the text
- Clean the text
- Return text as string
'''

import pdfplumber
from docx import Document
from fastapi import UploadFile, File, HTTPException
from app.utils.text_cleaner import text_cleaner

def text_extracter(UserFile):

    # Checking if it's PDF or DOCX file
    text= ""
    if UserFile.filename.split(".")[-1]  == "pdf":
        with pdfplumber.open(UserFile.file) as pdf:
            for page in pdf.pages:
                text+= page.extract_text()
    elif UserFile.filename.split(".")[-1]  == "docx":
        doc= Document(UserFile.file)
        for paragraph in doc.paragraphs:
            text+= paragraph.text
    else:
        # If uploaded file is other than PDF or DOCX
        raise HTTPException(
            status_code=415,
            detail="Unsupported file format. Only PDF and DOCX files are allowed."
        )

    # Removing punctuations, lowercase and returning text 
    return text_cleaner(text)