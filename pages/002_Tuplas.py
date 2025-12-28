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
    page_title="Python Labs - Tuplas",
    page_icon="🟦",
    layout="wide",
)

# ---- CONTEÚDO DA PÁGINA ----
# ------ Titulo ------
st.title("🟦 Tuplas em Python")
st.subheader("Estruturas imutáveis, seguras e performáticas")
st.markdown(">Veja o código na aba ``📚 Docs`` no arquivo `exemplos.py`.")
st.markdown("""---""")


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

    st.subheader("📚 Documentação sobre Tuplas em Python")
    st.markdown("### Este módulo faz parte do **Python Labs** e tem como foco entender e praticar o uso de **tuplas em Python**.")

    st.markdown(
        """

    Tuplas são parecidas com listas, mas têm uma característica muito importante:

    > 🔒 **Imutáveis** – depois de criadas, **não podem ser alteradas**.

    Use esta página como um laboratório interativo para:
    - entender a diferença entre tupla e lista  
    - visualizar exemplos executados  
    - reforçar conceitos com exercícios guiados  
    """
    )

    st.divider()


    st.header("📘 Conceitos fundamentais sobre tuplas")

    st.markdown(
            """
    ### 🧠 O que é uma tupla?

    Uma **tupla** é uma estrutura de dados **ordenada**, **indexada** e **imutável**.

    Isso significa:

    - Você pode acessar elementos por índice ✅  
    - A ordem é preservada ✅  
    - Você **não pode** adicionar, remover ou alterar elementos depois de criada ❌  

    ---

    ### 🔍 Comparação rápida: Lista x Tupla

    | Característica | Lista (`list`) | Tupla (`tuple`) |
    |----------------|----------------|-----------------|
    | Mutável        | ✅ Sim         | ❌ Não          |
    | Ordenada       | ✅ Sim         | ✅ Sim          |
    | Usa colchetes  | ✅ `[]`        | ❌              |
    | Usa parênteses | ❌            | ✅ `()`         |
    | Mais rápida    | ❌            | ✅ Em geral     |
    | Pode ser chave de dicionário | ❌ Não | ✅ Sim |

    ---

    ### 🧩 Quando faz sentido usar tupla?

    Use tuplas quando:

    - os dados **não devem ser modificados**  
    - você quer **indicar claramente** que aquilo é fixo (semântico)  
    - você precisa usar como **chave em um dicionário**  
    - precisa de **desempenho um pouco melhor** em leituras  

    Exemplos de uso típico:

    - coordenadas: `(x, y)`  
    - retorno de múltiplos valores de uma função: `(status, mensagem)`  
    - configurações estáticas  
    - registros imutáveis (ex.: `("Maria", 35, "Analista")`)  
    """
        )

    st.info(
        "💡 Dica de desenvolvedor: "
        "usar tupla em vez de lista deixa o código mais expressivo quando você quer deixar claro que os dados não devem ser alterados."
    )

