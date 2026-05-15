import os
import pickle
import numpy as np
import pandas as pd
from sklearn.svm import LinearSVC
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from app.utils.tfidf_vectorizer import train_tfidf

# Create folders if they don't exist
os.makedirs('app/models', exist_ok=True)
os.makedirs('data', exist_ok=True)

def train_models():
    print("Training TF-IDF...")
    train_tfidf()

    print("Loading TF-IDF matrix and categories...")
    tfidf_matrix = np.load('app/models/tfidf_matrix.npy')
    categories_df = pd.read_csv('data/CategoryLabels.csv')

    print("Encoding labels...")
    encoder = LabelEncoder()
    categories_transformed = encoder.fit_transform(categories_df['Category'])
    with open('app/models/label_encoder.pkl', 'wb') as f:
        pickle.dump(encoder, f)
    print("Label encoder saved!")

    X = tfidf_matrix.copy()
    y = categories_transformed.copy()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

    print("Training SVM...")
    model_svm = LinearSVC()
    model_svm.fit(X_train, y_train)
    y_pred = model_svm.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"SVM Accuracy: {acc}")
    with open('app/models/svm_model.pkl', 'wb') as f:
        pickle.dump(model_svm, f)
    print("All models trained and saved!")

if __name__ == "__main__":
    train_models()