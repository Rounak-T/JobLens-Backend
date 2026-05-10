import requests
import os
from dotenv import load_dotenv
from app.utils.role_mapper import role_to_jobs
from app.utils.similarity import cosine_cal

load_dotenv()

api_key = os.getenv("JSEARCH_API_KEY")

headers = {
    "X-RapidAPI-Key": api_key,
    "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
}

def recommend_job(resume_text, predicted_role):

    relevant_jobs= role_to_jobs[predicted_role]
    seen_url= set()
    all_jobs= []

    for job_title in relevant_jobs:

        params = {
            "query": job_title,
            "num_pages": 1,
            "page": 1
        }
        response = requests.get(
            "https://jsearch.p.rapidapi.com/search",
            headers=headers,
            params=params
        )

        data= response.json()['data']

        for job in data:
            if job['job_apply_link'] not in seen_url:
                seen_url.add(job['job_apply_link']) 
                all_jobs.append(job)

    ranked_jobs = []
    for job in all_jobs:
        score= cosine_cal(resume_text, job['job_description'])

        temp= {
            'title': job['job_title'],
            'description': job['job_description'],
            'location': job['job_location'],
            'apply_link': job['job_apply_link'],
            'match_score': score
        }

        ranked_jobs.append(temp)

    ranked_jobs= sorted(ranked_jobs, key=lambda x: x['match_score'], reverse=True)  

    return ranked_jobs[:5]