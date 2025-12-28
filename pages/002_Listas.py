# pages/002_Listas.py
import streamlit as st
from pathlib import Path
import pandas as pd
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
    page_title="Listas",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---- CONTEÚDO DA PÁGINA ----
# ------ Titulo ------
st.title("📋 Listas em Python")
st.write(
    """
Neste exemplo, vamos simular o atendimento em uma fila de banco utilizando **listas em Python**.
Cada cliente recebe uma **senha** de acordo com o tipo de atendimento (Normal, Prioritário ou Caixa) e entra na fila em ordem de chegada (FIFO - *First In, First Out*).
"""
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
    st.markdown("""

# 🧠 Python Labs – Módulo de **Listas em Python**  
### Exercícios progressivos • Lógica • Estruturas de Dados • Algoritmos

![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Categoria](https://img.shields.io/badge/Estudos-Lógica%20de%20Programação-orange)


---

## 🔗 Navegação Rápida
- [Objetivo](#🎯-objetivo-do-módulo)
- [Estrutura dos Arquivos](#📁-estrutura-dos-arquivos)
- [Conteúdo por Nível](#📘-conteúdo-por-nível)
- [Como Executar](#🚀-como-executar)
- [Por que estudar listas assim?](#🧠-por-que-estudar-listas-dessa-forma)
- [Roadmap de Estudos](#📈-roadmap-dos-próximos-módulos)
- [Autor](#👨‍💻-autor)

---

## 🎯 Objetivo do Módulo
Aprender e dominar **listas em Python** por meio de exercícios práticos distribuídos em quatro níveis:

| Nível | Foco |
|------|------|
| 🟩 **Básico** | Fundamentos da estrutura de lista |
| 🟦 **Intermediário** | Lógica aplicada e manipulação de dados |
| 🟨 **Aplicação** | Problemas reais, matrizes e funções utilitárias |
| 🟥 **Avançado** | Algoritmos, slicing manual, zip manual, ordenação |

---

## 📁 Estrutura dos Arquivos

```
listas/
├── lista_exercicios_basicos.py
├── lista_exercicios_intermediario.py
├── lista_exercicios_aplicacao.py
└── lista_exercicios_avancado.py
```

---

## 📘 Conteúdo por Nível

### 🟩 **1. lista_exercicios_basicos.py**
> _Fundamentos essenciais_

- Criação e acesso a listas  
- Inserção e remoção de itens  
- Contagem manual  
- Acesso por índices  
- Inversão manual da lista  
- Estruturas simples para fixação

---

### 🟦 **2. lista_exercicios_intermediario.py**
> _Pensamento algorítmico_

- Filtragem de elementos  
- Soma e agregação  
- Maior/menor sem funções nativas  
- Map e transformação (ex.: quadrados)  
- Combinação de listas sem `+`

---

### 🟨 **3. lista_exercicios_aplicacao.py**
> _Resolução de problemas reais_

- Remoção de duplicados  
- Contagem de ocorrências  
- Busca manual (True/False)  
- Criação de funções utilitárias  
- Matrizes (listas de listas)  
- Impressão de diagonais

---

### 🟥 **4. lista_exercicios_avancado.py**
> _Algoritmos, eficiência e domínio da linguagem_

- Ordenação manual (Bubble Sort)  
- Zip manual (intercalamento de listas)  
- Geração de números aleatórios  
- Filtros avançados  
- Implementação manual do slicing (`lista[início:fim]`)  
- Controle profundo de índices e loops aninhados  

---

## 🚀 Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/python-labs.git
```

Entre na pasta:

```bash Copiar código
cd python-labs/listas
```
Execute qualquer arquivo:

```bash Copiar código
python lista_exercicios_avancado.py
```
💡 Recomendado usar ambiente virtual (venv) para estudos organizados.

🧠 Por que estudar listas dessa forma?
>Listas são a espinha dorsal do Python.

- Quase tudo em Python gira em torno de listas ou estruturas derivadas:

- respostas de APIs → listas de dicionários

- JSON → listas e dicionários

- Machine Learning → listas/arrays de vetores

- Manipulação de arquivos e logs → listas

- ETL, automações e pipelines → listas

Dominar listas = abrir portas para:

- Dicionários avançados

- Funções poderosas

- Estruturas de IA

- Data structures

- Desenvolvimento backend (Flask, FastAPI)

Além disso, exercícios avançados como ordenação e slicing manual treinam:

- controle algorítmico

- lógica de alto nível

- raciocínio para entrevistas técnicas

- independência de ferramentas nativas

📈 Roadmap dos Próximos Módulos
| Módulo                                 | Status         |
|----------------------------------------|----------------|
| ✔️ Listas                              | Concluído      |
| 🔜 Dicionários                         | Em andamento   |
| 🔜 Funções (básico → avançado)         | Planejado      |
| 🔜 Tuplas & Sets                       | Planejado      |
| 🔜 Estruturas Avançadas                | Planejado      |
| 🔜 Mini-projetos (sistemas completos)  | Planejado      |

---

## 👨‍💻 Autor  

**Aldomar Assolin – Manex**  
Desenvolvedor em formação • ADS • Lógica • Python • Backend • IA  

_Apaixonado por aprendizado constante e evolução profissional._

⭐ Se este módulo te ajudou, deixe uma estrela no repositório!

                
                """)
# ===============================
# Aba 2 - Exemplos Práticos
# ===============================
with tab_exemplos: 
    
    st.header("🛒 Lista de Compras (CRUD simples)")

    st.markdown(
        "Exemplo de como transformar um menu com `input()` no terminal "
        "em uma interface web usando formulários e tabela interativa."
    )

    # inicializa DataFrame na sessão
    if "lista_compras" not in st.session_state:
        st.session_state.lista_compras = pd.DataFrame(
            {"Produto": [], "Quantidade": [], "unidade": []}
        )

    df = st.session_state.lista_compras

    tab_inserir, tab_atualizar, tab_remover, tab_lista = st.tabs(
        ["➕ Inserir", "✏️ Atualizar", "🗑️ Remover", "📋 Exibir lista"]
    )

    # 1 - Inserir item
    with tab_inserir:
        st.subheader("Inserir novo item")
        with st.form("form_inserir"):
            produto = st.text_input("Produto")
            quantidade = st.text_input("Quantidade")
            
            # Unidades de medida comuns
            opcoes_unidade = ["un", "kg", "g", "dz", "L", "mL", "pct", "cx", "Outro"]
            unidade_sel = st.selectbox("Unidade", options=opcoes_unidade)

            if unidade_sel == "Outro":
                unidade = st.text_input("Digite a unidade:")
            else:
                unidade = unidade_sel
                
            submit_ins = st.form_submit_button("Adicionar")

        if submit_ins:
            if not produto:
                st.error("Informe o nome do produto.")
            else:
                novo_item = pd.DataFrame(
                    {"Produto": [produto], "Quantidade": [quantidade], "unidade": [unidade]}
                )
                st.session_state.lista_compras = pd.concat(
                    [st.session_state.lista_compras, novo_item],
                    ignore_index=True,
                )
                st.success(f"{produto} adicionado à lista.")

    # 2 - Atualizar item
    with tab_atualizar:
        st.subheader("Atualizar item")
        if df.empty:
            st.info("A lista de compras está vazia.")
        else:
            produtos = df["Produto"].tolist()
            produto_sel = st.selectbox("Escolha o produto para atualizar:", produtos)
            nova_qtd = st.text_input("Nova quantidade")
            nova_unid = st.text_input("Nova unidade")
            if st.button("Atualizar"):
                mask = st.session_state.lista_compras["Produto"] == produto_sel
                if nova_qtd:
                    st.session_state.lista_compras.loc[mask, "Quantidade"] = nova_qtd
                if nova_unid:
                    st.session_state.lista_compras.loc[mask, "unidade"] = nova_unid
                st.success(f"{produto_sel} atualizado na lista.")

    # 3 - Remover item
    with tab_remover:
        st.subheader("Remover item")
        if df.empty:
            st.info("A lista de compras está vazia.")
        else:
            produtos = df["Produto"].tolist()
            produto_rem = st.selectbox("Escolha o produto para remover:", produtos)
            if st.button("Remover"):
                st.session_state.lista_compras = st.session_state.lista_compras[
                    st.session_state.lista_compras["Produto"] != produto_rem
                ]
                st.success(f"{produto_rem} removido da lista.")

    # 4 - Exibir lista
    with tab_lista:
        st.subheader("Lista de Compras")
        if st.session_state.lista_compras.empty:
            st.info("A lista de compras está vazia.")
        else:
            st.dataframe(st.session_state.lista_compras, use_container_width=True)

# ===============================
# Aba 3 - Documentação
# ===============================
with tab_docs:

    listas_dir = Path("listas")

    if not listas_dir.exists():
        st.info("A pasta 'listas/' ainda está vazia.")
    else:
        
        py_files = list(listas_dir.glob("*.py"))
        md_files = list(listas_dir.glob("*.md"))
        
        if not py_files and not md_files:
            st.info("Em breve teremos conteúdo para compartilhar!")
        
        # ---------- SEÇÃO DE MARKDOWN ----------
        if md_files:
            st.markdown("## 📄 Documentação em Markdown")    
            for arquivo_md in md_files:
                with st.expander(arquivo_md.name):
                    conteudo_md = arquivo_md.read_text(encoding="utf-8")
                    st.markdown(conteudo_md)
                
        # ---------- SEÇÃO DE ARQUIVOS PYTHON ----------    
        if py_files:           
            st.markdown("## 📜 Arquivos encontrados")
            for arquivo in py_files:
                with st.expander(arquivo.name):
                    conteudo = arquivo.read_text(encoding="utf-8")
                    st.code(conteudo, language="python")
        else:
            st.info("Nenhum arquivo Python criado até o momento.")

# ===============================
# Footer
# ===============================
footer()            