# pages/003_Algoritmos.py
import streamlit as st
from pathlib import Path
import time
from ui.navbar import navbar
from ui.sidebar import render_sidebar
from ui.style import styles
from ui.footer import footer
from ui.header import header

# ===============================
# CONFIGURAÇÕES DA PÁGINA
# ===============================

st.set_page_config(
    page_title="Algoritmos",
    page_icon="〽",
    layout="wide",
)

# ---- SIDEBAR ----
render_sidebar()

# ---- ESTILO BÁSICO (CSS SIMPLES) ----
styles()

# ---- CABEÇALHO ----
header()

# ---- Nav ----
navbar()

# ---- CONTEÚDO DA PÁGINA ----
# ------ Titulo ------
st.title("〽 Algoritmos – Python Labs")
st.subheader("Este módulo registra minha evolução em lógica, algoritmos, Python e Inteligência Artificial.")
st.markdown("""
            >Aqui estudo, implemento e documento algoritmos essenciais para desenvolver meu raciocínio lógico e minha base como programador. 
            >Cada arquivo representa um capítulo do meu aprendizado — simples, direto e prático.
            
            ---
            """)

# ===============================
# Abas principais
# ===============================
tab_principal, tab_exemplos, tab_docs = st.tabs(
    ["📘 Principal", "🧪 Exemplos Práticos", "📚 Docs"]
)

# ===============================
# Aba 1 - Conceitos
# ===============================
with tab_principal:
    st.markdown("""

## 🎯 Objetivo deste módulo
- Entender o funcionamento dos principais algoritmos
- Praticar lógica de programação de forma consistente
- Criar bases sólidas para machine learning, análise de dados e IA
- Aprender a medir complexidade e fazer escolhas mais inteligentes ao programar

---

## 📚 Fontes de estudo
- *Entendendo Algoritmos* — Aditya Bhargava  
- Materiais complementares do meu cronograma de IA

---

## 🧩 Conteúdos que serão implementados aqui
✅ Busca linear      
✅ Busca binária     
⬜ Ordenação por seleção      
⬜ Recursão      
⬜ Dividir para conquistar   
⬜ Tabelas hash      
⬜ Grafos (conceitos iniciais)    
⬜ BFS / Dijkstra (conceitos introdutórios)      

Cada algoritmo terá:
- Implementação em Python  
- Comentários didáticos  
- Uma breve explicação no início do arquivo  
- Opcionalmente um `.md` explicando o raciocínio  

---

## 🚀 Evolução contínua
Este módulo cresce conforme estudo, pratico e reviso.
Ele demonstra meu compromisso com uma base técnica sólida e com a evolução consistente como desenvolvedor.

                """)
# ===============================
# Aba 2 - Exemplos Práticos
# ===============================
with tab_exemplos: 
    # ---------- EXEMPLO: Busca Binária Visual ----------
    st.title("🔍 Visualizador de Busca Binária")
    st.write(
        """
        Nesta seção você pode **ver passo a passo** como a busca binária funciona.
        A lista é ordenada e, a cada passo, o algoritmo divide o intervalo pela metade.
        """
    )
    
    st.markdown(">Veja o código na aba ``📚 Docs`` no arquivo `busca_binaria.py`.")
    st.markdown("---")

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

# ===============================
# Aba 3 - Documentação
# ===============================
with tab_docs:

    alg_dir = Path("algoritmos")

    if not alg_dir.exists():
        st.info("A pasta 'algoritmos/' ainda está vazia.")
    else:
        
        py_files = list(alg_dir.glob("*.py"))
        md_files = list(alg_dir.glob("*.md"))
        
        if not py_files and not md_files:
            st.info("Em breve teremos conteúdo para compartilhar!")
        
        # ---------- SEÇÃO DE MARKDOWN ----------    
        if md_files:
            st.markdown("## 📄 Documentação em Markdown")    
            for arquivo_md in alg_dir.glob("*.md"):
                with st.expander(arquivo_md.name):
                    conteudo_md = arquivo_md.read_text(encoding="utf-8")
                    st.markdown(conteudo_md)
        
        # ---------- SEÇÃO DE ARQUIVOS PYTHON ----------  
        if py_files:       
            st.markdown("## 📜 Arquivos encontrados")
            for arquivo in alg_dir.glob("*.py"):
                with st.expander(arquivo.name):
                    conteudo = arquivo.read_text(encoding="utf-8")
                    st.code(conteudo, language="python")
        else:
            st.info("Nenhum arquivo Python criado até o momento.")
            
# ===============================
# Footer
# ===============================
footer()
