import streamlit as st

st.title("📚 Dicionários em Python")
st.caption("Chave → valor | Base de JSON, APIs e sistemas reais")

# --- 1) Conceito rápido ---
st.subheader("1) O que é um dicionário?")
st.markdown("""
Um **dicionário** (`dict`) guarda dados no formato **chave → valor**.
Ele é ótimo quando você quer acessar informações por **nome**, não por posição.
""")

# Exemplo simples
st.subheader("2) Exemplo simples")
pessoa = {"nome": "Manex", "idade": 35, "cargo": "Líder de Produção"}
st.code('pessoa = {"nome": "Manex", "idade": 35, "cargo": "Líder de Produção"}', language="python")
st.write("Dicionário (renderizado):", pessoa)

col1, col2 = st.columns(2)
with col1:
    chave = st.selectbox("Escolha uma chave", list(pessoa.keys()))
with col2:
    st.write("Valor:", pessoa.get(chave))

# --- 3) Operações básicas ---
st.subheader("3) Operações básicas")
st.markdown("- Acessar: `d['chave']` ou `d.get('chave')`\n- Atualizar/adicionar: `d['x'] = valor`\n- Remover: `del d['x']` ou `d.pop('x')`")

# --- 4) Mini prática: Agenda em memória ---
st.subheader("4) Mini prática: Agenda (lista de dicionários)")

if "agenda" not in st.session_state:
    st.session_state.agenda = []

with st.form("add_form", clear_on_submit=True):
    nome = st.text_input("Nome")
    email = st.text_input("Email (identificador)")
    telefone = st.text_input("Telefone (opcional)")
    submitted = st.form_submit_button("➕ Adicionar")

if submitted:
    email_norm = email.strip().lower()
    if len(nome.strip()) < 3 or email_norm.count("@") != 1:
        st.error("Nome ou email inválido.")
    else:
        # checar duplicidade
        existe = any(c.get("email") == email_norm for c in st.session_state.agenda)
        if existe:
            st.warning("Já existe um contato com esse email.")
        else:
            st.session_state.agenda.append({
                "nome": nome.strip().title(),
                "email": email_norm,
                "telefone": telefone.strip() or None
            })
            st.success("Contato adicionado!")

st.write("📌 Contatos na agenda:")
st.dataframe(st.session_state.agenda, use_container_width=True)

# --- 5) Buscar por email ---
st.subheader("5) Buscar contato por email")
email_busca = st.text_input("Digite um email para buscar", key="email_busca")
if st.button("🔎 Buscar"):
    email_b = email_busca.strip().lower()
    achado = next((c for c in st.session_state.agenda if c.get("email") == email_b), None)
    if achado:
        st.success("Contato encontrado:")
        st.json(achado)
    else:
        st.info("Contato não encontrado.")
