# ui/sidebar.py
import streamlit as st
from core.config import BASE_DIR

image_thumb = BASE_DIR / "public" / "images" / "thumb.png" 

def render_sidebar():
    with st.sidebar:
        # 👉 Título e subtítulo
        st.markdown("## 🧠 Python Labs | Portfólio em evolução")
        st.markdown(""">Python, backend, dados e IA aplicada""")
        st.markdown("---")
        
        # Imagem de perfil
        st.image(
            image_thumb, 
            caption="Aldomar “Manex” Assolin",
            
        )

        
        
        # 👉 Status atual
        st.markdown("---")
        st.markdown("### 📊 Status do estudo")
        st.write("• Artefato aplicado: **GTH Agents**")
        st.write("• Base técnica: **Python, backend e dados**")
        st.write("• Formação: **Gestão da Indústria 4.0**")
        
        # 👉 Mini “badge” de jornada
        st.markdown("---")
        st.caption(">Jornada: Soldagem ➝ Software ➝ Python, IA & Indústria 4.0")
        st.markdown("---")

        # 👉 Links rápidos
        st.subheader("Contato profissional")
        
        st.html("""
                <div class="links-contatos">
                 <a href="https://github.com/AldomarAssolin" target="_blank">
                     <img src="https://img.shields.io/badge/GitHub-AldomarAssolin-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Badge">
                 </a>
                    <a href="https://linkedin.com/in/aldomarassolin" target="_blank">
                        <img src="https://img.shields.io/badge/LinkedIn-AldomarAssolin-0A66C2?style=for-the-badge&logo=linkedIn&logoColor=white" alt="LinkedIn Badge">
                    </a>
                </div>
                 """)

        st.markdown("---")
        st.caption("Versão 0.5 • Registro contínuo de estudo e prática")
