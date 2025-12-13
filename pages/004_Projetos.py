# pages/002_Listas.py
import streamlit as st
from pathlib import Path
import os
import pandas as pd
from ui.sidebar import render_sidebar

BASE_DIR = os.path.dirname(__file__)
CLEAN_PATH = os.path.join(BASE_DIR, "..", "docs", "social_media_clean.csv")

# ---- SIDEBAR ----
render_sidebar()

# ---- CONTEÚDO DA PÁGINA ----
st.title("🧩 Projetos em Python")

# ===============================
# Abas principais
# ===============================
tab_conceitos, tab_exemplos, tab_exercicios = st.tabs(
    ["📘 Principal", "🧪 Exemplos Práticos", "📚 Docs"]
)

# ===============================
# Aba 1 - Conceitos
# ===============================
with tab_conceitos:
    st.markdown("""
                # 🚀 Projetos – Python Labs

Este diretório reúne os meus projetos práticos dentro do Python Labs.  
São experimentos, pequenos sistemas, testes e protótipos que aplicam na prática tudo o que estou estudando.

---

## 🎯 Objetivo dos projetos
- Transformar teoria em prática  
- Construir portfólio real e progressivo  
- Testar ideias e consolidar a aprendizagem  
- Conectar Python com dados, IA, APIs e automações  
- Criar aplicações pequenas, mas funcionais, que evoluem junto comigo  

---

## 📚 Base de estudo
Os projetos são inspirados nos módulos do meu cronograma de IA:

- Fundamentos de Python  
- Manipulação e análise de dados (NumPy, Pandas)  
- Machine Learning e classificação  
- Redes neurais e visão computacional  
- Criação de APIs com Flask/FastAPI  
- Boas práticas de organização e versionamento  

Referência: Cronograma de Aprendizado de IA com Python

---

## 🧩 Estrutura típica de cada projeto
Cada projeto tem seu próprio diretório:


                """)

    
# ===============================
# Aba 2 - Exemplos Práticos
# ===============================
with tab_exemplos:            
    st.set_page_config(page_title="Social Media Analytics", layout="wide")

    st.title("📊 Social Media Engagement")
    st.markdown("""
    Este exemplo demonstra como carregar dados de **engajamento de mídia social** a partir de um arquivo **CSV**, limpar os dados usando a biblioteca **pandas** e visualizar as impressões diárias ao longo do tempo com gráficos de linha e barras.
    """)
    st.markdown(">Veja o código na aba ``📚 Docs`` no arquivo `social_media.py`.")
    st.markdown("---")

    df = pd.read_csv(CLEAN_PATH, parse_dates=["DATE"])

    st.subheader("Tabela de dados")
    st.dataframe(df, use_container_width=True)

    st.subheader("Impressões diárias")
    st.line_chart(
        df.set_index("DATE")["DAILY IMPRESSIONS"]
    )

    source = df.sort_values(by="DATE")
    st.subheader("Impressões diárias (gráfico de barras)")
    st.bar_chart(
        source,
        x="DATE",
        y="DAILY IMPRESSIONS",
        stack=False
    )
    
# ===============================
# Aba 3 - Exercícios Guiados
# ===============================
with tab_exercicios:
    projetos_dir = Path("projetos")

    if not projetos_dir.exists():
        st.info("A pasta 'projetos/' ainda está vazia.")
    else:
        
        py_files = list(projetos_dir.glob("*.py"))
        md_files = list(projetos_dir.glob("*.md"))

        if not py_files and not md_files:
            st.info("Em breve teremos conteúdo para compartilhar!")
            
        # ---------- SEÇÃO DE MARKDOWN ----------
        if md_files:    
            st.markdown("## 📄 Documentação em Markdown")    
            for arquivo_md in projetos_dir.glob("*.md"):
                with st.expander(arquivo_md.name):
                    conteudo_md = arquivo_md.read_text(encoding="utf-8")
                    st.markdown(conteudo_md)
                    
        # ---------- SEÇÃO DE ARQUIVOS PYTHON ----------
        if py_files:          
            st.markdown("## 📜 Arquivos encontrados")
            for arquivo in projetos_dir.glob("*.py"):
                if arquivo.suffix == ".py":
                    with st.expander(arquivo.name):
                        conteudo = arquivo.read_text(encoding="utf-8")
                        st.code(conteudo, language="python")
        else:
            st.info("Nenhum arquivo Python criado até o momento.")
    