import streamlit as st
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
else:
    base_path = "http://work.adityavyas.co.in"

backend = "http://fastapi:8000/api/"

st.markdown("# LLM Covel Letter Generator")

option = st.selectbox(
    'Operations Available',
    ('Prompt Generator',
     'GPT Cover Letter Generation (Requires API Key)',
     'Backend Health Check (For Debugging)')
)

st.markdown("---")

if option == 'Backend Health Check (For Debugging)':
    st.write("Let's make sure our backend is running")
    add_health_check_button(st, backend_url=backend)

if option == 'Prompt Generator':
    jd = st.text_area("Paste Job Description (Required)")
    resume = st.text_area("Paste Resume (Not Required)")
    if st.button("Generate Prompt"):
        url = backend+'coverLetterPrompt'
        payload = {
            'job_description': jd,
            'resume': resume
        }
        r = requests.get(url,
                         params=payload
                         )
        st.text_area(label="Copy this prompt and paste it into your LLM" +
                     "Model (e.g., chat.openai.com)",
                     value=r.json(),
                     height=700
                     )


if option == 'GPT Cover Letter Generation (Requires API Key)':
    jd = st.text_area("Paste Job Description (Required)")
    resume = st.text_area("Paste Resume (Not Required)")
    api_key = st.text_input("OpenAI API Key",
                            type="password")
    model_name = st.text_input("OpenAI Model Name",
                               value="gpt-3.5-turbo")

    if st.button("Generate Prompt"):
        url = backend+'coverLetterPromptResponse'
        payload = {
            'job_description': jd,
            'resume': resume,
            'api_key': api_key,
            'model_name': model_name
        }
        r = requests.get(url,
                         params=payload
                         )
        if r.status_code == 200:
            st.text_area(label="Here's your response",
                         value=r.json())
        else:
            st.text_area(label="Failed",
                         value=r.content)
