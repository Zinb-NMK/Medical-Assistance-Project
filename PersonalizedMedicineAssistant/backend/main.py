import os
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load Dataset
dataset = pd.read_csv("Data Sets/Training.csv")

# Remove Duplicate Rows
dataset.drop_duplicates(inplace=True)
print(f"Duplicate rows removed: {4616}")

# Encoding target variable
le = LabelEncoder()
dataset["prognosis"] = le.fit_transform(dataset["prognosis"])

# Splitting Data
x = dataset.drop("prognosis", axis=1)
y = dataset["prognosis"]

# Train Random Forest Model
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42, stratify=y)

rf = RandomForestClassifier(n_estimators=200, random_state=42)
rf.fit(x_train, y_train)

# Evaluate Model
y_pred = rf.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Random Forest Accuracy: {accuracy * 100:.2f}%")

# Cross-validation
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
cross_val_acc = np.mean(cross_val_score(rf, x, y, cv=skf))
print(f"Cross-validation Accuracy: {cross_val_acc * 100:.2f}%")

# Save Model
model_path = "models/svc.pkl"
os.makedirs("models", exist_ok=True)
pickle.dump(rf, open(model_path, 'wb'))

# Load Additional Data
sym_des = pd.read_csv("Data Sets/symptoms_df.csv")
precautions = pd.read_csv("Data Sets/precautions_df.csv")
workout = pd.read_csv("Data Sets/workout_df.csv")
description = pd.read_csv("Data Sets/description.csv")
medications = pd.read_csv("Data Sets/medications.csv")
diets = pd.read_csv("Data Sets/diets.csv")

# Symptoms and Disease Mappings
symptoms_dict = {symptom: idx for idx, symptom in enumerate(x.columns)}
diseases_list = dict(enumerate(le.classes_))


# Helper Function
def get_recommendations(disease):
    desc = description[description['Disease'] == disease]['Description'].values
    pre = precautions[precautions['Disease'] == disease][
        ['Precaution_1', 'Precaution_2', 'Precaution_3', 'Precaution_4']].values
    meds = medications[medications['Disease'] == disease]['Medication'].values
    diet = diets[diets['Disease'] == disease]['Diet'].values
    work = workout[workout['disease'] == disease]['workout'].values
    return desc, pre, meds, diet, work


# Prediction Function (Returning Top 5 Diseases)
def predict_diseases(patient_symptoms, top_n=5):
    input_vector = np.zeros(len(symptoms_dict))

    for symptom in patient_symptoms:
        if symptom in symptoms_dict:
            input_vector[symptoms_dict[symptom]] = 1
        else:
            print(f"Warning: '{symptom}' is not recognized.")

    input_df = pd.DataFrame([input_vector], columns=x.columns)
    probabilities = rf.predict_proba(input_df)[0]  # Get prediction probabilities
    top_disease_indices = np.argsort(probabilities)[-top_n:][::-1]  # Get top N diseases

    return [(diseases_list[idx], probabilities[idx]) for idx in top_disease_indices]


# User Input
symptoms = input("Enter your symptoms separated by commas: ")
user_symptoms = [s.strip() for s in symptoms.split(',') if s.strip() in symptoms_dict]

if not user_symptoms:
    print("No valid symptoms entered. Please try again.")
else:
    predicted_diseases = predict_diseases(user_symptoms, top_n=5)

    for rank, (disease, probability) in enumerate(predicted_diseases, 1):
        desc, pre, meds, diet, work = get_recommendations(disease)

        print(f"\n========= Possible Disease {rank}: {disease} (Confidence: {probability * 100:.2f}%) =========")
        print("========= Description:=========\n", desc[0] if len(desc) > 0 else "No description available.")

        print("========= Precautions: =========")
        if len(pre) > 0:
            for i, p in enumerate(pre[0], 1):
                print(f"{i} : {p}")
        else:
            print("No precautions available.")

        print("========= Medications: =========")
        if len(meds) > 0:
            for i, m in enumerate(meds, 1):
                print(f"{i} : {m}")
        else:
            print("No medications available.")

        print("========= Workout: =========")
        if len(work) > 0:
            for i, w in enumerate(work, 1):
                print(f"{i} : {w}")
        else:
            print("No workout recommendations available.")

        print("========= Diets: =========")
        if len(diet) > 0:
            for i, d in enumerate(diet, 1):
                print(f"{i} : {d}")
        else:
            print("No diet recommendations available.")
