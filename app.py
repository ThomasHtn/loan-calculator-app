import streamlit as st
import requests

API_URL = 'http://localhost:9500/'

if st.sidebar.button("Check api health"):
    try:
        response = requests.get(API_URL+"/health")
        if response.status_code == 200 and response.json().get("status") == "ok":
            st.sidebar.success("✅ API in good health")
        else:
            st.sidebar.error(f"⚠️ API error: {response.json()}")
    except Exception as e:
        st.sidebar.error(f"❌ Cannot call API\n{e}")

st.title("📊 Predict loan amount")

with st.form("prediction_form"):
    age = st.number_input("Âge", 18, 100, 30)
    taille = st.number_input("Taille (cm)", 100.0, 250.0, 170.0)
    poids = st.number_input("Poids (kg)", 30.0, 200.0, 70.0)
    sexe = st.selectbox("Sexe", ["H", "F"])
    sport_licence = st.selectbox("Licence Sportive", ["oui", "non"])
    niveau_etude = st.selectbox("Niveau d'étude", ["aucun", "bac", "bac+2", "master", "doctorat"])
    region = st.selectbox("Région", ["Île-de-France", "Corse", "Autre"])
    smoker = st.selectbox("Fumeur", ["oui", "non"])
    nationalité_francaise = st.selectbox("Nationalité française", ["oui", "non"])
    revenu = st.number_input("Revenu estimé / mois (€)", 0.0, 20000.0, 3000.0)

    submitted = st.form_submit_button("Predic loan amount")

    if submitted:
        input_data = {
            "age": age,
            "taille": taille,
            "poids": poids,
            "sexe": sexe,
            "sport_licence": sport_licence,
            "niveau_etude": niveau_etude,
            "region": region,
            "smoker": smoker,
            "nationalité_francaise": nationalité_francaise,
            "revenu_estime_mois": revenu,
        }

        response = requests.post(API_URL+"/predict", json=input_data)

        if response.status_code == 200:
            prediction = response.json()["prediction"]
            st.success(f"💰 Predict loan amount : {prediction:.2f} €")
        else:
            st.error("Prediction error.")