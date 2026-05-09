from sklearn.metrics.pairwise import cosine_similarity
import pickle

with open('data/tfidf_vectorizer.pkl', 'rb') as f:
    vectorizer= pickle.load(f)

def cosine_cal(resume_text, jd_text):

    resume_vector= vectorizer.transform([resume_text])
    jd_vector= vectorizer.transform([jd_text])

    score = cosine_similarity(resume_vector, jd_vector)

    return round(float(score[0][0]) * 100, 2)

# import os

# print(os.getcwd())
# print(os.listdir())