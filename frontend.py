import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.title("Insurance Predictor")

age = st.number_input("Age", 1, 119, 25)
weight = st.number_input("Weight", 1.0, 200.0, 60.0)
height = st.number_input("Height", 0.5, 2.5, 1.7)
income = st.number_input("Income (LPA)", 1.0, 100.0, 10.0)
smoker = st.selectbox("Smoker", [True, False])
city = st.text_input("City", "Mumbai")
occupation = st.selectbox("Occupation", [
    'retired','freelancer','student','government_job',
    'business_owner','unemployed','private_job'
])

if st.button("Predict"):
    data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }

    res = requests.post(API_URL, json=data)

    if res.status_code == 200:
        st.success(res.json()["response"]["predicted_category"])
    else:
        st.error(res.text)