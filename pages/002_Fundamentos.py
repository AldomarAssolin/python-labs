# pages/001_Fundamentos.py
import streamlit as st
from pathlib import Path
from datetime import datetime, date
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
    page_title="Fundamentos",
    page_icon="🧩",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---- CONTEÚDO DA PÁGINA ----
# ------ Titulo ------
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

## 🔃 Estrutura Básica do Python
 ✅ Revisar sintaxe geral do Python  
 ✅ Criar exemplo padrão usando `def main()`  
 ✅ Entrada e saída (`input()` e `print()`)

---

## 🔤 Variáveis e Tipos de Dados
 ✅ Criar exemplos de tipos primitivos (int, float, str, bool)  
 ✅ Conversão de tipos (`int()`, `float()`, `str()`)    
 ✅ Comentários e boas práticas simples 

---

## 🔄 Estruturas de Controle
### Condicionais
 ✅ `if`, `elif`, `else`    
 ✅ Operadores lógicos (`and`, `or`, `not`)     
 ✅ Comparações (`==`, `!=`, `>=`, etc.)        

### Loops
 ✅ `for` com listas e ranges   
 ✅ `while` (com controle seguro)   
 ✅ `break` e `continue`    

---

## 📦 Estruturas de Dados
 ✅ Listas (criação, acesso, métodos)   
 ✅ Tuplas (imutabilidade)  
 ✅ Dicionários (chave/valor)   
 ⬜ Sets (conjuntos) 

---

## 🧠 Funções
 ⬜ Funções simples  
 ⬜ Parâmetros e retorno     
 ⬜ Argumentos nomeados  
 ⬜ Valores padrão   
 ⬜ Funções dentro de funções    
 ⬜ `lambda` 

---

## 🧱 Introdução à POO
 ⬜ Criar primeira classe    
 ⬜ Atributos e métodos  
 ⬜ `__init__`   
 ⬜ Instância de objeto  
 ⬜ Exercício prático simples    

---

## ⚠️ Tratamento de Exceções
 ⬜ `try / except`   
 ⬜ `finally`    
 ⬜ Trabalhar com erros reais (ex: divisão por zero) 

---

## 📁 Manipulação de Arquivos
 ⬜ Ler arquivos texto   
 ⬜ Escrever arquivos    
 ⬜ `with open()` (context manager)  

---

