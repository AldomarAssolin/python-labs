from ui.style import styles
import streamlit as st

def navbar():
    st.markdown(
        """
        <nav class="nav">
            <a href="/" class="nav-link" target="_self">Home</a>
            <a href="/About" class="nav-link" target="_self">Sobre Mim</a>
            <a href="/Projetos" class="nav-link" target="_self">Projetos</a>
        </nav>
        """,
        unsafe_allow_html=True,
    )