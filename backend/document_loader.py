import os
from PyPDF2 import PdfReader

def load_documents(folder_path):
    docs = []
    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            reader = PdfReader(os.path.join(folder_path, file))
            text = ""
            for i, page in enumerate(reader.pages):
                text += f"\n[Page {i+1}] " + page.extract_text()
            docs.append({
                "document": file,
                "content": text
            })
    return docs
