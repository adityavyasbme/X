from urllib.parse import urlparse
import streamlit as st
from src.domain import footer
import os

footer.hide_footer(st)

env = os.environ.get('ENVIRONMENT', 'Not Set')
if env == "Not Set":
    raise "Enviornment not set"
elif env == 'local':
    base_path = "http://localhost:8501"
else:
    base_path = "http://work.adityavyas.co.in"


st.markdown("# Project Lists")
st.write(f"""
    1. [Demo Project]({base_path}/Demo%20Project)    
    2. [LLM - Cover Letter Generation]({base_path}/LLM%20-%20Cover%20Letter%20Generation)
    3. [ML - Simple Linear Regression based Car Valuation]({base_path}/ML%20-%20Simple%20Linear%20Regression%20based%20Car%20Valuation)
    4. [ML - Stock Price Prediction using ARIMA]({base_path}/ML%20-%20Stock%20Price%20Prediction%20using%20ARIMA)
""")
