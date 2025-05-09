import pandas as pd
import pickle

def load_cancer_data():
    data = pd.read_csv('../Data Sets/cancer/cancer_dataset.csv')
    return data

def predict_cancer_symptoms(symptoms, model_path='../general_disease/models/svc.pkl'):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    prediction = model.predict([symptoms])
    return prediction[0]


def get_cancer_medications(disease):
    medications_df = pd.read_csv('../Data Sets/cancer/cancer_medication.csv')
    meds = medications_df[medications_df['disease'] == disease]['medications'].tolist()
    return meds if meds else ['No medication found for this disease']
