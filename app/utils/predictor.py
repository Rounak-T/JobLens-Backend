import pickle

with open('data/svm_model.pkl', 'rb')as f:
    svm_model= pickle.load(f)

with open('data/Categories_encoder.pkl', 'rb')as f:
    encoder= pickle.load(f)

with open('data/tfidf_vectorizer.pkl', 'rb') as f:
    vectorizer= pickle.load(f)

def predict_role(resume_text):

    resume_vector= vectorizer.transform([resume_text])
    prediction= svm_model.predict(resume_vector)
    pred_label= str(encoder.inverse_transform(prediction)[0])

    return pred_label
