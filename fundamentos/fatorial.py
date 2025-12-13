"""
Docstring for fundamentos.fatorial

Cálculo do fatorial de um número usando função recursiva em Python.
"""

import streamlit as st


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
