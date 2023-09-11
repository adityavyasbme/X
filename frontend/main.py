
import requests
import streamlit as st
from src.infrastructure import google_analytics as ga
import webbrowser

# interact with FastAPI endpoint
backend = "http://fastapi:8000/api/"
api_url = 'work.adityavyas.co.in/docs'

ga.inject_ga()


def healthcheck():
    r = requests.get(backend+'healthcheck')
    return r


# construct UI layout
st.title("Projects")

# description and instructions
st.write(
    """This streamlit example uses a FastAPI service as backend.
    Visit this URL at `:8000/docs` for FastAPI documentation."""
)

if st.button("Healthcheck"):
    res = healthcheck().content
    if b'true' in res:
        data = "Healthcheck Success"
    else:
        data = "Healthcheck Failed"
    st.write(data)

if st.button('API Docs'):
    webbrowser.open_new_tab(api_url)
