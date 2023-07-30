# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 22:09:21 2023

@author: Sumanta
"""
import pickle
import streamlit as st
#from streamlit_option_menu import option_menu


# loading the saved model
diabetes_model = pickle.load(open('C:/Users/Sumanta/Desktop/DiabetesPredictionSystem/saved model/diabetes_model.sav','rb'))

# page title
st.title('Diabetes Prediction using Machine Learning')


# getting the input data from the user
col1, col2, col3 = st.columns(3)

with col1:
    Pregnancies = st.text_input('Number of Pregnancies')
    
with col2:
    Glucose = st.text_input('Glucose Level')

with col3:
    BloodPressure = st.text_input('Blood Pressure value')

with col1:
    SkinThickness = st.text_input('Skin Thickness value')

with col2:
    Insulin = st.text_input('Insulin Level')

with col3:
    BMI = st.text_input('BMI value')

with col1:
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

with col2:
    Age = st.text_input('Age of the Person')


# code for Prediction
diab_diagnosis = ''

# creating a button for Prediction

if st.button('Diabetes Test Result'):
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    
    if (diab_prediction[0] == 1):
      diab_diagnosis = 'Diabetic Positive'
    else:
      diab_diagnosis = 'Diabetic Negetive'
    
st.success(diab_diagnosis)
