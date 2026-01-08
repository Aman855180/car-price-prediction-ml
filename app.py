import streamlit as st 
import pandas as pd 
import joblib

st.markdown("""
<style>


.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}


h1 {
    color: #ffffff;
    text-align: center;
    font-weight: 700;
}


p {
    color: #cfd8dc;
    text-align: center;
}


label {
    color: #e0e0e0 !important;
    font-weight: 500;
}


.stSelectbox > div > div,
.stNumberInput > div > div {
    background-color: #1f2933;
    color: white;
    border-radius: 10px;
}

.stButton > button {
    background-color: #2563eb;
    color: white;
    border-radius: 10px;
    height: 45px;
    width: 100%;
    font-size: 16px;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #1e40af;
}


.stSuccess {
    background-color: #064e3b;
    color: #d1fae5;
    border-radius: 10px;
    padding: 15px;
    font-size: 18px;
}


footer {visibility: hidden;}
header {visibility: hidden;}

</style>
""", unsafe_allow_html=True)


model = joblib.load("car_price_model.joblib")

df = pd.read_csv("Cleaned Car.csv")

st.title("Car Price Predictor")
st.write("This website predicts the price of a car you want to sell. Try filling the details below:")


company_list = sorted(df["company"].unique())
company=st.selectbox("select your car's company name:",company_list)

car_models = sorted(df[df["company"] == company]["name"].unique())
name = st.selectbox("Select the model:", car_models)

year = st.selectbox("Select Year of Purchase:", sorted(df["year"].unique(), reverse=True))

fuel_type_list = df["fuel_type"].unique()
fuel_type = st.selectbox("Select the Fuel Type:", fuel_type_list)

kms = st.number_input("Enter the Number of Kilometres that the car has travelled:", min_value=0)


if st.button("Predict Price"):
    input_data = pd.DataFrame([[name, company, year, kms, fuel_type]],columns=["name", "company", "year", "kms_driven", "fuel_type"])

    price = model.predict(input_data)[0]

    st.success(f"Estimated Car Price: ₹ {round(price,2)}")