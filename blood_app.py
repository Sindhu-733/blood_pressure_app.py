# app.py
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("bp_model.pkl")

st.title("Blood Pressure Prediction App")

# Collect user input
age = st.number_input("Age", min_value=1, max_value=100)
weight = st.number_input("Weight (kg)")
height = st.number_input("Height (cm)")
cholesterol = st.selectbox("Cholesterol", options=[1, 2, 3])
glucose = st.selectbox("Glucose", options=[1, 2, 3])

# Make prediction
if st.button("Predict"):
    input_data = pd.DataFrame([[age, weight, height, cholesterol, glucose]],
                              columns=["age", "weight", "height", "cholesterol", "glucose"])
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Blood Pressure: {prediction:.2f}")
