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
