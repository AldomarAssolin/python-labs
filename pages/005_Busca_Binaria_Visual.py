import streamlit as st
import time
from ui.sidebar import render_sidebar   # se você já estiver usando
from ui.style import styles             # se tiver função de estilos

# aplica estilos globais (se você tiver)
try:
    st.markdown(styles(), unsafe_allow_html=True)
except Exception:
    pass

# sidebar padrão do Python Labs
try:
    render_sidebar()
except Exception:
    pass

st.title("🔍 Visualizador de Busca Binária")
st.write(
    """
    Nesta página você pode **ver passo a passo** como a busca binária funciona.
    A lista é ordenada e, a cada passo, o algoritmo divide o intervalo pela metade.
    """
)

# --- configuração da lista ---
st.markdown("### ⚙️ Configuração")

tamanho = st.slider("Tamanho da lista (1 até N)", min_value=10, max_value=1000, value=30, step=10)
lista = list(range(1, tamanho + 1))

item = st.number_input(
    "Número para buscar na lista",
    min_value=1,
    max_value=tamanho,
    value=tamanho // 2
)

st.write(f"Lista: 1 até {tamanho}")

from typing import List, Tuple, Any, Dict

def busca_binaria_com_passos(lista, item):
    passos = []
    baixo = 0
    alto = len(lista) - 1
    iteracao = 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == item:
            passos.append({
                "iteração": iteracao,
                "baixo": baixo,
                "alto": alto,
                "meio": meio,
                "chute": chute,
                "decisão": "encontrado ✅"
            })
            return meio, passos

        if chute > item:
            passos.append({
                "iteração": iteracao,
                "baixo": baixo,
                "alto": alto,
                "meio": meio,
                "chute": chute,
                "decisão": "chute > item → vai para esquerda"
            })
            alto = meio - 1
        else:
            passos.append({
                "iteração": iteracao,
                "baixo": baixo,
                "alto": alto,
                "meio": meio,
                "chute": chute,
                "decisão": "chute < item → vai para direita"
            })
            baixo = meio + 1

        iteracao += 1

    return None, passos

# Função para mostrar os passos animados
def mostrar_passos_animados(passos):
    placeholder = st.empty()

    for passo in passos:
        placeholder.markdown(
            f"""
            ### 🔎 Passo {passo['iteração']}
            - **Baixo:** {passo['baixo']}
            - **Alto:** {passo['alto']}
            - **Meio:** {passo['meio']}
            - **Chute:** {passo['chute']}
            - **Decisão:** {passo['decisão']}
            """
        )
        time.sleep(1)  # Delay de 1 segundo entre os passos

    st.success("✔ Animação concluída!")


if st.button("▶ Executar busca binária"):
    indice, passos = busca_binaria_com_passos(lista, item)  # 1) calcula

    st.markdown("### ▶ Animação da busca")
    mostrar_passos_animados(passos)                         # 2) anima

    if indice is None:
        st.error(f"Item {item} **não foi encontrado** na lista.")
    else:
        st.success(f"Item {item} encontrado no índice {indice} (posição {indice + 1} na lista).")

    st.markdown("### 📊 Passo a passo")
    st.table(passos)
else:
    st.info("Configure a lista e clique em **Executar busca binária** para ver os passos.")

