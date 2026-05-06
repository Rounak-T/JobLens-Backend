from fastapi import FastAPI, UploadFile, File
from app.utils.resume_parser import text_extracter
from fastapi.responses import JSONResponse

app= FastAPI()

@app.get("/")
def test():
    return {"message": "The app is running"}

@app.post("/upload")
def TextExtracter(UserFile: UploadFile= File(...)):

    text= text_extracter(UserFile)
    return JSONResponse(status_code=200, content={"text": text})