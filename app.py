import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('model.sav')

st.title("Sales Prediction App")
st.write("Enter your advertising budget to predict Sales (in thousands of units).")

# User inputs
tv = st.number_input("TV Advertising Budget ($k)", min_value=0.0, value=150.0, step=1.0)
radio = st.number_input("Radio Advertising Budget ($k)", min_value=0.0, value=25.0, step=1.0)
newspaper = st.number_input("Newspaper Advertising Budget ($k)", min_value=0.0, value=10.0, step=1.0)

if st.button("Predict Sales"):
    # Create a DataFrame for predictions matching training format
    input_data = pd.DataFrame({
        'TV': [tv],
        'Radio': [radio],
        'Newspaper': [newspaper]
    })
    
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Sales: {prediction:.2f} thousand units")
