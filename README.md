🏡 House Price Predictor API
This project is a production-ready machine learning API that predicts house prices based on features like bedrooms, bathrooms, square footage, and zipcode.

Built with:

🚀 FastAPI for serving the model

🧠 scikit-learn for training

🐳 Docker for containerization

💾 joblib for model persistence

🔬 Optional: GitHub Actions + Streamlit + Hugging Face

📦 Features
/predict endpoint to serve predictions

Trained on the King County House Sales dataset

Fully containerized via Docker

Ready for CI/CD and cloud deployment

🚀 How to Run the Project
✅ Local (Python only)
bash
Copy
Edit
# Step into project
cd house-price-api

# Activate your environment, then run:
uvicorn app.main:app --reload
Visit: http://localhost:8000/docs

🐳 Dockerized (recommended)
bash
Copy
Edit
# Build the Docker image
docker build -t house-price-api .

# Run the container
docker run -p 8000:8000 house-price-api
🔍 API Endpoint
POST /predict
Predicts house price using the trained model.

🔸 Sample JSON Input
json
Copy
Edit
{
  "bedrooms": 3,
  "bathrooms": 2.5,
  "sqft_living": 1800,
  "floors": 1.0,
  "zipcode": 98103
}

