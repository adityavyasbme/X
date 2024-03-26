from urllib.parse import urlparse
import streamlit as st
from src.domain import footer
import os
from src.domain.pageConfig import set_env_vars
set_env_vars()
footer.hide_footer(st)

base_path = os.environ['base_path']


st.markdown("# Project Lists")
st.write(f"""
    1. [Demo Project]({base_path}/Demo%20Project)    
    2. [LLM - Cover Letter Generation]({base_path}/LLM%20-%20Cover%20Letter%20Generation)
    3. [ML - Simple Linear Regression based Car Valuation]({base_path}/ML%20-%20Simple%20Linear%20Regression%20based%20Car%20Valuation)
    4. [ML - Stock Price Prediction using ARIMA]({base_path}/ML%20-%20Stock%20Price%20Prediction%20using%20ARIMA)
    5. [Option Pricing using Black Scholes with Rule Based Recommendations ]({base_path}/Option%20Pricing%20using%20Black%20Scholes%20with%20BONUS%20Rule%20Based%20Recommendations)
    6. [Chat with PDF]({base_path}/Chat%20With%20PDF)
    7. [Youtube Summarizer ]({base_path}/Youtube%20Summarizer)
    8. [Judger vs Learner Personality]({base_path}/Judger%20vs%20Learner%20Personality)
   
""")
