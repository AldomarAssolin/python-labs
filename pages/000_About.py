import streamlit as st

from ui.sidebar import render_sidebar
from ui.style import styles
from ui.header import header
from ui.footer import footer

# ---- CONFIGURAÇÕES DA PÁGINA ----
st.set_page_config(
    page_title="Sobre Mim",
    page_icon="👤",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---- SIDEBAR ----
render_sidebar()

# ---- ESTILO BÁSICO (CSS SIMPLES) ----
styles()

# ---- CABEÇALHO ----
header()

# Config de layout
st.title("👤 Sobre Mim")
st.caption("Um pouco da minha história, foco atual e como posso agregar.")

st.divider()

# ====== HERO / RESUMO ======
col1, col2 = st.columns([2, 1], gap="large")

with col1:
    st.subheader("Quem eu sou")
    st.write(
        """
Sou **Aldomar “Manex” Assolin**. Vim do chão de fábrica (soldagem e liderança de produção) e hoje estou em transição para **Análise e Desenvolvimento de Sistemas**.

Curto construir coisas úteis: apps simples, APIs, automações e ferramentas que resolvem problemas reais, especialmente os que eu vivi na indústria: **organização, rastreabilidade, produtividade e qualidade**.
        """
    )

    st.subheader("Meu foco atual")
    st.write(
        """
- **Backend:** Python (projetos práticos) e evolução em Java/Spring Boot  
- **Banco de dados:** SQL e modelagem relacional (e explorando NoSQL quando faz sentido)  
- **Boas práticas:** organização de projeto, POO, arquitetura e documentação  
- **Objetivo:** virar um dev capaz de pegar um problema e entregar uma solução do começo ao fim
        """
    )

with col2:
    st.subheader("Stack (na prática)")
    st.markdown(
        """
**Linguagens:** Python, Java, PHP, JavaScript  
**Frameworks:** Streamlit, Flask (aprendendo), React (base)  
**DB:** MySQL/SQL (bom domínio), modelagem ER  
**Ferramentas:** Git/GitHub, Postman, Swagger, Linux (em evolução)
        """
    )

st.divider()

# ====== LINHA DO TEMPO / HISTÓRIA ======
with st.expander("📌 Minha trajetória (resumo)", expanded=True):
    st.write(
        """
- **15 anos como soldador** e vivência forte em produção, processos e melhoria contínua  
- Migração para tecnologia com foco em **desenvolvimento de software**  
- Projetos próprios para consolidar aprendizagem (ex.: Python Labs, apps de gestão e API)
        """
    )

# ====== PROVAS / PROJETOS ======
st.subheader("Projetos em destaque")
st.write("Algumas coisas que eu venho construindo para aprender e gerar valor:")

p1, p2 = st.columns(2, gap="large")

with p1:
    st.markdown("### 🧠 Python Labs")
    st.write(
        "Um laboratório de estudos: exercícios, mini-projetos, páginas didáticas e experimentos com IA."
    )
    st.markdown("- Objetivo: aprender fazendo, com organização e evolução contínua")

with p2:
    st.markdown("### 🏭 App de Controle de Produção (em evolução)")
    st.write(
        "Projeto focado em importação de planilhas, fila de produção por item, status e rastreio do fluxo (montagem → soldagem → inspeção)."
    )
    st.markdown("- Objetivo: digitalizar processos reais do meu contexto industrial")

st.divider()

# ====== CONTATO / LINKS ======
st.subheader("Contato e redes")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("**LinkedIn**")
    st.write("linkedin.com/in/aldomarassolin")

with c2:
    st.markdown("**GitHub**")
    st.write("github.com/AldomarAssolin")

with c3:
    st.markdown("**Email**")
    st.write("assolinaldomar@gmail.com")

st.info("Se você curte projetos com pegada prática (indústria + software), a gente vai se entender.")


# ---- RODAPE ----
footer()
