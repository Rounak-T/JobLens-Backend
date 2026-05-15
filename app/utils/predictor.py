# import pickle

# with open('app/models/svm_model.pkl', 'rb')as f:
#     svm_model= pickle.load(f)

# with open('app/models/label_encoder.pkl', 'rb')as f:
#     encoder= pickle.load(f)

# with open('app/models/tfidf_vectorizer.pkl', 'rb') as f:
#     vectorizer= pickle.load(f)

# def predict_role(resume_text):

#     resume_vector= vectorizer.transform([resume_text])
#     prediction= svm_model.predict(resume_vector)
#     pred_label= str(encoder.inverse_transform(prediction)[0])

#     return pred_label


import pickle

svm_model = None
encoder = None
vectorizer = None

def load_models():
    global svm_model, encoder, vectorizer
    if svm_model is None:
        with open('app/models/svm_model.pkl', 'rb') as f:
            svm_model = pickle.load(f)
        with open('app/models/label_encoder.pkl', 'rb') as f:
            encoder = pickle.load(f)
        with open('app/models/tfidf_vectorizer.pkl', 'rb') as f:
            vectorizer = pickle.load(f)

def predict_role(resume_text):
    load_models()
    resume_vector = vectorizer.transform([resume_text])
    prediction = svm_model.predict(resume_vector)
    pred_label = str(encoder.inverse_transform(prediction)[0])
    return pred_label