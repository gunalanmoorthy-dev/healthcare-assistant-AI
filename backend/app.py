from fastapi import FastAPI

app = FastAPI()

@app.get("/symptom-checker")
def symptom_checker():
    return {"message": "Symptom Checker Endpoint"}

@app.get("/medication-info")
def medication_info():
    return {"message": "Medication Info Endpoint"}

@app.get("/health-tips")
def health_tips():
    return {"message": "Health Tips Endpoint"}