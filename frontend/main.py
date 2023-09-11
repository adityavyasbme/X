
import requests
import streamlit as st
from src.infrastructure import googleAnalytics as ga
from src.domain import pageConfig, footer

# interact with FastAPI endpoint
backend = "http://fastapi:8000/api/"
api_url = 'https://work.adityavyas.co.in/docs'

ga.inject_ga(st)
pageConfig.set_page_config(st)
footer.hide_footer(st)


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


st.markdown(
    f'<a href="{api_url}" style="display: inline-block; padding: 12px 20px; background-color: #4CAF50; color: white; text-align: center; text-decoration: none; font-size: 16px; border-radius: 4px;">Action Text on Button</a>',
    unsafe_allow_html=True
)
