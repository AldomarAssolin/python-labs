import streamlit as st
import os

def check_auth():
    pwd = st.text_input("Senha de acesso", type="password")
    if pwd != os.getenv("AI_ACCESS_PASSWORD"):
        st.stop()

check_auth()
