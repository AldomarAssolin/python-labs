# pages/003_Algoritmos.py
import streamlit as st
from pathlib import Path
from ui.sidebar import render_sidebar

# ---- SIDEBAR ----
render_sidebar()

# ---- CONTEÚDO DA PÁGINA ----
st.title("⚙️ Algoritmos")

alg_dir = Path("algoritmos")

if not alg_dir.exists():
    st.info("A pasta 'algoritmos/' ainda está vazia.")
else:
    py_files = list(alg_dir.glob("*.py"))

    if not py_files:
        st.write("Em breve teremos conteúdo para compartilhar!")
    else:
        st.markdown("## 📜 Arquivos encontrados")
        for arquivo in py_files:
            with st.expander(arquivo.name):
                conteudo = arquivo.read_text(encoding="utf-8")
                st.code(conteudo, language="python")

        st.markdown("## 📄 Documentação em Markdown")

        md_files = list(alg_dir.glob("*.md"))

        for arquivo_md in md_files:
            with st.expander(arquivo_md.name):
                conteudo_md = arquivo_md.read_text(encoding="utf-8")
                st.markdown(conteudo_md)
