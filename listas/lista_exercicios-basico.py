"""
Docstring for listas.listas_exercicios-basicos

Listas - Exercícios Básicos

"""

# EX. 1 - Crie uma lista com 5 frutas e exiba o primeiro e o último item.
frutas = ["maçã", "banana", "laranja", "uva", "pera"]
print("Lista de frutas:", frutas)

print("Primeira fruta:", frutas[0])
print("Última fruta:", frutas[-1])

# EX. 2 - Adicione um item novo no final da lista.
frutas.append("manga")
print("Lista de frutas após adicionar manga:", frutas)

# EX. 3 - Remova um item específico da lista.
frutas.remove("banana")
print("Lista de frutas após remover banana:", frutas)

# EX. 4 - Conte quantos elementos existem na lista (sem usar len()).
contador = 0
for fruta in frutas:
    contador += 1
print("Número de frutas na lista:", contador)

# EX. 5 - Inverta a lista manualmente (sem reverse() e sem [::-1]).

i = 0
j = len(frutas) - 1
while i < j:
    item = frutas[i] # guarda o valor temporariamente em uma lista auxiliar
    frutas[i] = frutas[j] # atribui o valor da posição j para a posição i
    frutas[j] = item # atribui o valor guardado na lista auxiliar para a posição j
    i += 1 # incrementa i 
    j -= 1 # decrementa j
print("Lista de frutas invertida primeira solução:", frutas)
    
# Outra solução para inverter a lista:
frutas_invertidas = []
for i in range(contador - 1, -1, -1): # contador - 1 é o último índice da lista. O -1 é para incluir o índice 0. O -1 final é o passo (decremento).
    frutas_invertidas.append(frutas[i])
print("Lista de frutas invertida:", frutas_invertidas)

# O que é o range()?
# O range() é uma função que gera uma sequência de números inteiros, que pode ser usada para iterar em loops. 
# Ele pode receber até três argumentos: início, fim e passo.