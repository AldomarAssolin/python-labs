# pages/003_Algoritmos.py
import streamlit as st
from pathlib import Path

st.title("⚙️ Algoritmos")

alg_dir = Path("algoritmos")

if not alg_dir.exists():
    st.info("A pasta 'algoritmos/' ainda está vazia.")
else:
    st.markdown("## 📜 Arquivos encontrados")

    for arquivo in alg_dir.glob("*.py"):
        with st.expander(arquivo.name):
            conteudo = arquivo.read_text(encoding="utf-8")
            st.code(conteudo, language="python")
            
    st.markdown("## 📄 Documentação em Markdown")
    for arquivo_md in alg_dir.glob("*.md"):
        with st.expander(arquivo_md.name):
            conteudo_md = arquivo_md.read_text(encoding="utf-8")
            st.markdown(conteudo_md)
