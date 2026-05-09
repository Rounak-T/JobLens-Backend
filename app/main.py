from fastapi import FastAPI, UploadFile, File, Form
from app.utils.resume_parser import text_extracter
from app.utils.text_cleaner import text_cleaner
from app.utils.similarity import cosine_cal
from fastapi.responses import JSONResponse

app= FastAPI()

@app.get("/")
def test():
    return {"message": "The app is running"}

# @app.post("/upload")
# def TextExtracter(UserFile: UploadFile= File(...)):

#     text= text_extracter(UserFile)
#     text= text_cleaner(text)
#     return JSONResponse(status_code=200, content={"text": text})

@app.post("/match-score")
def MatchScore(UserFile: UploadFile= File(...), raw_jd_text: str = Form(...)):

    resume_text= text_extracter(UserFile)
    resume_text= text_cleaner(resume_text)

    jd_text= text_cleaner(raw_jd_text)

    match_score= cosine_cal(resume_text, jd_text)

    return match_score