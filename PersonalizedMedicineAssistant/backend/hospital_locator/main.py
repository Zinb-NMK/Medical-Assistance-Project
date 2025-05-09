import requests

def find_nearby_hospitals(location, api_key):
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius=5000&type=hospital&key={api_key}"
    response = requests.get(url)
    data = response.json()
    hospitals = [place['name'] for place in data.get('results', [])]
    return hospitals


### api/api.py
from fastapi import FastAPI, HTTPException
from general_disease.main import predict_disease
from cancer_module.main import predict_cancer_symptoms, get_cancer_medications
from chatbot.main import chatbot_response
from hospital_locator.main import find_nearby_hospitals

app = FastAPI()

@app.get("/predict/general")
def general_disease(symptoms: list):
    try:
        result = predict_disease(symptoms)
        return {"diagnosis": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/predict/cancer")
def cancer_disease(symptoms: list):
    try:
        result = predict_cancer_symptoms(symptoms)
        medications = get_cancer_medications(result)
        return {"diagnosis": result, "medications": medications}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/chatbot")
def chat(user_input: str):
    return {"response": chatbot_response(user_input)}

@app.get("/hospitals")
def hospitals(location: str, api_key: str):
    try:
        hospitals = find_nearby_hospitals(location, api_key)
        return {"hospitals": hospitals}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))