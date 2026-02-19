# app.py
import streamlit as st
from pathlib import Path
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


st.write(
    """
Aqui eu registro minha transição de **chão de fábrica e soldagem** para **desenvolvimento de software e Inteligência Artificial**.

Não é um portfólio “pronto e perfeito”.  
É um espaço de estudo, prática e evolução — com código real, erros reais e aprendizado real.
"""
)

# ---- TAGS RÁPIDAS ----
st.markdown(
    """
    <span class="tag">📚 Estudando Python</span>
    <span class="tag">⚙️ Algoritmos</span>
    <span class="tag">🤖 IA em evolução</span>
    <span class="tag">🚀 Portfólio em construção</span>
    """,
    unsafe_allow_html=True,
)

st.markdown("---")

# ---- TRÊS COLUNAS DE VISÃO GERAL ----
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Status", "Em evolução", "+1 script")
    st.write(
        "Estudo um pouco de cada vez, transformando capítulos de livros em código "
        "e pequenos experimentos."
    )

with col2:
    st.metric("Foco atual", "Fundamentos", None)
    st.write(
        "Revisão de sintaxe, funções, estruturas de dados e organização de código "
        "com padrão profissional (main, módulos, etc.)."
    )

with col3:
    st.metric("Objetivo", "IA na prática", None)
    st.write(
        "Construir uma base sólida para depois entrar em análise de dados, ML, DL e MLOps."
    )

st.markdown("""---""")
# ---- SEÇÕES EXPLICATIVAS ----
st.markdown('<div class="section-title">📘 O que estou estudando agora</div>', unsafe_allow_html=True)
st.write(
    """
Minha trilha se apoia em:

- *Introdução à Programação com Python* – Nilo Ney Coutinho Menezes  
- *Entendendo Algoritmos* – Aditya Bhargava  
- Um cronograma pessoal de **IA com Python**, indo de fundamentos até deploy de modelos.

Cada tema que eu estudo vira um script, uma anotação ou um mini-projeto dentro deste laboratório.
"""
)

st.markdown('<div class="section-title">🗂️ Como o Python Labs está organizado</div>', unsafe_allow_html=True)

col_fund, col_alg, col_proj = st.columns(3)

with col_fund:
    st.subheader("🧩 Fundamentos")
    st.write(
        "- Variáveis, tipos e operadores\n"
        "- Condicionais e laços\n"
        "- Funções\n"
        "- Listas, tuplas, dicionários\n"
        "- POO básica\n"
    )

with col_alg:
    st.subheader("⚙️ Algoritmos")
    st.write(
        "- Busca (linear, binária)\n"
        "- Ordenações\n"
        "- Recursão\n"
        "- Complexidade (noções)\n"
        "- Estruturas de dados\n"
    )

with col_proj:
    st.subheader("🚀 Projetos")
    st.write(
        "- Pequenos experimentos com dados\n"
        "- Scripts úteis para o dia a dia\n"
        "- Protótipos de IA e automação\n"
        "- Ideias que podem virar portfólio\n"
    )

# ---- LISTAGEM AUTOMÁTICA DAS PASTAS ----
st.markdown("---")
st.markdown('<div class="section-title">📂 Estrutura do laboratório (autoatualizada)</div>', unsafe_allow_html=True)


pastas = ["fundamentos", "listas", "tuplas", "dicionarios", "algoritmos", "projetos"]  # ajuste aqui conforme seu repo

for pasta in pastas:
    p = BASE_DIR / pasta
    if p.exists():
        arquivos = list(p.glob("*.py"))
        arquivos_md = list(p.glob("*.md"))
        arquivos.extend(arquivos_md)
        with st.expander(f"{pasta.capitalize()} — {len(arquivos)} arquivo(s)"):
            st.caption("Arquivos Python e Markdown encontrados nesta pasta:")

            st.page_link(
                "pages/010_Explorer.py",
                label=f"Abrir {pasta.upper()}",
                icon="📁",
                query_params={"dir": pasta},
            )

            if arquivos:
                for arq in arquivos:
                    st.text(f"• {arq.name}")
            else:
                st.write("Ainda não há arquivos nesta pasta.")


# ---- RODAPE ----
footer()