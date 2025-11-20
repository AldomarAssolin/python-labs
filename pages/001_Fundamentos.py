# pages/001_Fundamentos.py
import streamlit as st
from pathlib import Path

st.title("🧩 Fundamentos de Python")

fundamentos_dir = Path("fundamentos")

if not fundamentos_dir.exists():
    st.info("A pasta 'fundamentos/' ainda está vazia.")
else:
    st.markdown("## 📜 Arquivos encontrados")

    for arquivo in fundamentos_dir.glob("*.py"):
        with st.expander(arquivo.name):
            conteudo = arquivo.read_text(encoding="utf-8")
            st.code(conteudo, language="python")
            
    st.markdown("## 📄 Documentação em Markdown")
    
    for arquivo_md in fundamentos_dir.glob("*.md"):
        with st.expander(arquivo_md.name):
            conteudo_md = arquivo_md.read_text(encoding="utf-8")
            st.markdown(conteudo_md)