# ===============================
# Aba 2 - Exemplos Práticos
# ===============================
with tab_exemplos:
    st.header("🧪 Exemplos práticos de tuplas")

    st.markdown("Abaixo estão alguns exemplos **executáveis** que reforçam os conceitos de tuplas.")

    # Exemplo 1 – Acesso básico
    with st.expander("EX. 1 – Criar tupla e acessar primeiro/último elemento"):
        tupla_exemplo = (10, 20, 30, 40, 50)
        st.write("`tupla_exemplo = (10, 20, 30, 40, 50)`")
        st.write("**Tupla completa:**", tupla_exemplo)
        st.write("**Primeiro elemento (`[0]`):**", tupla_exemplo[0])
        st.write("**Último elemento (`[-1]`):**", tupla_exemplo[-1])

    # Exemplo 2 – Imutabilidade
    with st.expander("EX. 2 – Tentando modificar uma tupla (imutabilidade)"):
        st.write("Tentando executar: `tupla_exemplo[1] = 25`")
        try:
            tupla_exemplo = (10, 20, 30, 40, 50)
            # Força um erro de imutabilidade
            tupla_exemplo[1] = 25  # type: ignore
        except TypeError as e:
            st.error(f"❌ Erro ao tentar modificar a tupla: {e}")

        st.markdown(
                """
    A mensagem de erro mostra que **objetos do tipo `tuple` não suportam atribuição de item**, 
    ou seja, você não pode alterar um elemento diretamente.
    """
            )

    # Exemplo 3 – Desempacotamento
    with st.expander("EX. 3 – Desempacotando valores da tupla"):
        tupla_exemplo = (10, 20, 30, 40, 50)
        a, b, c, d, e = tupla_exemplo
        st.write("`a, b, c, d, e = (10, 20, 30, 40, 50)`")
        st.write(f"a = {a}, b = {b}, c = {c}, d = {d}, e = {e}")
        st.info("Esse padrão é muito usado para retornar vários valores de uma função.")

    # Exemplo 4 – Concatenação
    with st.expander("EX. 4 – Concatenando tuplas"):
        tupla1 = (1, 2, 3)
        tupla2 = (4, 5, 6)
        tupla_concatenada = tupla1 + tupla2
        st.write("`tupla1 = (1, 2, 3)`")
        st.write("`tupla2 = (4, 5, 6)`")
        st.write("`tupla_concatenada = tupla1 + tupla2`")
        st.write("**Resultado:**", tupla_concatenada)

    # Exemplo 5 – Verificando existência com `in`
    with st.expander("EX. 5 – Verificando se um elemento existe na tupla"):
        contatos = ("Maria", "João", "Ana", "Pedro")
        st.write("`contatos = ('Maria', 'João', 'Ana', 'Pedro')`")
        nome_busca = st.text_input("Digite um nome para buscar na tupla:", "Ana")
        if nome_busca:
            if nome_busca in contatos:
                st.success(f"O nome **{nome_busca}** existe na tupla de contatos.")
            else:
                st.warning(f"O nome **{nome_busca}** **não** existe na tupla de contatos.")

    # Exemplo 6 – count()
    with st.expander("EX. 6 – Contando ocorrências de um valor"):
        tupla_numeros = (1, 2, 3, 2, 4, 2, 5)
        numero_contar = st.number_input(
            "Número para contar na tupla (1–5):",
            min_value=1,
            max_value=5,
            value=2,
            step=1,
        )
        ocorrencias = tupla_numeros.count(numero_contar)
        st.write("Tupla:", tupla_numeros)
        st.info(f"O número **{numero_contar}** aparece **{ocorrencias}** vez(es) na tupla.")

    # Exemplo 7 – Conversão lista ↔ tupla
    with st.expander("EX. 7 – Convertendo lista em tupla e tupla em lista"):
        lista_exemplo = [100, 200, 300]
        tupla_convertida = tuple(lista_exemplo)
        tupla_exemplo = (10, 20, 30, 40, 50)
        lista_convertida = list(tupla_exemplo)

        st.write("Lista original:", lista_exemplo)
        st.write("Tupla convertida da lista:", tupla_convertida)
        st.write("Tupla original:", tupla_exemplo)
        st.write("Lista convertida da tupla:", lista_convertida)

        st.info(
            "Estratégia comum: converter tupla em lista para editar, depois voltar para tupla para garantir imutabilidade."
        )

    # Exemplo 8 – enumerate()
    with st.expander("EX. 8 – Percorrendo tupla com índices (enumerate)"):
        tupla_exemplo = (10, 20, 30, 40, 50)
        st.write("`tupla_exemplo = (10, 20, 30, 40, 50)`")
        st.write("Índices e valores:")
        for indice, valor in enumerate(tupla_exemplo):
            st.write(f"• Índice: {indice} → Valor: {valor}")

    # Exemplo 9 – Tupla aninhada
    with st.expander("EX. 9 – Tupla aninhada e acesso interno"):
        tupla_aninhada = (1, 2, (3, 4, 5), 6)
        st.write("`tupla_aninhada = (1, 2, (3, 4, 5), 6)`")
        st.write("Elemento interno acessado com `[2][1]` (ou seja, 4):")
        elemento_interno = tupla_aninhada[2][1]
        st.success(f"Elemento interno: {elemento_interno}")

    # Exemplo 10 – Contagem manual
    with st.expander("EX. 10 – Contando itens da tupla manualmente"):
        tupla_exemplo = (10, 20, 30, 40, 50)
        contador = 0
        for item in tupla_exemplo:
            contador += 1
        st.write("Tupla:", tupla_exemplo)
        st.write("Número de itens (usando loop, sem `len()`):", contador)

# ===============================
# Aba 3 - Documentação
# ===============================
with tab_docs:
    st.header("📚 Exercícios guiados com tuplas")
    
    tuplas_dir = Path("tuplas")

    if not tuplas_dir.exists():
        st.info("A pasta 'tuplas/' ainda está vazia.")
    else:
        
        py_files = list(tuplas_dir.glob("*.py"))
        md_files = list(tuplas_dir.glob("*.md"))

        # Se ambas vazias
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
            st.markdown("## 📜 Arquivos Python")
            for arquivo_py in py_files:
                with st.expander(arquivo_py.name):
                    conteudo_py = arquivo_py.read_text(encoding="utf-8")
                    st.code(conteudo_py, language="python")
        else:
            st.info("Nenhum arquivo Python criado até o momento.")

# ===============================
# Footer
# ===============================
footer()