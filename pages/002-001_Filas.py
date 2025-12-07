"""
Docstring for pages.002-001_Listas_Filas

Utilizando Listas como Filas em Python
Simulando atendimento em uma fila de banco

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
st.markdown('<div class="big-title">📋 Utilizando Listas como Filas em Python</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Simulando atendimento em uma fila de banco</div>',
    unsafe_allow_html=True,
)

st.write(
    """
Neste exemplo, vamos simular o atendimento em uma fila de banco utilizando listas em Python.
A ideia é demonstrar como podemos adicionar clientes à fila e atendê-los na ordem correta (FIFO - First In, First Out).
""" 
)

# ---- CÓDIGO DE EXEMPLO ----
code_snippet = '''
# Função para adicionar um cliente à fila
def adicionar_cliente(fila, cliente):

    fila.append(cliente)
    print(f"Cliente {cliente} adicionado à fila.")
    
# Função para atender o próximo cliente na fila
def atender_cliente(fila):
    if len(fila) == 0:
        print("Nenhum cliente na fila.")
        return None
    cliente_atendido = fila.pop(0)
    print(f"Cliente {cliente_atendido} atendido.")
    return cliente_atendido
# Exemplo de uso
fila_banco = [] 
adicionar_cliente(fila_banco, "Cliente 1")
adicionar_cliente(fila_banco, "Cliente 2")
adicionar_cliente(fila_banco, "Cliente 3")
atender_cliente(fila_banco)
atender_cliente(fila_banco)
atender_cliente(fila_banco)
atender_cliente(fila_banco)
'''
display_code_snippet(code_snippet)
st.write(
    """
No código acima, definimos duas funções: `adicionar_cliente` para adicionar um cliente à fila e `atender_cliente` para atender o próximo cliente na fila.
Utilizamos uma lista chamada `fila_banco` para representar a fila de clientes.
Adicionamos três clientes à fila e os atendemos na ordem correta.
"""
)

st.markdown("---")

st.markdown("#### Próximos passos")
st.write(
    """
Você pode expandir este exemplo implementando funcionalidades adicionais, como:
- Visualizar a fila atual de clientes.
- Implementar prioridades para certos clientes.
- Simular tempos de atendimento diferentes para cada cliente.
"""
)

st.markdown("---")

st.markdown('<div class="section-title">🏠 Voltar para a página inicial</div>', unsafe_allow_html=True)
st.page_link("Home.py", label="Home", icon="🏠")

st.markdown("---")
st.markdown('<div class="section-title">📚 Outras páginas de estudo</div>', unsafe_allow_html=True)
st.page_link("pages/002_Listas.py", label="Listas", icon="📈")
# st.page_link("pages/002-002_Dicionarios.py", label="Dicionários", icon="📊")

st.markdown("---")
st.markdown('<div class="footer">Feito com ❤️ por Aldomar "Manex" Assolin</div>', unsafe_allow_html=True)

# Fim do arquivo pages/002-001_Listas_Filas.py