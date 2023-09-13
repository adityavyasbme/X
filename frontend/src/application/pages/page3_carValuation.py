import streamlit as st
import assets.carValuationParams as cvp
from src.domain import footer
from src.infrastructure.backendHealthCheck import add_health_check_button
import os
import requests

footer.hide_footer(st)

env = os.environ.get('ENVIRONMENT', 'Not Set')
if env == "Not Set":
    raise "Enviornment not set"
elif env == 'local':
    base_path = "http://localhost:8501"
    backend = "http://localhost:8000/api/"
else:
    base_path = "http://work.adityavyas.co.in"
    backend = "http://fastapi:8000/api/"

st.markdown("# Car Valuation")


st.write("""
The car valuation model is intentionally designed with simplicity in mind, 
relying on basic linear regression techniques to offer initial price estimates.
This simplicity ensures that users can easily access and utilize the model
through a user-friendly interface, avoiding the complexities associated with 
advanced algorithms. However, it's crucial to acknowledge that the Simple 
Linear Regression Model has its limitations. It may not provide accurate 
predictions for vehicles featuring attributes that lie outside the scope 
of our training data. Consequently, in such instances, the model's 
predictions may not precisely reflect the true market value of these unique
vehicles.
         
In future, I would focus on integrating better algorithm, e.g., XGBoost         
""")

option = st.selectbox(
    'Operations Available',
    ('Car Valuation',
     'Backend Health Check (For Debugging)')
)

st.markdown("---")

if option == 'Backend Health Check (For Debugging)':
    st.write("Let's make sure our backend is running")
    add_health_check_button(st, backend_url=backend)

if option == 'Car Valuation':
    Year = st.number_input("Car Manufacturing Year",
                           value=2020,
                           min_value=1951, max_value=2023)
    Driven = st.number_input(
        "How much have you driven the car? (KM)",
        format="%.2f",
        value=100000.0,
        min_value=0.0,
        max_value=2000000.0,
        step=1.)
    Fuel = st.selectbox('Fuel Type', [k.name for k in cvp.FuelType])
    SellerType = st.selectbox('Seller Type', [k.name for k in cvp.SellerType])
    TransmissionType = st.selectbox(
        'Transmission', [k.name for k in cvp.TransmisionType])
    Seats = st.number_input("Number of Seats",
                            min_value=2, max_value=8)
    Torque = st.number_input(
        "What's the torque? (RPM)",
        format="%.2f",
        value=500.0,
        min_value=200.0,
        max_value=2000.0,
        step=1.)

    KMPL = st.number_input(
        "What's the mileage? (KMPL)",
        format="%.2f",
        value=20.0,
        min_value=0.0,
        max_value=200.0,
        step=1.)

    EngineCC = st.number_input(
        "What's the Engine Capacity? (CC)",
        format="%.2f",
        value=1000.0,
        min_value=0.0,
        max_value=10000.0,
        step=1.)

    Power = st.number_input(
        "HorsePower? (W)",
        format="%.2f",
        value=700.0,
        min_value=0.0,
        max_value=2000.0,
        step=1.)

    OwnerType = st.selectbox('Owner Status', [k.name for k in cvp.OwnerType])

    if st.button("Valuate"):
        url = backend+'predictCarValuation'
        payload = {
            "Year": Year,
            "Driven": Driven,
            "Fuel": cvp.FuelType[Fuel],
            "SellerType": cvp.SellerType[SellerType],
            "Transmission": cvp.TransmisionType[TransmissionType],
            "Seats": Seats,
            "Torque_RPM": Torque,
            "Mileage_KMPL": KMPL,
            "Engine_CC": EngineCC,
            "Power": Power,
            "Owner": cvp.OwnerType[OwnerType]
        }
        r = requests.post(url,
                          json=payload)

        if r.status_code == 200:
            st.write(
                f"Expected Car Price INR {round(float(r.content.decode('utf-8')),2)}")
        else:
            st.write(r.content)
