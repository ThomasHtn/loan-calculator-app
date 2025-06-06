from fastapi import FastAPI
from pydantic import BaseModel
from loguru import logger
import joblib
import pandas as pd
from typing import Dict

app = FastAPI()

# Init logger Loguru
logger.add("logs.txt", rotation="1 MB", retention="10 days", level="INFO", backtrace=True, diagnose=True)

# Load model and preprocessor
model = joblib.load("model.pkl")
preprocessor = joblib.load("preprocessor.pkl")

# Entry data schema
class InputData(BaseModel):
    age: float
    taille: float
    poids: float
    sexe: str
    sport_licence: str
    niveau_etude: str
    region: str
    smoker: str
    nationalité_francaise: str
    revenu_estime_mois: float

@app.post("/predict")
def predict(data: InputData) -> Dict[str, float]:
    logger.info("Route : '/predict' (POST) has been called.")

    try:
        # Preprocess data to use it in model
        input_dict = data.dict()
        input_df = pd.DataFrame([input_dict])
        X = preprocessor.transform(input_df)

        # predic value from given data
        prediction = model.predict(X)[0]

        logger.info(f"Prediction request | Input: {input_dict} | Prediction: {prediction}")
        return {"prediction": float(prediction)}
    
    except Exception as e:
        logger.exception("Prediction failed")
        return {"error": "Prediction failed", "detail": str(e)}

@app.get("/health")
def health_check():
    logger.info("Route : '/health' (GET) has been called.")
    try:
        # Init default value
        dummy = pd.DataFrame([{
            "age": 30,
            "taille": 170.0,
            "poids": 65.0,
            "sexe": "H",
            "sport_licence": "non",
            "niveau_etude": "bac",
            "region": "Île-de-France",
            "smoker": "non",
            "nationalité_francaise": "oui",
            "revenu_estime_mois": 3000
        }])

        # Transform value to check preprocessor
        preprocessor.transform(dummy)

        logger.success("Health check success")
        return {"status": "ok", "message": "API in good health"}
    
    except Exception as e:
        logger.exception("Health check failed")
        return {"status": "error", "message": "Health error", "detail": str(e)}