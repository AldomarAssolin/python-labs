"""
Docstring for pages.002-001_Listas_Filas

Utilizando Listas como Filas em Python
Simulando atendimento em uma fila de banco com senhas
"""

from pathlib import Path
import streamlit as st
from ui.style import styles
from ui.sidebar import render_sidebar
from ui.code_display import display_code_snippet

# ---- CONFIGURAÇÕES DA PÁGINA ----
st.set_page_config(
    page_title="Listas como Filas",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---- SIDEBAR ----
render_sidebar()

# ---- ESTILO BÁSICO (CSS SIMPLES) ----
styles()

# ---- CABEÇALHO DA PÁGINA ----
st.markdown(
    '<div class="big-title">📋 Utilizando Listas como Filas em Python</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="subtitle">Simulando atendimento em uma fila de banco com senhas</div>',
    unsafe_allow_html=True,
)

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
    st.write(
        """
    Neste exemplo, vamos simular o atendimento em uma fila de banco utilizando **listas em Python**.
    Cada cliente recebe uma **senha** de acordo com o tipo de atendimento (Normal, Prioritário ou Caixa) e entra na fila em ordem de chegada (FIFO - *First In, First Out*).
    """
    )

    # ---- CÓDIGO DE EXEMPLO (VERSÃO TERMINAL / LÓGICA) ----
    code_snippet = '''
    menu_options = {
        1: "Normal",
        2: "Prioritario",
        3: "Caixa"
    }

    tipo_atendimento = {
        "Normal": "NOR",
        "Prioritario": "PRI",
        "Caixa": "CAX"
    }

    fila = []
    contador_senhas = {
        "Normal": 0,
        "Prioritario": 0,
        "Caixa": 0
    }

    def gerar_senha(tipo: str) -> str:
        """Gera uma senha no formato TIPOnnn, ex: NOR001, PRI005."""
        contador_senhas[tipo] += 1
        return f"{tipo_atendimento[tipo]}{contador_senhas[tipo]:03d}"

    def adicionar_cliente(fila, tipo):
        senha = gerar_senha(tipo)
        fila.append({"tipo": tipo, "senha": senha})
        print(f"Cliente adicionado: {tipo} - Senha {senha}")

    def atender_cliente(fila):
        if not fila:
            print("Nenhum cliente na fila.")
            return None
        cliente = fila.pop(0)  # FIFO
        print(f"Atendendo: {cliente['tipo']} - Senha {cliente['senha']}")
        return cliente
    '''
    display_code_snippet(code_snippet)

    st.write(
        """
    No código acima, definimos:
    - Um **dicionário** com os tipos de atendimento (`Normal`, `Prioritario`, `Caixa`) e seus códigos.
    - Uma lista chamada `fila` que guarda os clientes na ordem de chegada.
    - A função `gerar_senha`, que cria senhas como `NOR001`, `PRI002`, etc.
    - As funções `adicionar_cliente` e `atender_cliente`, que controlam a fila.
    """
    )

    st.markdown("---")
    
    st.markdown("#### Próximos passos")
    st.write(
        """
    Você pode expandir este exemplo implementando funcionalidades adicionais, como:
    - Diferentes regras de prioridade entre os tipos de atendimento.
    - Tempo estimado de espera para cada cliente.
    - Relatórios com a quantidade de atendimentos por tipo.
    """
    )

    st.markdown("---")
    st.markdown(
        '<div class="section-title">🏠 Voltar para a página inicial</div>',
        unsafe_allow_html=True,
    )
    st.page_link("Home.py", label="Home", icon="🏠")

    st.markdown("---")
    st.markdown(
        '<div class="section-title">📚 Outras páginas de estudo</div>',
        unsafe_allow_html=True,
    )
    st.page_link("pages/002_Listas.py", label="Listas", icon="📈")

    st.markdown("---")
    st.markdown(
        '<div class="footer">Feito com ❤️ por Aldomar "Manex" Assolin</div>',
        unsafe_allow_html=True,
    )

# ===============================
# Aba 2 - Exemplos Práticos
# ===============================
with tab_exemplos: 
    
    # ---- EXEMPLO INTERATIVO SIMPLES (OPCIONAL NA MESMA PÁGINA) ----
    st.markdown("#### Simulação simples de fila de atendimento")

    # estado da fila na sessão
    if "fila_banco" not in st.session_state:
        st.session_state.fila_banco = []
    if "contador_senhas" not in st.session_state:
        st.session_state.contador_senhas = {
            "Normal": 0,
            "Prioritario": 0,
            "Caixa": 0,
        }

    menu_options = {
        "Normal": "NOR",
        "Prioritario": "PRI",
        "Caixa": "CAX",
    }

    col1, col2 = st.columns(2)

    with col1:
        tipo_escolhido = st.selectbox(
            "Tipo de atendimento:",
            list(menu_options.keys()),
        )
        if st.button("➕ Adicionar cliente à fila"):
            st.session_state.contador_senhas[tipo_escolhido] += 1
            prefixo = menu_options[tipo_escolhido]
            num = st.session_state.contador_senhas[tipo_escolhido]
            senha = f"{prefixo}{num:03d}"
            st.session_state.fila_banco.append(
                {"tipo": tipo_escolhido, "senha": senha}
            )
            st.success(f"Cliente adicionado: {tipo_escolhido} - Senha {senha}")

    with col2:
        if st.button("▶️ Atender próximo cliente"):
            if st.session_state.fila_banco:
                cliente = st.session_state.fila_banco.pop(0)
                st.info(
                    f"Atendendo: {cliente['tipo']} - Senha {cliente['senha']}"
                )
            else:
                st.warning("Nenhum cliente na fila.")

    st.markdown("##### Fila atual")
    if st.session_state.fila_banco:
        for i, cli in enumerate(st.session_state.fila_banco, start=1):
            st.write(f"{i}. {cli['tipo']} - **{cli['senha']}**")
    else:
        st.write("Fila vazia no momento.")

    st.markdown("---")

    st.write(
        """
    No código acima, definimos:
    - Um **dicionário** com os tipos de atendimento (`Normal`, `Prioritario`, `Caixa`) e seus códigos.
    - Uma lista chamada `fila` que guarda os clientes na ordem de chegada.
    - A função `gerar_senha`, que cria senhas como `NOR001`, `PRI002`, etc.
    - As funções `adicionar_cliente` e `atender_cliente`, que controlam a fila.
    """
    )

    st.markdown("---")


# ===============================
# Aba 3 - Documentação
# ===============================
with tab_docs:

    lis_dir = Path("listas")

    if not lis_dir.exists():
        st.info("A pasta 'algoritmos/' ainda está vazia.")
    else:
        
        py_files = list(lis_dir.glob("*.py"))
        md_files = list(lis_dir.glob("*.md"))
        
        if not py_files and not md_files:
            st.info("Em breve teremos conteúdo para compartilhar!")
        
        # ---------- SEÇÃO DE MARKDOWN ----------    
        if md_files:
            st.markdown("## 📄 Documentação em Markdown")    
            for arquivo_md in lis_dir.glob("*.md"):
                with st.expander(arquivo_md.name):
                    conteudo_md = arquivo_md.read_text(encoding="utf-8")
                    st.markdown(conteudo_md)
        
        # ---------- SEÇÃO DE ARQUIVOS PYTHON ----------  
        if py_files:       
            st.markdown("## 📜 Arquivos encontrados")
            for arquivo in lis_dir.glob("*.py"):
                with st.expander(arquivo.name):
                    conteudo = arquivo.read_text(encoding="utf-8")
                    st.code(conteudo, language="python")
        else:
            st.info("Nenhum arquivo Python criado até o momento.")
            
    