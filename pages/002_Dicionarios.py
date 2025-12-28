import streamlit as st

from pathlib import Path
from ui.sidebar import render_sidebar
from ui.style import styles
from ui.footer import footer
from ui.header import header

# ---- SIDEBAR ----
render_sidebar()

# ---- ESTILO BÁSICO (CSS SIMPLES) ----
styles()

# ===============================
# Header
# ===============================
header()

# ===============================
# CONFIGURAÇÕES DA PÁGINA
# ===============================

st.set_page_config(
    page_title="Dicionarios",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---- CONTEÚDO DA PÁGINA ----
# ------ Titulo ------
st.title("📚 Documentação sobre Dicionários em Python")

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

    st.markdown("""
    ## O que é um dicionário?
    Um dicionário é uma coleção de pares chave-valor, onde cada chave é única.

    ## Criando dicionários
    - Vazio: `d = {}`
    - Com dados: `d = {"chave1": valor1, "chave2": valor2}`

    ## Acessando valores
    - Por chave: `valor = d["chave"]`
    - Com método get: `valor = d.get("chave", valor_padrao)`

    ## Modificando dicionários
    - Adicionar/atualizar: `d["nova_chave"] = novo_valor`
    - Remover: `del d["chave"]` ou `d.pop("chave")`

    ## Iterando sobre dicionários
    - Chaves: `for chave in d.keys():`
    - Valores: `for valor in d.values():`
    - Itens: `for chave, valor in d.items():`

    ## Métodos úteis
    - `d.keys()`: retorna todas as chaves
    - `d.values()`: retorna todos os valores
    - `d.items()`: retorna pares chave-valor
    - `d.clear()`: remove todos os itens
    - `d.update(outro_dicionario)`: atualiza com outro dicionário

    ## Documentação oficial
    [Dicionários na documentação do Python](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
    """)

# ===============================
# Aba 2 - Exemplos Práticos
# ===============================
with tab_exemplos: 
    st.title("📚 Dicionários em Python")
    st.caption("Chave → valor | Base de JSON, APIs e sistemas reais")
    st.markdown(">Veja o código na aba ``📚 Docs`` no arquivo `agenda.py`.")
    st.markdown("---")

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
            
# ===============================
# Aba 3 - Documentação
# ===============================
with tab_docs:
    
    dic_dir = Path("dicionarios")

    if not dic_dir.exists():
        st.info("A pasta 'algoritmos/' ainda está vazia.")
    else:
        
        py_files = list(dic_dir.glob("*.py"))
        md_files = list(dic_dir.glob("*.md"))
        
        if not py_files and not md_files:
            st.info("Em breve teremos conteúdo para compartilhar!")
        
        # ---------- SEÇÃO DE MARKDOWN ----------    
        if md_files:
            st.markdown("## 📄 Documentação em Markdown")    
            for arquivo_md in dic_dir.glob("*.md"):
                with st.expander(arquivo_md.name):
                    conteudo_md = arquivo_md.read_text(encoding="utf-8")
                    st.markdown(conteudo_md)
        
        # ---------- SEÇÃO DE ARQUIVOS PYTHON ----------  
        if py_files:       
            st.markdown("## 📜 Arquivos encontrados")
            for arquivo in dic_dir.glob("*.py"):
                with st.expander(arquivo.name):
                    conteudo = arquivo.read_text(encoding="utf-8")
                    st.code(conteudo, language="python")
        else:
            st.info("Nenhum arquivo Python criado até o momento.")

# ===============================
# Footer
# ===============================
footer()