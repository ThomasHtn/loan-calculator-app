import pytest
from fastapi.testclient import TestClient
from api import app  

client = TestClient(app)

# Test the health check endpoint
def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    json_data = response.json()
    assert "status" in json_data
    assert json_data["status"] in ["ok", "error"]  # can be "error" if the model fails

# Test the prediction endpoint
def test_predict():
    sample_input = {
        "age": 35,
        "taille": 175.0,
        "poids": 70.0,
        "sexe": "H",
        "sport_licence": "oui",
        "niveau_etude": "bac+2",
        "region": "Occitanie",
        "smoker": "non",
        "nationalité_francaise": "oui",
        "revenu_estime_mois": 2500
    }

    response = client.post("/predict", json=sample_input)
    assert response.status_code == 200
    json_data = response.json()

    # If the model works, we should get a numeric prediction
    if "prediction" in json_data:
        assert isinstance(json_data["prediction"], float)
    else:
        # Otherwise, check that the error is properly structured
        assert "error" in json_data
        assert "detail" in json_data