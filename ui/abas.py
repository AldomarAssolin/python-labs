import streamlit as st

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
    st.info("""
    Este diretório faz parte da minha jornada de evolução em Python e Inteligência Artificial.
    """)

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
