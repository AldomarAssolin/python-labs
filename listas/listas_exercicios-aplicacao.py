"""
Docstring for listas.listas_exercicios-aplicacao

Listas - Exercícios de Aplicação
"""

# EX. 1 - Remova todos os itens duplicados de uma lista.
itens = [1, 2, 2, 3, 4, 4, 5, 1, 6]
print("Lista original:", itens)

itens_unicos = []
for item in itens:
    if item not in itens_unicos:
        itens_unicos.append(item)
print("Lista sem itens duplicados:", itens_unicos)

"""
Alternativas nativas:
set() -> remove duplicados mas perde a ordem
dict.fromkeys() -> remove duplicados mantendo a ordem (desde Python 3.7)
collections.OrderedDict -> (antes de 3.7)
"""

# EX. 2 - Conte quantas vezes um elemento aparece na lista.
elemento = 4
contador = 0
for item in itens:
    if item == elemento:
        contador += 1
print(f"O elemento {elemento} aparece {contador} vezes na lista.")

"""
Também é possível usar o método count() das listas para contar ocorrências:
contador = itens.count(elemento)
"""

# EX. 3 - Faça uma função que retorna apenas itens únicos de uma lista.
def itens_unicos_func(lista):
    unicos = []
    for item in lista:
        if item not in unicos:
            unicos.append(item)
    return unicos

print("Itens únicos usando função:", itens_unicos_func(itens))

# EX. 4 - Faça uma função que busca um nome numa lista e retorna True ou False.
def busca_nome(lista, nome):
    for item in lista:
        if item == nome:
            return True
    return False
nomes = ["Ana", "Bruno", "Carla", "Daniel"]
print("Busca por 'Carla':", busca_nome(nomes, "Carla"))
print("Busca por 'Eduardo':", busca_nome(nomes, "Eduardo"))

"""

Também é possível usar o operador in para buscar itens em listas:
def busca_nome(lista, nome):
    return nome in lista
    
"""

# EX. 5 - Crie uma lista de listas (matriz 3x3) e imprima os elementos diagonalmente.
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matriz 3x3:")
for linha in matriz:
    print(linha)
    
print("Elementos diagonais:")
for i in range(3):
    print(matriz[i][i])
    
print("Elementos diagonais inversos:")
for i in range(3):
    print(matriz[i][2 - i])
    