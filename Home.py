# main.py
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Python Labs",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("🧠 Python Labs")
st.subheader("Laboratório de Estudos em Python, Algoritmos e IA")

st.write(
    """
    Este é o meu **laboratório interativo de aprendizado em Python**.

    - Estudos dos livros *Introdução à Programação com Python* e *Entendendo Algoritmos*  
    - Experimentos com IA, dados e projetos práticos  
    - Cada módulo fica organizado em pastas e páginas na barra lateral.
    """
)

base = Path(__file__).resolve().parent
pastas = ["fundamentos", "algoritmos", "projetos"]

st.markdown("### 📂 Estrutura do Laboratório")
for pasta in pastas:
    p = base / pasta
    if p.exists():
        arquivos = list(p.glob("*.py"))
        st.write(f"**{pasta.capitalize()}** — {len(arquivos)} arquivos")
        for arq in arquivos:
            st.text(f" • {arq.name}")
    else:
        st.write(f"**{pasta.capitalize()}** — (pasta ainda não criada)")
