import os
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC

# === Load Dataset ===
dataset_path = r"E:\Final_Project\PersonalizedMedicineAssistant\backend\Data Sets\general\Training.csv"
if not os.path.exists(dataset_path):
    raise FileNotFoundError(f"Dataset not found at {dataset_path}")

dataset = pd.read_csv(dataset_path)

# === Encode Target Variable ===
le = LabelEncoder()
dataset["prognosis"] = le.fit_transform(dataset["prognosis"])

# === Split Data ===
x = dataset.drop("prognosis", axis=1)
y = dataset["prognosis"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=20)

# === Train or Load SVC Model ===
model_dir = os.path.join("backend", "models")
model_path = os.path.join(model_dir, "svc.pkl")

if os.path.exists(model_path):
    svc = pickle.load(open(model_path, 'rb'))
else:
    svc = SVC(kernel='linear', probability=True)  # Enable probabilities
    svc.fit(x_train, y_train)
    os.makedirs(model_dir, exist_ok=True)
    pickle.dump(svc, open(model_path, 'wb'))

# === Load Additional Data ===
def load_csv_file(filename):
    path = os.path.join("backend", "Data Sets", "general", filename)
    try:
        df = pd.read_csv(path)
        df.columns = df.columns.str.strip()  # Remove leading/trailing spaces from column names
        return df
    except FileNotFoundError:
        print(f"Warning: File {filename} not found at {path}. Using an empty DataFrame.")
        return pd.DataFrame()

sym_des = load_csv_file("symptoms_df.csv")
precautions = load_csv_file("precautions_df.csv")
workout = load_csv_file("workout_df.csv")
description = load_csv_file("description.csv")
medications = load_csv_file("medications.csv")
diets = load_csv_file("diets.csv")

# === Symptoms and Disease Mappings ===
symptoms_dict = {symptom.lower(): idx for idx, symptom in enumerate(x.columns)}  # Handle lowercase input
diseases_list = dict(enumerate(le.classes_))

# === Helper Functions ===
def get_recommendations(disease):
    desc = description[description['Disease'] == disease]['Description'].values or ["No description available."]
    pre = precautions[precautions['Disease'] == disease][['Precaution_1', 'Precaution_2', 'Precaution_3', 'Precaution_4']].values or [["No precautions available."]]
    meds = medications[medications['Disease'] == disease]['Medication'].values or ["No medications available."]
    diet = diets[diets['Disease'] == disease]['Diet'].values or ["No diets available."]
    work = workout[workout['disease'] == disease]['workout'].values or ["No workouts available."]
    return desc, pre, meds, diet, work

def display_list(title, items):
    print(f"\n================= {title} ==================")
    if len(items) > 0:
        for i, item in enumerate(items, 1):
            print(f"{i}: {item}")
    else:
        print(f"No {title.lower()} available.")

# === Prediction Function ===
def predict_disease(patient_symptoms):
    input_vector = np.zeros(len(symptoms_dict))
    for symptom in patient_symptoms:
        symptom = symptom.lower()
        if symptom in symptoms_dict:
            input_vector[symptoms_dict[symptom]] = 1
        else:
            print(f"Warning: '{symptom}' is not recognized.")
    input_df = pd.DataFrame([input_vector], columns=x.columns)
    proba = svc.predict_proba(input_df)
    predicted_label = svc.predict(input_df)[0]
    confidence = proba[0][predicted_label]
    return diseases_list.get(predicted_label, "Unknown disease"), confidence

# === User Input ===
symptoms = input("Enter your symptoms separated by commas: ")
user_symptoms = [s.strip().lower() for s in symptoms.split(',') if s.strip().lower() in symptoms_dict]

# === Check for Valid Symptoms ===
unrecognized = [s for s in symptoms.split(',') if s.strip().lower() not in symptoms_dict]
if unrecognized:
    print(f"Warning: These symptoms were not recognized: {', '.join(unrecognized)}")

if not user_symptoms:
    print("No valid symptoms entered. Please try again.")
else:
    predicted_disease, confidence = predict_disease(user_symptoms)
    desc, pre, meds, diet, work = get_recommendations(predicted_disease)

    # === Display Results ===
    print("\n================= Predicted Disease ==================")
    print(f"{predicted_disease} (Confidence: {confidence * 100:.2f}%)")

    print("\n================= Description ==================")
    print(desc[0] if len(desc) > 0 else "No description available.")

    display_list("Precautions", pre[0] if len(pre) > 0 else [])
    display_list("Medications", meds)
    display_list("Workout", work)
    display_list("Diets", diet)
