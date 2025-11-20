# ui/sidebar.py
import streamlit as st
from streamlit_extras.badges import badge

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
        badge(type="github", name="AldomarAssolin/python-labs")
        # 👉 Mini “badge” de jornada
        st.markdown("---")
        st.caption("Jornada: Soldagem ➝ ADS ➝ Python & IA")
        st.markdown("---")

        # 👉 Links rápidos
        st.subheader("Sinta-se à vontade para conectar!")
        
        st.html("""
                <div class="links-contatos">
                 <a href="https://github.com/AldomarAssolin" target="_blank">
                     <img src="https://img.shields.io/badge/GitHub-AldomarAssolin-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Badge">
                 </a>
                    <a href="https://linkedin.com/in/aldomarassolin" target="_blank">
                        <img src="https://img.shields.io/badge/LinkedIn-AldomarAssolin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Badge">
                    </a>
                </div>
                 """)

        st.markdown("---")
        st.caption("Versão 0.1 • Laboratório em construção")

