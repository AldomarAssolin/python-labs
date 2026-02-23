# app.py
import streamlit as st
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent

page_home = st.Page(str(ROOT_DIR / "pages/001_Home.py"), title="Home", icon="🏠")
page_about = st.Page(str(ROOT_DIR / "pages/000_About.py"), title="Sobre Mim", icon="👤")
page_fundamentos = st.Page(str(ROOT_DIR / "pages/002_Fundamentos.py"), title="Fundamentos", icon="📚")
page_algoritmos = st.Page(str(ROOT_DIR / "pages/003_Algoritmos.py"), title="Algoritmos", icon="⚙️")
page_projetos = st.Page(str(ROOT_DIR / "pages/004_Projetos.py"), title="Projetos", icon="💹")
page_explorer = st.Page(str(ROOT_DIR / "pages/010_Explorer.py"), title="Explorer", icon="📁")

nav = st.navigation([
    page_home,
    page_about,
    page_fundamentos,
    page_algoritmos,
    page_projetos,
    page_explorer
])

nav.run()

