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
""")
