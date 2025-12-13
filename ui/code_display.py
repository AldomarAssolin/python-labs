"""
Docstring for ui.display_code_snippet
"""

import streamlit as st
from pathlib import Path
from ui.style import styles
from ui.sidebar import render_sidebar


def display_code_snippet(code: str, language: str = "python"):
    """

    Exibe um trecho de código formatado na aplicação Streamlit.

    Parâmetros:
    - code (str): O código a ser exibido.
    - language (str): A linguagem de programação do código (padrão é "python").

    """
    st.markdown("### Trecho de Código")
    st.code(code, language=language)