## 🏁 Mini Projetos (Fundamentos)
 ⬜ Calculadora simples  
 ⬜ Sistema básico de cadastro (lista/dicionário)    
 ⬜ Conversor de temperatura     
 ⬜ Simulador de lista de compras    

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
        nome_fmt = nome.strip().title()
        
        if " " in nome or " " in nickname:
            st.error("O nome ou nickname não pode conter espaços.")
        elif not nome or not sobrenome:
            st.error("Preencha nome e sobrenome.")
        else:
            # normalizações
            sobrenome_fmt = (
                sobrenome.strip()
                .title()
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
            

    st.markdown("---")
    
    # Calculo Fatorial
    def fatorial(n):
        """Calcula o fatorial de n de forma recursiva."""
        if n == 0 or n == 1:
            return 1
        else:
            return n * fatorial(n - 1)
        
    st.title("📚 Cálculo do Fatorial em Python")
    st.markdown("""
                >Problema clássico em programação é o cáclculo do fatorial. Ele é utilizado em estatística para calcular permutações e combinações de conjuntos.
                >O cálculo é simples e por isso muito utilizado como exemplo em cursos de programação.
                
                ### Para calcular o fatorial, multiplicamos o número por todos os números que precedem até chegarmos em 1.
                
                _Um caso especial é o fatorial de 0, que por definição é 1._
                ```bash
                Ex.:
                5! = 5 x 4 x 3 x 2 x 1 = 120
                0! = 1
                ```
                """)

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
    
    st.divider() 
    
    # Tempo de entrega de delivery (Basico)
    import streamlit as st
    import time

    option = ""
    options = ["Macdonalds", "Burguer Kings", "KFC", "Sair"]

    def header():
        st.header("🛵 Verifique o tempo de entrega dos restaurantes.")
        
    def choice(option):
        option_selected = st.selectbox(
            "Escolha o restaurante!",
            (options),
        )
        option = option_selected
        return option

    def response(restaurant_name: str, delivery_time: int) -> None:
        st.caption("Resturante: " + restaurant_name)
        st.caption("Tempo de entrega: " + str(delivery_time) + "min")
        
    def main():
        
        restaurant_name = ''
        delivery_time = 0
        
        header()
        st.divider()
        decision = choice(option)
        # st.space()
        
        while True:
            if decision == "Macdonalds":
                restaurant_name = decision
                delivery_time = 35
                response(restaurant_name,delivery_time)
                break
            elif decision == "Burguer Kings":
                restaurant_name = decision
                delivery_time = 30
                response(restaurant_name,delivery_time)
                break
            elif decision == "KFC":
                restaurant_name = decision
                delivery_time = 20
                response(restaurant_name,delivery_time)
                break
            elif decision == "Sair":
                with st.spinner("Processando...", show_time=False):
                    time.sleep(3)
                st.info("Volte sempre!!!")
                break
            else:
                with st.spinner("Processando...", show_time=False):
                    time.sleep(3)
                st.error("Opss! Escolha uma opção válida!")
                break

            
        
        st.divider()

        
    # ponto de entrada do programa recomendado
    if __name__ == "__main__":
        main()

    # Calculadora IMC (Basico)
    st.header("⚖️ Calculadora de IMC")
    st.markdown("""
        O Índice de Massa Corporal (IMC) é uma medida utilizada para avaliar se uma pessoa está com peso adequado em relação à sua altura. 
        Ele é calculado dividindo o peso da pessoa (em kg) pela altura ao quadrado (em metros). O resultado é um número que pode ser interpretado 
        para determinar se a pessoa está abaixo do peso, com peso normal, sobrepeso ou obesidade.

        ### Fórmula do IMC:
        
        ```bash
        IMC = peso (kg) / (altura (m))^2
        ```
            
        ### Classificação do IMC:
        - Abaixo de 18,5: Abaixo do peso
        - Entre 18,5 e 24,9: Peso normal
        - Entre 25 e 29,9: Sobrepeso
        - 30 ou acima: Obesidade
        """)
    st.caption("""
            ### Observações:
            - O IMC é uma medida simples e não leva em consideração fatores como massa muscular, distribuição de gordura ou outros aspectos da saúde.
            - Para uma avaliação mais completa da saúde, é recomendado consultar um profissional de saúde.
            """)
    
    def calcular_imc(peso: float, altura: float) -> float:
        """Calcula o Índice de Massa Corporal (IMC) dado o peso e a altura."""
        if altura <= 0:
            raise ValueError("A altura deve ser maior que zero.")
        imc = peso / (altura ** 2)
        return imc
    
    def classificar_imc(imc: float) -> str:
        """Classifica o IMC de acordo com as faixas estabelecidas."""
        if imc < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= imc < 25:
            return "Peso normal"
        elif 25 <= imc < 30:
            return "Sobrepeso"
        else:
            return "Obesidade"
        
    with st.form("imc_form"):
        peso = st.number_input("Digite seu peso em kg:", min_value=0.0, value=70.0, step=0.1)
        altura = st.number_input("Digite sua altura em metros:", min_value=0.0, value=1.75, step=0.01)
        submitted_imc = st.form_submit_button("Calcular IMC")
        
    if submitted_imc:
        try:
            imc_resultado = calcular_imc(peso, altura)
            classificacao = classificar_imc(imc_resultado)
            with st.spinner("Calculando...", show_time=False):
                time.sleep(2)
            st.success(f"Seu IMC é {imc_resultado:.2f}, o que é classificado como: {classificacao}.")
            
        except ValueError as e:
            st.error(str(e))
            
    
    


# ===============================
# Aba 3 - Documentacao
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
            
# ===============================
# Footer
# ===============================
footer()