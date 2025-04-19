# app/model/predictor.py

import joblib
import os
import numpy as np

# Load the saved model and encoder
MODEL_PATH = os.path.join("models", "aws_recommender_model.joblib")
ENCODER_PATH = os.path.join("models", "encoder.joblib")

model = joblib.load(MODEL_PATH)
encoder = joblib.load(ENCODER_PATH)

def predict_instance(workload_type: str, traffic_level: str, budget: str):
    # Format input
    input_data = [[workload_type, traffic_level, budget]]

    # Encode the input
    try:
        input_encoded = encoder.transform(input_data).toarray()
    except Exception as e:
        return None, str(e)  # Return error message if encoding fails

    # Predict
    prediction = model.predict(input_encoded)[0]
    return prediction, None
