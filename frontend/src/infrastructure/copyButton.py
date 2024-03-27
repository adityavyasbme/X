import streamlit as st
import clipboard

if "copied" not in st.session_state:
    st.session_state.copied = []


def on_copy_click(text):
    st.session_state.copied.append(text)
    clipboard.copy(text)
