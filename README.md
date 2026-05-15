# JobLens (Backend)

> Your resume, through a smarter lens.

JobLens is an NLP + Machine Learning system that analyzes your resume against a job description, predicts your most suitable job role, identifies skill gaps, and recommends live job listings.

Frontend repo: [JobLens-UI](https://github.com/Rounak-T/JobLens-UI)

---

## Features

- **Resume Parsing** — Supports PDF and DOCX formats
- **Match Score** — Cosine similarity between your resume and a job description
- **Skill Gap Analysis** — Identifies matched and missing skills using spaCy and skillNer
- **Role Prediction** — Predicts your job role using a trained SVM model
- **Live Job Recommendations** — Fetches real job listings via JSearch API, ranked by relevance

---

## Tech Stack

- **Backend:** FastAPI + Uvicorn
- **ML:** scikit-learn (TF-IDF, LinearSVC, Cosine Similarity)
- **NLP:** spaCy (en_core_web_lg) + skillNer
- **PDF Parsing:** pdfplumber, python-docx
- **Job API:** JSearch via RapidAPI
- **Environment:** python-dotenv

---

## Project Structure

```
JobLens-Backend/
├── app/
│   ├── main.py                  # FastAPI app, endpoints
│   ├── models/                  # Generated model files (gitignored)
│   └── utils/
│       ├── resume_parser.py     # PDF/DOCX text extraction
│       ├── text_cleaner.py      # Text preprocessing
│       ├── tfidf_vectorizer.py  # TF-IDF training
│       ├── similarity.py        # Cosine similarity scoring
│       ├── skill_extractor.py   # Skill extraction + gap analysis
│       ├── predictor.py         # SVM role prediction
│       ├── job_recommender.py   # Live job fetching + ranking
│       └── role_mapper.py       # Maps predicted roles to job titles
├── data/
│   └── Resume.csv               # Kaggle resume dataset
├── train_model.py               # Generates all model files
├── eda.ipynb                    # Exploratory data analysis
├── ann_model.ipynb              # Model experimentation notebook
├── requirements.txt
└── .env                         # API keys (not committed)
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| POST | `/resume-analysis` | Returns match score, matched skills, missing skills |
| POST | `/predict-role` | Returns predicted role and live job recommendations |

---

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/Rounak-T/JobLens-Backend.git
cd JobLens-Backend
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_lg
```

### 4. Set up environment variables

Create a `.env` file in the root:

```
JSEARCH_API_KEY=your_rapidapi_key_here
```

Get your free API key at [RapidAPI JSearch](https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch)

### 5. Generate model files

```bash
python train_model.py
```

This generates all `.pkl` and `.npy` files inside `app/models/`.

### 6. Run the server

```bash
uvicorn app.main:app --reload
```

Visit `http://127.0.0.1:8000/docs` to test the API.

---

## ML Models

| Model | Accuracy | Notes |
|-------|----------|-------|
| LinearSVC (SVM) | ~70% | Primary classifier, works well on sparse TF-IDF vectors |
| ANN (experimental) | ~65% | Experimented with, not used in production |

Dataset: [Kaggle Resume Dataset](https://www.kaggle.com/datasets/gauravduttakiit/resume-dataset) — 2484 resumes across 24 job categories.

---

## Known Limitations

- TF-IDF misses semantic similarity — "tax return filing" and "taxation" won't match
- Only 24 job categories — edge cases like AI/DS may get misclassified
- Match scores tend to be low (25–40%) due to keyword mismatch between resumes and JDs
- Job listings are fetched live and may vary

---

## Author

**Rounak T** — 3rd Year AI & Data Science Student, Savitribai Phule Pune University
