import streamlit as st
from src.domain import footer
import os
import requests
from pprint import pprint
from src.domain.pageConfig import set_env_vars
set_env_vars()
footer.hide_footer(st)

backend = os.environ['backend']

st.markdown("# Rule Based Recommendations for Option Pricing")
st.write("""
    Welcome to this interactive tool for option pricing! Here, you can select different option pricing models and input relevant parameters to get pricing recommendations. This tool uses rule-based logic to analyze the output from the selected model and offer actionable insights.

    To understand the theory behind these models, check out the [Medium article](https://medium.com/@CrazyStupidTraveller/bb02cf5accc4?source=friends_link&sk=bbe0f023fac5f6491219ff95c52eff84).

    For a deeper dive into the code, visit the [GitHub repository](https://github.com/adityavyasbme/MachineLearningProjects/blob/main/finance/derivativePricing/blackScholes.ipynb).
    """)
st.markdown("---")

# Model Selection
modelName = st.selectbox("Select Option Pricing Model", [
    "BlackScholes", "Black76", "GarmanKohlhagen", "BachelierModel", "BinaryOption"])

# Common Fields with Default Values
stockPrice = st.number_input("Stock Price", min_value=0.01, value=100.0)
strikePrice = st.number_input("Strike Price", min_value=0.01, value=100.0)
timeToExpirationYr = st.number_input(
    "Time to Expiration (Years)", min_value=0.01, value=1.0)
riskFreeRate = st.number_input(
    "Risk-Free Rate", min_value=0.0, max_value=1.0, value=0.5)
volatility = st.number_input(
    "Volatility", min_value=0.0, max_value=1.0, value=0.2)
optionType = st.selectbox("Option Type", ["call", "put"], index=0)

# Conditional Fields
dividendYield = 0.0
foreignRiskFreeRate = 0.0

if modelName in ["BlackScholes", "GarmanKohlhagen"]:
    dividendYield = st.number_input(
        "Dividend Yield", min_value=0.0, max_value=1.0, value=0.01)

if modelName == "GarmanKohlhagen":
    foreignRiskFreeRate = st.number_input(
        "Foreign Risk-Free Rate", min_value=0.0, max_value=1.0, value=0.02)


# Create dictionary of inputs
input_dict = {
    "modelName": modelName,
    "stockPrice": stockPrice,
    "strikePrice": strikePrice,
    "timeToExpirationYr": timeToExpirationYr,
    "riskFreeRate": riskFreeRate,
    "volatility": volatility,
    "dividendYield": dividendYield,
    "foreignRiskFreeRate": foreignRiskFreeRate,
    "optionType": optionType
}
st.markdown("---")
url = backend+'optionPricingRecommendation'
if st.button("Get Recommendations"):
    with st.spinner("""Fetching Recommendations"""):
        r = requests.post(url, json=input_dict)
    if r.status_code == 200:
        res = r.json()
        st.json(res['result'])
        st.write(res['recommendation'])
    st.markdown("---")
