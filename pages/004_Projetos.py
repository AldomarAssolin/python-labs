# pages/002_Listas.py
import streamlit as st
from pathlib import Path
import os
import base64
import pandas as pd
from typing import Dict, List
import csv
from ui.card import card_container, card_html
from ui.navbar import navbar
from ui.sidebar import render_sidebar
from ui.style import styles
from ui.footer import footer
from ui.header import header
from core.config import BASE_DIR


# ---- SIDEBAR ----
render_sidebar()

# ---- ESTILO BÁSICO (CSS SIMPLES) ----
styles()

# ===============================
# Header
# ===============================
header()

# ===============================
# CONFIGURAÇÕES DA PÁGINA
# ===============================

st.set_page_config(
    page_title="Projetos",
    page_icon="📅",
    layout="wide",
)

BASE_DIR = os.path.dirname(__file__)
CLEAN_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "docs", "social_media_clean.csv"))
LIB_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "docs", "library_books.csv"))
IMAGEM_CARD = os.path.abspath(os.path.join(BASE_DIR, "..", "public", "images", "thumb.png"))
IMAGEM_THUMB = os.path.abspath(os.path.join(BASE_DIR, "..", "public", "images", "thumb-op-app.png"))

image_thumb = Path(BASE_DIR) / "public" / "images" / "thumb.png"
image_thumb = Path(BASE_DIR) / "public" / "images" / "thumb.png"

# ---- Nav ----
navbar()

# ---- CONTEÚDO DA PÁGINA ----
# ------ Titulo ------
st.title("📅 Projetos em Python")

# ===============================
# Abas principais
# ===============================
tab_principal, tab_exemplos, tab_docs = st.tabs(
    ["📘 Principal", "🧪 Exemplos Práticos", "📚 Docs"]
)

# ===============================
# Aba 1 - Principal
# ===============================
with tab_principal:
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
    - `README.md` com descrição, objetivos e aprendizados.
    - `exemplos práticos` com notebooks ou scripts de demonstração.
    - `docs` com anotações, insights e codigos de exemplo.
    

                """)
    
    st.divider()

    # ===============================
    # Projetos em destaque
    # ===============================

    st.header("🚀 Projetos em destaque")
    st.subheader("Algumas coisas que eu venho construindo para aprender e gerar valor")
    st.divider()

    def load_image_base64(image_path):
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
        
    image_card_base64 = load_image_base64(IMAGEM_CARD)
    image_op_app_base64 = load_image_base64(IMAGEM_THUMB)

    card_labs = card_html(
    title="Python Labs",
    text="Um laboratório de estudos: exercícios, mini-projetos, páginas didáticas e experimentos com IA.",
    image=f"data:image/png;base64,{image_card_base64}",
    url="https://github.com/AldomarAssolin/python-labs"
    )
    
    card_op_app = card_html(
    title="App de Controle de Produção",
    text="Projeto focado em importação de planilhas, fila de produção por item, status e rastreio do fluxo (montagem → soldagem → inspeção).",
    image=f"data:image/png;base64,{image_op_app_base64}",
    url="https://github.com/AldomarAssolin/op-app"
    )

    card_container([card_labs, card_op_app])

    
# ===============================
# Aba 2 - Exemplos Práticos
# ===============================
with tab_exemplos:   
    
    # Social Media analises         
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
    
    # Livraria
    
    # Lista todos os livros
    def lista_todos_livros(caminho) -> List[Dict]:
        if not os.path.exists(caminho):
            return []
        
        with open(caminho, "r", newline="", encoding="utf-8") as arquivo:
            reader = csv.DictReader(arquivo)
            return list(reader)

    livros = lista_todos_livros(LIB_PATH)

    df = pd.DataFrame(livros)

    st.header("📚 Catálogo de Livros (Exemplo)")
    st.dataframe(df, use_container_width=True)

# ===============================
# Aba 3 - Documentacao
# ===============================
with tab_docs:
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
# ===============================
# Footer
# ===============================
footer()    