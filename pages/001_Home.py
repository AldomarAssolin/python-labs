# app.py
import streamlit as st
from pathlib import Path
from ui.navbar import navbar
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

# ---- Nav ----
navbar()


st.write(
    """
Aqui eu registro minha evolução profissional saindo da vivência de **chão de fábrica, soldagem e produção**
para **desenvolvimento de software, Python, dados e Inteligência Artificial aplicada**.

Este portfólio apresenta meu esforço de estudo e aplicação prática: cada trilha, script,
experimento e projeto mostra uma parte da construção de repertório técnico com problemas reais como referência.
"""
)

# ---- TAGS RÁPIDAS ----
st.markdown(
    """
    <span class="tag">📚 Python aplicado</span>
    <span class="tag">⚙️ Software e backend</span>
    <span class="tag">🤖 IA e agentes</span>
    <span class="tag">🏭 Indústria 4.0</span>
    """,
    unsafe_allow_html=True,
)

st.html("""<a href="/About" class="btn-links">Saiba mais sobre mim</a>""")

st.markdown("---")

# ---- TRÊS COLUNAS DE VISÃO GERAL ----
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Status", "Portfólio em evolução", None)
    st.write(
        "A base do laboratório segue crescendo com estudos, scripts, páginas didáticas "
        "e experimentos organizados como evidência prática."
    )

with col2:
    st.metric("Artefato aplicado", "GTH Agents", None)
    st.write(
        "Sistema digital de apoio à decisão pensado como artefato do TCC da pós-graduação, "
        "conectando software, dados e Gestão do Talento Humano."
    )

with col3:
    st.metric("Formação", "Gestão da Indústria 4.0", "em andamento")
    st.write(
        "A pós-graduação reforça o elo entre tecnologia, processos industriais, "
        "dados, automação e melhoria operacional."
    )

st.markdown("""---""")
# ---- SEÇÕES EXPLICATIVAS ----
st.markdown('<div class="section-title">🚀 Artefato aplicado: GTH Agents</div>', unsafe_allow_html=True)
st.write(
    """
**GTH Agents** é um artefato aplicado que estou desenvolvendo para conectar minha pós-graduação
em **Gestão da Indústria 4.0** com minha evolução em software, dados e Inteligência Artificial aplicada.

Minha proposta é tratar o sistema como um apoio digital à decisão em **Gestão do Talento Humano (GTH)**,
organizando informações de colaboradores, competências, avaliações, metas, feedbacks, reconhecimentos
e PDIs em uma base mais estruturada e rastreável.

No portfólio, ele mostra minha passagem de exercícios isolados para uma aplicação com domínio,
arquitetura, autenticação, controle de acesso, documentação técnica e relação direta com um problema
de gestão e desenvolvimento de pessoas.
"""
)

gth_stack, gth_objetivo = st.columns(2, gap="large")

with gth_stack:
    st.subheader("Stack principal")
    st.write(
        "- Backend em Python com Flask\n"
        "- API REST com Clean Architecture\n"
        "- PostgreSQL, SQLAlchemy e Alembic\n"
        "- Frontend React/Vite com Tailwind CSS\n"
        "- Docker, autenticação JWT e controle de acesso por perfil e escopo"
    )

with gth_objetivo:
    st.subheader("Objetivo prático")
    st.write(
        "- Centralizar histórico e evolução de colaboradores\n"
        "- Estruturar avaliações, metas, feedbacks, reconhecimentos e PDIs\n"
        "- Apoiar decisões de gestão de pessoas com dados rastreáveis\n"
        "- Classificar perfis de talento por regras de negócio\n"
        "- Evoluir para saúde organizacional, analytics e people analytics"
    )

st.markdown('<div class="section-title">🎓 Formação e trilha atual</div>', unsafe_allow_html=True)
st.write(
    """
Minha formação em andamento agora combina **Pós-graduação em Gestão da Indústria 4.0** com uma trilha prática
de Python, backend, dados e IA.

A ideia é usar a experiência anterior em produção como vantagem técnica: entender processos, gargalos,
rastreabilidade e melhoria contínua, e então traduzir isso em software, automações e aplicações de IA.
"""
)

st.markdown('<div class="section-title">📘 O que estou estudando agora</div>', unsafe_allow_html=True)
st.write(
    """
Minha trilha se apoia em:

- *Introdução à Programação com Python* – Nilo Ney Coutinho Menezes  
- *Entendendo Algoritmos* – Aditya Bhargava  
- Um cronograma pessoal de **IA com Python**, indo de fundamentos até deploy de modelos.
- Uma trilha inicial de **Backend com Django**, registrada sem criar evidências vazias.

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
        "- Protótipos de software, dados e automação\n"
        "- GTH Agents como artefato aplicado do TCC da pós-graduação\n"
    )

# ---- LISTAGEM AUTOMÁTICA DAS PASTAS ----
st.markdown("---")
st.markdown('<div class="section-title">📂 Estrutura do laboratório (autoatualizada)</div>', unsafe_allow_html=True)


pastas = ["fundamentos", "listas", "tuplas", "dicionarios", "algoritmos", "projetos"]  # ajuste aqui conforme seu repo
st.caption(f"Path: {BASE_DIR} — clicando na pasta, você vê os arquivos dentro dela.")
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
st.divider()


# ====== PROVAS / PROJETOS ======
st.subheader("Projetos em destaque")
st.write("Projetos que demonstram meu avanço técnico, minha dedicação aos estudos e minha busca por aplicação prática:")
st.divider()
p1, p2, p3 = st.columns(3, gap="large")

with p1:
    st.markdown("### 🤖 GTH Agents")
    st.write(
        "Artefato aplicado do TCC da pós-graduação: um sistema digital de apoio à decisão em Gestão do Talento Humano."
    )
    st.markdown("- Stack: Python/Flask, React/Vite, PostgreSQL, SQLAlchemy, Docker e JWT")
    st.html("""<a href="https://github.com/AldomarAssolin/gth-agents.git" class="btn-links" target="_blank" rel="noopener noreferrer">Ver no GitHub</a>""")

with p2:
    st.markdown("### 🧠 Python Labs")
    st.write(
        "Um laboratório de estudos: exercícios, mini-projetos, páginas didáticas e experimentos com IA."
    )
    st.markdown("- Objetivo: aprender fazendo, com organização e evolução contínua")
    st.html("""<a href="https://github.com/AldomarAssolin/python-labs" class="btn-links" target="_blank" rel="noopener noreferrer">Ver no GitHub</a>""")

with p3:
    st.markdown("### 🏭 App de Controle de Produção (em evolução)")
    st.write(
        "Projeto focado em importação de planilhas, fila de produção por item, status e rastreio do fluxo (montagem → soldagem → inspeção)."
    )
    st.markdown("- Objetivo: digitalizar processos reais do meu contexto industrial")
    st.html("""<a href="https://github.com/AldomarAssolin/op-app" class="btn-links" target="_blank" rel="noopener noreferrer">Ver no GitHub</a>""")


# ---- RODAPE ----
footer()
