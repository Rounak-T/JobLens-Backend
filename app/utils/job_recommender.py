import requests
import os
from dotenv import load_dotenv
from app.utils.role_mapper import role_to_jobs
from app.utils.similarity import cosine_cal
from concurrent.futures import ThreadPoolExecutor

load_dotenv()

api_key = os.getenv("JSEARCH_API_KEY")

def fetch_jobs(job_title):

    headers = {
    "X-RapidAPI-Key": api_key,
    "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }
    params = {
            "query": job_title + " in India",
            "num_pages": 1,
            "page": 1
    }
    response = requests.get(
            "https://jsearch.p.rapidapi.com/search",
            headers=headers,
            params=params
    )
    data= response.json()['data']

    return data

def recommend_job(resume_text, predicted_role):

    relevant_jobs= role_to_jobs[predicted_role]
    seen_url= set()
    all_jobs= []

    with ThreadPoolExecutor() as executor:
        data= list(executor.map(fetch_jobs, relevant_jobs))

    data = [item for sublist in data for item in sublist]

    for job in data:
        if job['job_apply_link'] not in seen_url:
            seen_url.add(job['job_apply_link']) 
            all_jobs.append(job)

    ranked_jobs = []
    for job in all_jobs:
        score= cosine_cal(resume_text, job['job_description'])

        temp= {
            'title': job['job_title'],
            'match_score': score,
            'apply_link': job['job_apply_link']
        }

        ranked_jobs.append(temp)

    ranked_jobs= sorted(ranked_jobs, key=lambda x: x['match_score'], reverse=True)  

    return ranked_jobs[:5]