"""Calculadora do Índice de Massa Corporal (IMC) com classificação.

🔬 Para entender as variáveis neste código (aula prática):

Imagine que você tem uma caixa vazia. Quando você coloca algo nela, essa coisa ganha um nome para você poder 
encontrá-la depois. Essa caixa com nome é uma variável em Python.

Exemplos reais deste código:

peso = 70.5        ← 'peso' é o nome da caixa, 70.5 é o que está dentro
altura = 1.75      ← 'altura' é o nome da caixa, 1.75 é o que está dentro
imc = 22.86        ← 'imc' é o nome da caixa, 22.86 é o que está dentro
classificacao = "Normal"  ← nome da caixa, texto dentro

Cada vez que você quiser usar o valor do peso, altura, IMC ou classificação, você pode simplesmente usar o nome da 
variável (caixa) em vez de escrever o número ou texto toda vez. Isso torna seu código mais fácil de ler e manter.
"""

print("***Variaveis com valor atibuido***")
peso = 70.5 # Aqui estamos criando uma variável chamada 'peso' e atribuindo a ela o valor 70.5 (que representa o peso em kg).
altura = 1.75 # Aqui estamos criando uma variável chamada 'altura' e atribuindo a ela o valor 1.75 (que representa a altura em metros).
classificacao = "Normal" # Aqui estamos criando uma variável chamada 'classificacao' e atribuindo a ela o valor "Normal" (que representa a classificação do IMC).

calculo_imc = peso / (altura ** 2) # Veja aqui as variaveis sendo usadas para calcular o IMC
imc = round(calculo_imc, 2)

print(f"Peso: {peso} kg") # print é um método de saída. Ele mostra o que está dentro dos parênteses na tela.
print(f"Altura: {altura} m")
print(f"Classificação: {classificacao}")
print(f"IMC: {imc}")
print("#"*30)

print("***Variaveis com dados de entrada do usuario***")
peso_digitado = float(input("Digite seu peso em kg: ") ) # Aqui estamos usando a função input() para pedir ao usuário que digite seu peso. O valor digitado é uma string, então usamos float() para converter essa string em um número decimal (float) e armazenamos esse valor na variável 'peso_digitado'.
altura_digitada = float(input("Digite sua altura em metros: ") ) # Aqui estamos usando a função input() para pedir ao usuário que digite sua altura. O valor digitado é uma

calculo_imc = peso_digitado / (altura_digitada ** 2) # Veja aqui as variaveis sendo usadas para calcular o IMC
imc = round(calculo_imc, 2)

# Condicionais if-elif-else para classificar o IMC
if imc < 18.5:
    classificacao = "Abaixo do peso" # Utilizando a variável 'classificacao' para armazenar o resultado da classificação do IMC
elif 18.5 <= imc < 25:
    classificacao = "Normal"
elif 25 <= imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

# Dados de saida com a funcao print() para mostrar o resultado na tela, utilizando as variáveis para exibir os valores calculados e a classificação do IMC.
print(f"Peso: {peso_digitado} kg")
print(f"Altura: {altura_digitada} m")
print(f"IMC: {imc}")
print(f"Classificação: {classificacao}")

# Resultado esperado:
"""
##############################
***Variaveis com dados de entrada do usuario***
Digite seu peso em kg: 80 -> O usuário digita 80 e pressiona Enter
Digite sua altura em metros: 1.75 -> O usuário digita 1.75 e pressiona Enter
Peso: 80.0 kg
Altura: 1.75 m
IMC: 26.12
Classificação: Sobrepeso
"""
