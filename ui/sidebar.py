# ui/sidebar.py
import streamlit as st

def render_sidebar():
    with st.sidebar:
        # 👉 Imagem de topo (pode ser do GitHub, LinkedIn, etc.)
        st.image(
            "https://avatars.githubusercontent.com/u/106867303",  # exemplo: teu avatar do GitHub
            width=140,
        )

        # 👉 Título e subtítulo
        st.markdown("## 🧠 Python Labs")
        st.markdown("Dev em evolução • Aldomar \"Manex\" Assolin")
        
        # 👉 Status atual
        st.markdown("---")
        st.markdown("### 📊 Status do estudo")
        st.write("• Foco atual: **Fundamentos de Python**")
        st.write("• Próximo passo: **Algoritmos**")
        st.write("• Objetivo: **chegar em IA aplicada**")

        # 👉 Mini “badge” de jornada
        st.markdown("---")
        st.caption("Jornada: Soldagem ➝ ADS ➝ Python & IA")

        # 👉 Links rápidos
        st.markdown("### 🔗 Links")
        st.write("[GitHub](https://github.com/AldomarAssolin)")
        st.write("[LinkedIn](https://linkedin.com/in/aldomarassolin)")

        st.markdown("---")
        st.caption("Versão 0.1 • Laboratório em construção")

