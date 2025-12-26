import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.title("Status do Sistema")

# Mongo
try:
    from infra.mongo import ping
    ping()
    st.success("MongoDB Atlas: conectado ✅")
except Exception as e:
    st.error("MongoDB Atlas: falha na conexão ❌")
    st.caption(str(e))
