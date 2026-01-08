#  Car Price Prediction using Streamlit

A Streamlit web application that predicts used car prices using a trained machine learning regression model.

---

##  Problem Statement
Estimating the correct price of a used car is challenging due to multiple influencing factors such as brand, model, year, fuel type, and kilometers driven.  
This project uses machine learning to predict a fair market price for used cars.

---

##  Features
- Interactive Streamlit web interface
- Company and model selection
- Fuel type and year input
- Kilometers driven input
- Real-time car price prediction

---

##  Tech Stack
- Python
- pandas
- NumPy
- scikit-learn
- Streamlit
- joblib

---

## Machine Learning Model
- Regression-based ML model
- Trained on cleaned used car dataset
- Categorical features encoded during training
- Model saved using `joblib`

---

## 📁 Project Structure
```
car-price-prediction-ml/
│
├── app.py # Main Streamlit application
├── car_price_model.joblib # Trained ML model
├── Cleaned Car.csv # Cleaned dataset used for training & UI
├── requirements.txt # Project dependencies
├── README.md # Project documentation
└── .gitignore # Files/folders to ignore in Git
```