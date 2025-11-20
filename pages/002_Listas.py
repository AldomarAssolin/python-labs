# pages/002_Listas.py
import streamlit as st
from pathlib import Path

st.title("🧩 Listas em Python")

listas_dir = Path("listas")

if not listas_dir.exists():
    st.info("A pasta 'listas/' ainda está vazia.")
else:
    py_files = list(listas_dir.glob("*.py"))
    
    if not py_files:
        st.write("Em breve teremos conteúdo para compartilhar!")
    else:
        st.markdown("## 📜 Arquivos encontrados")
        for arquivo in listas_dir.glob("*.py"):
            with st.expander(arquivo.name):
                conteudo = arquivo.read_text(encoding="utf-8")
                st.code(conteudo, language="python")

        st.markdown("## 📄 Documentação em Markdown")    

        for arquivo_md in listas_dir.glob("*.md"):
            with st.expander(arquivo_md.name):
                conteudo_md = arquivo_md.read_text(encoding="utf-8")
                st.markdown(conteudo_md)