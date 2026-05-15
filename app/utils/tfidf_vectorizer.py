import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def train_tfidf():
    df = pd.read_csv("data/cleaned_resumes.csv")
    vectorizer = TfidfVectorizer(max_features=8000)

    tfidf_matrix = vectorizer.fit_transform(df['Resume_str'])

    np.save('app/models/tfidf_matrix.npy', tfidf_matrix.toarray())
    df['Category'].to_csv('data/CategoryLabels.csv', index=False)

    with open('app/models/tfidf_vectorizer.pkl', 'wb') as f:
        pickle.dump(vectorizer, f)

    print("TF-IDF training done!")

if __name__ == "__main__":
    train_tfidf()