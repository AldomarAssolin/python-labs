# header.py
"""
Docstring for ui.header

Author: Aldomar Assolin
Date: 2024-06-15
Description: 
This module defines the header component for the Streamlit application. 
It includes a title, subtitle, and navigation links to different pages of the app.


"""
import streamlit as st

def header():
    st.markdown('<div class="title-highlight">Olá! Sou Aldomar Assolin</div>', unsafe_allow_html=True)
    st.markdown('<div class="big-title">🧠 Python Labs – Minha Jornada em Python & IA</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">Um laboratório vivo. Um estudo contínuo. Um dev em construção.</div>',
        unsafe_allow_html=True,
    )
    
    