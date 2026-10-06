# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 13:26:08 2026

@author: DELL
"""



import requests


url = 'https://drinkable-kilometer-identity.ngrok-free.dev/diabetes_prediction'


input_data_for_model = {
    'Pregnancies': 1,
    'Glucose': 85,
    'BloodPressure': 66,
    'SkinThickness': 29,
    'Insulin': 0,
    'BMI': 26.6,
    'DiabetesPedigreeFunction': 0.351,
    'Age': 31
}


response = requests.post(
    url,
    json=input_data_for_model
)


print(response.status_code)
print(response.text)



    