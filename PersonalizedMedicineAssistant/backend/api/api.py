from fastapi import FastAPI
from general_disease.main import router as general_disease_router
from cancer_module.main import router as cancer_router
from chatbot.main import router as chatbot_router
from hospital_locator.main import router as hospital_router

app = FastAPI()

# Include different routers
app.include_router(general_disease_router, prefix="/general")
app.include_router(cancer_router, prefix="/cancer")
app.include_router(chatbot_router, prefix="/chatbot")
app.include_router(hospital_router, prefix="/hospital")

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Personalized Medicine Assistant API is running!"}
