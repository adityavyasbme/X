import streamlit as st
from src.domain import footer
import os
import requests
from pprint import pprint

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

st.markdown("# Microsoft Stock Price Prediction")

st.markdown("### Why ARIMA? ")
st.write("""
In my quest to predict the future value of Microsoft (MSFT) stock, 
particularly its "Adj Close" price for the upcoming week, 
I embarked on an extensive exploration of various modeling 
approaches. I left no stone unturned, experimenting with both 
supervised and unsupervised methods, such as Linear Regression, 
Lasso, Elastic Net, K-Nearest Neighbors (KNN), Decision Trees, 
Support Vector Regression (SVR), MLP Regressor, AdaBoost Regressor, 
Gradient Boost Regressor, Random Forest Regressor, 
Extra Tree Regressor, ARIMA, and Long Short-Term Memory (LSTM) networks.

My dataset was comprehensive, including not only MSFT's historical 
stock prices but also supplementary data like Google's "Adj Close" 
prices, IBM's "Adj Close" prices, Japan-US exchange rates, 
US-UK exchange rates, and key indices such as the S&P 500, 
DJIA, and VIXCLS. To make the data more amenable to analysis, 
I converted these values into their natural logarithms and 
shifted them by a period of five weeks. This transformation 
allowed me to better capture trends and patterns in the data.

Upon running the models, I meticulously assessed their 
performance on training and test data. Notably, Lasso, 
Elastic Net, and KNN emerged as strong contenders, 
demonstrating promising predictive abilities. 
However, I also observed that the ARIMA model delivered a 
compelling performance. What's particularly interesting is 
that ARIMA, a time series model, surpassed even the LSTM, 
which is typically considered a potent tool for sequence data.

Given the success of the ARIMA model, I made the deliberate choice 
to select it as my primary tool for forecasting MSFT stock prices.
With ARIMA as the cornerstone, I took further steps to fine-tune 
the model, leveraging various techniques to optimize its predictive 
capabilities. To enhance the robustness of my forecasts, I employed 
ensemble methods, combining the results of multiple models 
into a cohesive and more reliable prediction. This thorough 
approach allowed me to select the most suitable model for my 
stock prediction task and to refine it for even better accuracy.
""")

st.write(
    "You can access my code and view the graphs on my GitHub repository by following this link: [Notebook](https://github.com/adityavyasbme/MachineLearningProjects/blob/main/finance/stockPricePrediction/microsoftStockPrediction.ipynb).")

st.markdown("---")
st.markdown("### Recent Prediction")

st.write("I created a backend API to get the recent prediction of MSFT stock.")

st.warning("This is a prediction for next week." +
           " Investing in MSFT stock is your choice.")

url = backend+'stockPrediction'
with st.spinner("""It takes about 5 minute to train the model 
every day; So be patient! Once the model is trained 
you will see the result asap!"""):
    r = requests.get(url)
if r.status_code == 200:
    st.json(r.json())
st.markdown("---")
