"""
Docstring for listas.listas_exercicios-intermediario

Listas - Exercícios Intermediário
"""

# EX. 1 - Crie uma lista de números e retorne apenas os números pares.
numeros = [10, 15, 22, 33, 40, 55, 60]
print("Lista de números:", numeros)
numeros_pares = []
for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)
print("Números pares na lista:", numeros_pares)

# Outra forma de fazer o EX. 1 usando list comprehension:
"""
Explicação sobre list comprehension:
List comprehension é uma forma concisa de criar listas em Python.
Ela permite construir uma nova lista aplicando uma expressão a cada item de uma sequência ou iterável, opcionalmente filtrando os itens com uma condição.
A sintaxe básica é:
[nova_expressão for item in iterável if condição]
Por exemplo, a lista de números pares acima poderia ser criada assim:
numeros_pares = [numero for numero in numeros if numero % 2 == 0]
"""

# EX. 2 - Some todos os valores da lista usando for.
soma = 0
for numero in numeros:
    soma += numero
print("Soma de todos os números na lista:", soma)

""" 
Outra forma de fazer o EX. 2 usando a função sum()
soma = sum(numeros) 
"""

# EX. 3 - Encontre o maior e o menor número sem usar max() ou min().
maior = numeros[0]
menor = numeros[0]
for numero in numeros:
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
print("Maior número na lista:", maior)
print("Menor número na lista:", menor)

# EX. 4 - Crie uma nova lista contendo os quadrados dos números de outra lista.
lista_numero = [1, 2, 3, 4, 5]
quadrados = []
for numero in lista_numero:
    quadrados.append(numero ** 2)
print("Lista de quadrados dos números:", quadrados)

# Outra forma de fazer o EX. 4 usando list comprehension:
"""
quadrados = [numero ** 2 for numero in lista_numero]
ou
quadrado = [n*n for n in lista_numero]
"""

# EX. 5 - Junte duas listas sem usar o operador +.
numeros.extend(lista_numero)
print("Lista após juntar as duas listas:", numeros)