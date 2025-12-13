# pages/001_Fundamentos.py
import streamlit as st
from pathlib import Path
from datetime import datetime, date
from ui.sidebar import render_sidebar

# ---- SIDEBAR ----
render_sidebar()

# ---- CONTEÚDO DA PÁGINA ----
st.title("🧩 Fundamentos de Python")

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
    st.header("🧩 Fundamentos de Python")
    st.subheader("Conceitos básicos para começar a programar")
    st.markdown("Este documento lista tudo o que preciso estudar e implementar dentro da pasta `fundamentos/`. Cada item será marcado conforme eu avançar. Meu objetivo aqui é dominar a base do Python com exemplos simples, claros e funcionais.")
    
    st.markdown("""


---

## ✅ Estrutura Básica do Python
- [ ] Revisar sintaxe geral do Python  
- [ ] Criar exemplo padrão usando `def main()`  
- [ ] Entrada e saída (`input()` e `print()`)

---

## 🔤 Variáveis e Tipos de Dados
- [ ] Criar exemplos de tipos primitivos (int, float, str, bool)
- [ ] Conversão de tipos (`int()`, `float()`, `str()`)
- [ ] Comentários e boas práticas simples

---

## 🔄 Estruturas de Controle
### Condicionais
- [ ] `if`, `elif`, `else`
- [ ] Operadores lógicos (`and`, `or`, `not`)
- [ ] Comparações (`==`, `!=`, `>=`, etc.)

### Loops
- [ ] `for` com listas e ranges
- [ ] `while` (com controle seguro)
- [ ] `break` e `continue`

---

## 📦 Estruturas de Dados
- [ ] Listas (criação, acesso, métodos)
- [ ] Tuplas (imutabilidade)
- [ ] Dicionários (chave/valor)
- [ ] Sets (conjuntos)

---

## 🧠 Funções
- [ ] Funções simples
- [ ] Parâmetros e retorno
- [ ] Argumentos nomeados
- [ ] Valores padrão
- [ ] Funções dentro de funções
- [ ] `lambda`

---

## 🧱 Introdução à POO
- [ ] Criar primeira classe
- [ ] Atributos e métodos
- [ ] `__init__`
- [ ] Instância de objeto
- [ ] Exercício prático simples

---

## ⚠️ Tratamento de Exceções
- [ ] `try / except`
- [ ] `finally`
- [ ] Trabalhar com erros reais (ex: divisão por zero)

---

## 📁 Manipulação de Arquivos
- [ ] Ler arquivos texto
- [ ] Escrever arquivos
- [ ] `with open()` (context manager)

---

## 🏁 Mini Projetos (Fundamentos)
- [ ] Calculadora simples
- [ ] Sistema básico de cadastro (lista/dicionário)
- [ ] Conversor de temperatura
- [ ] Simulador de lista de compras

---

## 📝 Observações pessoais
> Adicionar aqui descobertas, dificuldades, coisas que quero revisar, e boas práticas aprendidas.

---

## 🔚 Meta deste módulo
Criar uma base sólida para seguir para **Algoritmos** e depois para **Machine Learning**, como no meu cronograma de estudos.


    """)
    
# ===============================
# Aba 2 - Exemplos Práticos
# ===============================
with tab_exemplos:
    st.header("🧾 Exemplo: Cadastro simples")

    st.markdown(
        "Esta seção demonstra o exemplo **criado no arquivo** `user.py` na aba ``docs`` transformando um script de cadastro no terminal "
        "em uma interface web usando Streamlit."
    )

    with st.form("cadastro_form"):
        nome = st.text_input("Primeiro nome")
        sobrenome = st.text_input("Sobrenome")
        nickname = st.text_input("Nickname (sem espaços)")
        data_nasc = st.date_input(
            "Data de nascimento",
            value=date(2000, 1, 1),
            min_value=date(1930, 1, 1),
            max_value=date.today(),
        )

        submitted = st.form_submit_button("Cadastrar")

    if submitted:
        # validações simples
        if " " in nickname:
            st.error("O nickname não pode conter espaços.")
        elif not nome or not sobrenome:
            st.error("Preencha nome e sobrenome.")
        else:
            # normalizações
            nome_fmt = nome.strip().title()
            sobrenome_fmt = (
                sobrenome.strip()
                .title()
                .replace(" De ", " de ")
                .replace(" Da ", " da ")
                .replace(" Dos ", " dos ")
                .replace(" Das ", " das ")
            )

        hoje = date.today()
        idade = hoje.year - data_nasc.year - (
            (hoje.month, hoje.day) < (data_nasc.month, data_nasc.day)
        )

        st.success("Cadastro concluído com sucesso!")

        st.markdown("### ✅ Dados cadastrados")
        st.write(f"**Nome:** {nome_fmt} {sobrenome_fmt}")
        st.write(f"**Nickname:** {nickname}")
        st.write(f"**Data de nascimento:** {data_nasc.strftime('%d/%m/%Y')}  (Idade: {idade} anos)")
        st.write(f"**Data atual:** {hoje.strftime('%d/%m/%Y')}")

        st.markdown("---")
        st.caption("Exemplo de conversão de `input()` no terminal para interface web com Streamlit.")
        
# Calculo Fatorial

def fatorial(n):
    """Calcula o fatorial de n de forma recursiva."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
    
st.title("📚 Cálculo do Fatorial em Python")

numero = st.number_input(
    "Digite um número inteiro não negativo para calcular o fatorial:",
    min_value=0,
    value=5,
    step=1
)

if st.button("Calcular Fatorial"):
    resultado = fatorial(numero)
    st.success(f"O fatorial de {numero} é {resultado}.")
    
st.info("""
O fatorial de um número n (denotado como n!) é o produto de todos os inteiros positivos de 1 até n.
Por definição, o fatorial de 0 é 1 (0! = 1).
O fatorial é amplamente utilizado em matemática, estatística e ciência da computação, especialmente em combinações e permutações.
""")

# Exemplo de uso da função
st.subheader("Exemplos de Fatorial")
exemplos = [0, 1, 5, 7, 10]
for ex in exemplos:
    st.write(f"{ex}! = {fatorial(ex)}") 
    
# ===============================
# Aba 3 - Exercícios Guiados
# ===============================
with tab_docs:
    fundamentos_dir = Path("fundamentos")

    if not fundamentos_dir.exists():
        st.info("A pasta 'fundamentos/' ainda está vazia.")
    else:
        
        py_files = list(fundamentos_dir.glob("*.py"))
        md_files = list(fundamentos_dir.glob("*.md"))

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
            

