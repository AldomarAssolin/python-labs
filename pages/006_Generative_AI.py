import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI
from ui.sidebar import render_sidebar
from ui.style import styles

# Carrega variáveis de ambiente
load_dotenv()

st.header("Estudando conexão com IA Generativa")


# ===============================
# CONFIGURAÇÕES DA PÁGINA
# ===============================
# ----  ----
st.set_page_config(
    page_title="IA Generativa",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ===============================
# Sidebar
# ===============================

render_sidebar()

# ===============================
# ESTILO BÁSICO (CSS SIMPLES)
# ===============================

styles()

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


    # Cliente OpenAI
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY")
    )

    st.title("Chat com OpenAI")

    prompt = st.text_area("Digite sua pergunta:")

    if st.button("Enviar"):
        if not prompt.strip():
            st.warning("Digite alguma coisa, ser humano.")
        else:
            with st.spinner("Pensando..."):
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "Você é um assistente técnico e didático."},
                        {"role": "user", "content": prompt}
                    ]
                )

                st.markdown("### Resposta")
                st.write(response.choices[0].message.content)

# ===============================
# Aba 2 - Exemplos Práticos
# ===============================
with tab_exemplos:
    st.info("""
    Aqui estudo, implemento e documento algoritmos essenciais para desenvolver meu raciocínio lógico e minha base como programador.
    Cada arquivo representa um capítulo do meu aprendizado — simples, direto e prático.
    """) 
    
# ===============================
# Aba 3 - Documentação
# ===============================
with tab_docs:
    st.info("""
    Aqui estudo, implemento e documento algoritmos essenciais para desenvolver meu raciocínio lógico e minha base como programador.
    """)