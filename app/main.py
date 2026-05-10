from fastapi import FastAPI, UploadFile, File, Form
from app.utils.resume_parser import text_extracter
from app.utils.text_cleaner import text_cleaner
from app.utils.similarity import cosine_cal
from app.utils.skill_extractor import skill_gap
from app.utils.predictor import predict_role
from app.utils.job_recommender import recommend_job
from fastapi.responses import JSONResponse

app= FastAPI()

@app.get("/")
def test():
    return {"message": "The app is running"}

@app.post("/resume-analysis")
def ResumeAnalysis(UserFile: UploadFile= File(...), raw_jd_text: str = Form(...)):

    resume_text= text_extracter(UserFile)

    resume_text= text_cleaner(resume_text)
    jd_text= text_cleaner(raw_jd_text)

    skills= skill_gap(resume_text, jd_text)
    missing_skills= skills['missing_skills']
    matched_skills= skills['matched_skills']
    match_score= cosine_cal(resume_text, jd_text)

    return JSONResponse(status_code=200, content={"match_score": match_score, 'missing_skills': missing_skills, 'matched_skills': matched_skills})

@app.post("/predict-role")
def PredictRole(UserFile: UploadFile= File(...)):
    resume_text= text_extracter(UserFile)
    resume_text= text_cleaner(resume_text)

    prediction= predict_role(resume_text)

    jobs= recommend_job(resume_text, prediction)

    return JSONResponse(status_code=200, content={'predicted_role': prediction, 'jobs': jobs})

