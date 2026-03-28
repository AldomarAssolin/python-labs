# pages/002_Listas.py
import streamlit as st
from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px
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
CSV_TECH_LAYOFFS = os.path.abspath(os.path.join(BASE_DIR, "..", "docs", "tech_layoffs_2026_tracker.csv"))

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
    with st.expander("Social Media Engagement", expanded=False):

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
    with st.expander("Library Catalog", expanded=False):
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
        
    # IA Layoffs
    with st.expander("IA Layoffs", expanded=False):
        # 2. Carregamento de Dados com Cache
        @st.cache_data
        def load_data():
            # Caminho do seu arquivo CSV
            df = pd.read_csv(CSV_TECH_LAYOFFS, parse_dates=["layoff_date"])
            df['layoff_date'] = pd.to_datetime(df['layoff_date'])
            return df

        df = load_data()

        # --- TÍTULO E CONTEXTO ---
        st.title("📊 Monitoramento de Demissões Tech: A Era da IA (2026)")

        st.caption("Análise detalhada dos cortes de empregos em empresas de tecnologia, com foco na influência da Inteligência Artificial.")

        st.header("Sobre este conjunto de dados")
        st.markdown("""---""")
        st.markdown("""
                    
        Em média **736** trabalhadores da área de `tecnologia` perderão seus empregos todos os dias em 2026.

        > - Não por causa de uma recessão.   
        > - Não por causa de uma crise financeira.   
        > - Por causa da inteligência artificial.   

        Este conjunto de dados rastreia todos os principais **eventos de demissão em massa** no setor de tecnologia em
        2026 — *verificados a partir de fontes em tempo real e atualizados até
        18 de março de 2026* — fornecendo os
        dados estruturados mais recentes sobre demissões disponíveis no Kaggle.

        """)



        with st.expander("📖 Sobre este Dataset e Fontes"):
            st.markdown("""
            **Fonte:** [Kaggle - Tech Layoffs 2026 Tracker](https://www.kaggle.com/datasets/alitaqishah/tech-layoffs-2026-ai-job-cuts-tracker?resource=download)   
            **Período:** Atualizado em 18 de Março de 2026.  
            **Escopo:** Abrange 28 empresas globais em 10 países e 23 setores.
            
            **Contexto de Mercado:** 
            Este rastreamento foca na transição tecnológica.   
            **Eventos marcantes:**   
            - **Oracle (30k)** e **Amazon (16k)** dominam o início do ano.    
            - Um dado crítico: **61% dos cortes** citam explicitamente a IA como motivador principal.
            """)

        # --- MÉTRICAS RÁPIDAS ---
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total de Vagas Cortadas", f"{df['jobs_cut'].sum():,.0f}")
        col2.metric("Empresas Analisadas", len(df))
        col3.metric("% Citaram IA", "61%")
        col4.metric("Ações em Alta", "17 de 28", help="Empresas cujas ações subiram no dia do anúncio")

        # --- ABAS DE ANÁLISE ---
        tab1, tab2, tab3 = st.tabs(["🤖 O Fator IA", "📈 Reação do Mercado", "🌍 Geografia e Setores"])

        with tab1:
            st.header("1. Substituição ou Eficiência? O papel da IA")
            st.markdown("""
            **Explicação:** Este gráfico compara o volume de demissões entre empresas que justificaram o corte pela 
            implementação de IA vs. outros motivos. 
            *   **Referência:** Baseado na coluna `ai_cited` e nos investimentos simultâneos (`simultaneous_ai_investment_bn`).
            """)
            
            fig_ia = px.bar(df, x='company', y='jobs_cut', color='ai_cited',
                            title="Cortes por Empresa: O 'Carimbo' da IA",
                            labels={'jobs_cut': 'Vagas Cortadas', 'ai_cited': 'Citou IA?'},
                            hover_data=['sector', 'ceo_quote'])
            st.plotly_chart(fig_ia, use_container_width=True)

        with tab2:
            st.header("2. Wall Street vs. Força de Trabalho")
            st.markdown("""
            **Explicação:** Cruzamos a agressividade do corte (`% da força de trabalho`) com a reação imediata do preço da ação.
            *   **Referência:** Colunas `pct_workforce_cut` (eixo X) e `stock_change_day_pct` (eixo Y).
            *   **O que observar:** Bolinhas na parte superior indicam que o mercado financeiro "celebrou" a redução de custos.
            """)
            
            fig_market = px.scatter(df, x='pct_workforce_cut', y='stock_change_day_pct',
                                    size='jobs_cut', color='stock_reaction',
                                    hover_name='company', text='company',
                                    title="Variação da Ação (%) vs Impacto Interno (%)")
            fig_market.update_traces(textposition='top center')
            st.plotly_chart(fig_market, use_container_width=True)

        with tab3:
            st.header("3. Concentração Global")
            st.markdown("""
            **Explicação:** Um mapa de calor que identifica quais setores em quais regiões do planeta estão sofrendo 
            o maior volume de demissões brutas.
            *   **Referência:** Cruzamento de `sector`, `region` e a soma de `jobs_cut`.
            """)
            
            mapa_calor = df.pivot_table(index='sector', columns='region', values='jobs_cut', aggfunc='sum').fillna(0)

            fig_heat = px.imshow(mapa_calor, 
                                labels=dict(x="Região", y="Setor", color="Total de Demissões"),
                                title="Calor de Demissões por Setor e Região",
                                text_auto=True, aspect="auto", color_continuous_scale='Reds')
            st.plotly_chart(fig_heat, use_container_width=True)
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