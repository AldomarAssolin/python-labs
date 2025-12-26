import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from infra.repo_healthcheck import write_healthcheck, list_healthchecks

st.title("MongoDB Test")

# if st.button("Inserir healthcheck"):
#     inserted_id = write_healthcheck()
#     st.success(f"Inserido: {inserted_id}")

st.subheader("Últimos registros")
st.write(list_healthchecks(10))
