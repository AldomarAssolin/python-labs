"""
Docstring for listas.listas_exercicios-avancado

Listas - Exercícios Avançados

"""

# EX. 1 - Ordene uma lista manualmente (sem usar .sort() ou sorted()).
contatos = ["Maria", "Ana", "João", "Pedro", "Carla"]
n = len(contatos)

for i in range(n):
    for j in range(0, n-i-1):
        if contatos[j] > contatos[j+1]:
            # Troca os elementos
            contatos[j], contatos[j+1] = contatos[j+1], contatos[j]
print("Lista ordenada:", contatos)


# EX. 2 - Misture duas listas alternando elementos (zip manual).
lista1 = [1, 3, 5, 7]
lista2 = ['a', 'b', 'c', 'd']
misturada = []
for i in range(min(len(lista1), len(lista2))):
    misturada.append(lista1[i])
    misturada.append(lista2[i])
print("Lista misturada:", misturada)

# EX. 3 - Crie uma lista com 20 números aleatórios entre 1 e 100.
import random
numeros_aleatorios = []
for _ in range(20):
    numeros_aleatorios.append(random.randint(1, 100))
print("Números aleatórios:", numeros_aleatorios)

# EX. 4 - Filtre apenas números maiores que 50.
maiores_que_50 = []
for numero in numeros_aleatorios:
    if numero > 50:
        maiores_que_50.append(numero)
print("Números maiores que 50:", maiores_que_50)

# EX. 5 - Implemente uma função slice(lista, inicio, fim) que simula o slicing do Python.
def slice(lista, inicio, fim):
    resultado = []
    for i in range(inicio, fim):
        resultado.append(lista[i])
    return resultado
print("Slice da lista de números aleatórios (índices 5 a 15):", slice(numeros_aleatorios, 5, 15))
