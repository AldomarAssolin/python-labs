import streamlit as st

def header():
    st.markdown('<div class="title-highlight">Olá! Sou Aldomar Assolin</div>', unsafe_allow_html=True)
    st.markdown('<div class="big-title">🧠 Python Labs – Minha Jornada em Python & IA</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">Um laboratório vivo. Um estudo contínuo. Um dev em construção.</div>',
        unsafe_allow_html=True,
    )
    
    # Navigation
    with st.container(width='stretch',height=60):
        st.page_link("app.py",label="Home",icon="🏠")