# pages/001_Fundamentos.py
import streamlit as st
from pathlib import Path
from ui.sidebar import render_sidebar

# ---- SIDEBAR ----
render_sidebar()

# ---- CONTEÚDO DA PÁGINA ----
st.title("🧩 Fundamentos de Python")

fundamentos_dir = Path("fundamentos")

if not fundamentos_dir.exists():
    st.info("A pasta 'fundamentos/' ainda está vazia.")
else:
    
    py_files = list(fundamentos_dir.glob("*.py"))
    md_files = list(fundamentos_dir.glob("*.md"))

    # Se ambas vazias
    if not py_files and not md_files:
        st.info("Em breve teremos conteúdo para compartilhar!")
    
    # ---------- SEÇÃO DE MARKDOWN ----------
    if md_files:
        st.markdown("## 📄 Documentação em Markdown")
        for arquivo_md in md_files:
            with st.expander(arquivo_md.name):
                conteudo_md = arquivo_md.read_text(encoding="utf-8")
                st.markdown(conteudo_md)

    # ---------- SEÇÃO DE ARQUIVOS PYTHON ----------
    if py_files:
        st.markdown("## 📜 Arquivos Python")
        for arquivo_py in py_files:
            with st.expander(arquivo_py.name):
                conteudo_py = arquivo_py.read_text(encoding="utf-8")
                st.code(conteudo_py, language="python")
    else:
        st.info("Nenhum arquivo Python criado até o momento.")
        

