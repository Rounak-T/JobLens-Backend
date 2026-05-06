import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

df= pd.read_csv("data/cleaned_resumes.csv")
vectorizer= TfidfVectorizer(max_features= 8000)

tfidf_matrix= vectorizer.fit_transform(df['Resume_str'])

np.save('data/tfidf_matrix.npy', tfidf_matrix.toarray())
df['Category'].to_csv('data/CategoryLabels.csv', index=False)

with open('data/tfidf_vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)