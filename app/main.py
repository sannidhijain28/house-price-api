from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load the model (make sure the file exists!)
model = joblib.load("app/house_model.joblib")

# Define expected input structure
class HouseInput(BaseModel):
    bedrooms: int
    bathrooms: float
    sqft_living: int
    floors: float
    zipcode: int

# Create FastAPI app
app = FastAPI()

# Predict endpoint
@app.post("/predict")
def predict_price(house: HouseInput):
    try:
        input_data = np.array([[house.bedrooms, house.bathrooms, house.sqft_living, house.floors, house.zipcode]])
        prediction = model.predict(input_data)
        return {"predicted_price": round(float(prediction[0]), 2)}
    except Exception as e:
        return {"error": str(e)}
