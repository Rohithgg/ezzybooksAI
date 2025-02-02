import docx
from fastapi import FastAPI, File, UploadFile, HTTPException, Form
import pdfplumber
# import docx
import ollama
import os
from ollama import ChatResponse
from ollama import chat
app = FastAPI()

def extract_pdf_book(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text.strip()

def extract_docx_book(docx_file):
    doc = docx.opendocx(docx_file)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text
    return text.strip()

@app.post("/summarize")
def summarize(file: UploadFile(...)):
    try:
        if file.content_type == "application/pdf" and file.filename.endswith(".pdf"):
            return extract_pdf_book(file.file)
        elif file.content_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document" and file.endswith(".docx"):
            return extract_docx_book(file.file)
        else:
            raise HTTPException(status_code=400, detail="Unsupported file type")

    #response
        response: ChatResponse = chat(model="qwen2",
                                  context="for the given pdf or docx you have to summarise and convey it to the user in simple and manageable chucks",
                                  messages=[
                                      {
                                
                                          "role": "user",
                                          "content": input("You: ")
                                      }
                                  ])
        summery = (response["messages"]["content"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    print(summery)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=11434)
