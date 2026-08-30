import streamlit as st

from ui.navbar import navbar
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

# ---- Nav ----
navbar()

# Config de layout
st.title("👤 Sobre Mim")
st.caption("Minha trajetória, foco atual e direção profissional.")

st.divider()

# ====== HERO / RESUMO ======
col1, col2 = st.columns([2, 1], gap="large")

with col1:
    st.subheader("Quem eu sou")
    st.write(
        """
Sou **Aldomar “Manex” Assolin**. Vim do chão de fábrica, com experiência em soldagem,
liderança de produção e melhoria de processos, e hoje direciono essa bagagem para
**desenvolvimento de software, Python, dados e Inteligência Artificial aplicada**.

Minha formação atual inclui a **Pós-graduação em Gestão da Indústria 4.0**, em andamento,
reforçando a conexão entre tecnologia, automação, processos industriais e aplicação prática.

Tenho satisfação em construir coisas úteis: apps simples, APIs, automações, agentes determinísticos e ferramentas que
resolvem problemas reais, especialmente os que eu vivi na indústria: **organização,
rastreabilidade, produtividade e qualidade**.
        """
    )

    st.subheader("Meu foco atual")
    st.write(
        """
- **Artefato aplicado:** GTH Agents, sistema digital de apoio à decisão para o TCC da pós-graduação
- **Backend:** Python, Django em trilha inicial e evolução em Java/Spring Boot
- **Banco de dados:** SQL e modelagem relacional (e explorando NoSQL quando faz sentido)
- **Boas práticas:** organização de projeto, POO, arquitetura, documentação e evidências
- **Objetivo:** transformar problemas reais em soluções de software úteis, explicáveis e evolutivas
        """
    )

with col2:
    st.subheader("Stack (na prática)")
    st.markdown(
        """
**Linguagens:** Python, Java, PHP, JavaScript
**Frameworks:** Streamlit, Django (trilha inicial), Flask (aprendendo), React (base)
**DB:** MySQL/SQL (bom domínio), modelagem ER
**Ferramentas:** Git/GitHub, Postman, Swagger, Linux (em evolução)
**Direção:** IA aplicada, agentes determinísticos, automações e Indústria 4.0
        """
    )

st.divider()

# ====== LINHA DO TEMPO / HISTÓRIA ======
with st.expander("📌 Minha trajetória (resumo)", expanded=True):
    st.write(
        """
- **15 anos como soldador** e vivência forte em produção, processos e melhoria contínua
- Migração para tecnologia com foco em **desenvolvimento de software, Python e IA aplicada**
- Formação em andamento em **Gestão da Indústria 4.0**
- Projetos próprios para consolidar aprendizagem (ex.: Python Labs, GTH Agents como artefato aplicado, apps de gestão e API)
        """
    )

# ====== CONTATO / LINKS ======
st.subheader("Contato e redes")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("**LinkedIn**")
    st.write('<a href="https://www.linkedin.com/in/aldomarassolin" class="links" target="_blank">linkedin.com/aldomarassolin</a>', unsafe_allow_html=True)

with c2:
    st.markdown("**GitHub**")
    st.write('<a href="https://github.com/AldomarAssolin" class="links" target="_blank">github.com/AldomarAssolin</a>', unsafe_allow_html=True)

with c3:
    st.markdown("**Email**")
    st.write("assolinaldomar@gmail.com")

st.info("Meu foco é unir experiência industrial, estudo técnico e entrega prática em software, dados e IA aplicada.")


# ---- RODAPE ----
footer()
