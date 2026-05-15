# import spacy
# from spacy.matcher import PhraseMatcher
# from skillNer.general_params import SKILL_DB
# from skillNer.skill_extractor_class import SkillExtractor

# nlp = spacy.load("en_core_web_lg")
# skill_extractor = SkillExtractor(nlp, SKILL_DB, PhraseMatcher)

# def extract_skills(text):

#     annotations = skill_extractor.annotate(text)
#     skills = list(set(
#     item['doc_node_value'].lower().strip()
#     for item in annotations['results']['ngram_scored']
# ))

#     return skills

# def skill_gap(resume_text, jd_text):

#     resume_skills= set(extract_skills(resume_text))
#     jd_skills= set(extract_skills(jd_text))
#     missing_skills= jd_skills - resume_skills
#     matched_skills = jd_skills & resume_skills

#     return {
#         "matched_skills": list(matched_skills),
#         "missing_skills": list(missing_skills)
#     }

import spacy
from spacy.matcher import PhraseMatcher
from skillNer.general_params import SKILL_DB
from skillNer.skill_extractor_class import SkillExtractor

nlp = None
skill_extractor = None

def load_extractor():
    global nlp, skill_extractor
    if nlp is None:
        nlp = spacy.load("en_core_web_lg")
        skill_extractor = SkillExtractor(nlp, SKILL_DB, PhraseMatcher)

def extract_skills(text):
    load_extractor()
    annotations = skill_extractor.annotate(text)
    skills = list(set(
        item['doc_node_value'].lower().strip()
        for item in annotations['results']['ngram_scored']
    ))
    return skills

def skill_gap(resume_text, jd_text):
    resume_skills = set(extract_skills(resume_text))
    jd_skills = set(extract_skills(jd_text))
    missing_skills = jd_skills - resume_skills
    matched_skills = jd_skills & resume_skills
    return {
        "matched_skills": list(matched_skills),
        "missing_skills": list(missing_skills)
    }