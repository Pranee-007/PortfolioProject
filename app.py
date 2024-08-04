import streamlit as st
import pandas as pd
import numpy as np
import joblib
import sklearn

with open('optimized_rf_model.pkl', 'rb') as model_file:
    model = joblib.load(model_file)

st.title('Insurance Premium Estimator')

age = st.slider('Age', 18, 66)
weight = st.slider('Weight (kg)', 51, 132)
height = st.slider('Height (cm)', 145, 188)
bmi = weight / ((height/100)**2)  # Calculate BMI
diabetes = st.selectbox('Diabetes', ['No', 'Yes'])
blood_pressure = st.selectbox('Blood Pressure Problems', ['No', 'Yes'])
transplants = st.selectbox('Any Transplants', ['No', 'Yes'])
chronic_diseases = st.selectbox('Any Chronic Diseases', ['No', 'Yes'])
allergies = st.selectbox('Known Allergies', ['No', 'Yes'])
cancer_history = st.selectbox('History of Cancer in Family', ['No', 'Yes'])
surgeries = st.slider('Number of Major Surgeries', 0, 3)

input_data = pd.DataFrame({
    'Age': [age],
    'Weight': [weight],
    'Height': [height],
    'BMI': [bmi],
    'Diabetes': [1 if diabetes == 'Yes' else 0],
    'BloodPressureProblems': [1 if blood_pressure == 'Yes' else 0],
    'AnyTransplants': [1 if transplants == 'Yes' else 0],
    'AnyChronicDiseases': [1 if chronic_diseases == 'Yes' else 0],
    'KnownAllergies': [1 if allergies == 'Yes' else 0],
    'HistoryOfCancerInFamily': [1 if cancer_history == 'Yes' else 0],
    'NumberOfMajorSurgeries': [surgeries]
})

if st.button('Estimate Premium'):
    try:
        prediction = model.predict(input_data)
        st.write(f'Estimated Premium: ₹{prediction[0]:.2f}')  # Format with currency
    except Exception as e:
        st.error(f'An error occurred: {e}')