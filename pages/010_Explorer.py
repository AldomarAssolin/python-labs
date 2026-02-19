from pathlib import Path
import streamlit as st

from ui.sidebar import render_sidebar
from ui.style import styles
from ui.footer import footer
from ui.header import header
from core.config import BASE_DIR

# ---- CONFIGURAÇÕES DA PÁGINA ----
st.set_page_config(
    page_title="Python Labs",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---- SIDEBAR ----
render_sidebar()

# ---- ESTILO BÁSICO (CSS SIMPLES) ----
styles()

# ---- CABEÇALHO ----
header()

BASE_DIR = Path(__file__).resolve().parents[1]  # raiz do projeto

st.title("📁 Explorer")

dir_name = st.query_params.get("dir")

if not dir_name:
    st.info("Nenhuma pasta selecionada.")
    st.stop()

target = (BASE_DIR / dir_name).resolve()

# Segurança básica: impede sair da raiz via path estranho
if BASE_DIR not in target.parents and target != BASE_DIR:
    st.error("Caminho inválido.")
    st.stop()

if not target.exists() or not target.is_dir():
    st.error(f"Pasta não encontrada: {dir_name}")
    st.stop()

st.caption(f"Pasta: `{dir_name}`")

files = sorted([p for p in target.glob("*") if p.is_file() and p.suffix in {".py", ".md"}])

if not files:
    st.warning("Sem arquivos nessa pasta.")
    st.stop()

for f in files:
    with st.expander(f.name):
        if f.suffix == ".md":
            st.markdown(f.read_text(encoding="utf-8"))
        else:
            st.code(f.read_text(encoding="utf-8"), language="python")

# ---- RODAPE ----
footer()