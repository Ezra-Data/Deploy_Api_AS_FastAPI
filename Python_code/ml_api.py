# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 12:47:00 2026

@author: DELL
"""


from fastapi import FastAPI
from pydantic import BaseModel
import pickle

app = FastAPI()


# Define the input data
class model_input(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int


# Load the saved model
diabetes_model = pickle.load(
    open('diabetes_model.sav', 'rb')
)


# Create the prediction endpoint
@app.post('/diabetes_prediction')
def diabetes_pred(input_parameters: model_input):

    # Extract the input values
    preg = input_parameters.Pregnancies
    glu = input_parameters.Glucose
    bp = input_parameters.BloodPressure
    skin = input_parameters.SkinThickness
    insulin = input_parameters.Insulin
    bmi = input_parameters.BMI
    dpf = input_parameters.DiabetesPedigreeFunction
    age = input_parameters.Age

    # Create input list in the same order
    # used during model training
    input_list = [
        preg,
        glu,
        bp,
        skin,
        insulin,
        bmi,
        dpf,
        age
    ]

    # Make prediction
    prediction = diabetes_model.predict([input_list])

    # Return result
    if prediction[0] == 0:
        return 'The person is not Diabetic'
    else:
        return 'The person is diabetic'

