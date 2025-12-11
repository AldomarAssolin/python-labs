"""

Docstring for tuplas.exemplos

"""

# EX. 1 - Crie uma tupla com 5 elementos e exiba o primeiro e o último item.
tupla_exemplo = (10, 20, 30, 40, 50)
print("Tupla de exemplo:", tupla_exemplo)
print("Primeiro elemento da tupla:", tupla_exemplo[0])
print("Último elemento da tupla:", tupla_exemplo[-1])

# EX. 2 - Tente modificar um elemento da tupla e observe o erro.
try:
    tupla_exemplo[1] = 25
except TypeError as e:
    print("Erro ao tentar modificar a tupla:", e)
    
# EX. 3 - Desempacote os valores da tupla em variáveis separadas.
a, b, c, d, e = tupla_exemplo
print("Valores desempacotados:", a, b, c, d, e)

# EX. 4 - Concatene duas tuplas e exiba o resultado.
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla_concatenada = tupla1 + tupla2
print("Tupla concatenada:", tupla_concatenada)

# EX. 5 - Verifique se um elemento existe na tupla.
contatos = ("Maria", "João", "Ana", "Pedro")
nome_busca = "Ana"
if nome_busca in contatos:
    print(f"O nome {nome_busca} existe na tupla de contatos.")
else:
    print(f"O nome {nome_busca} não existe na tupla de contatos.")
    
# EX. 6 - Conte quantas vezes um elemento aparece na tupla.
tupla_numeros = (1, 2, 3, 2, 4, 2, 5)
numero_contar = 2   
ocorrencias = tupla_numeros.count(numero_contar)
print(f"O número {numero_contar} aparece {ocorrencias} vezes na tupla.")

# EX. 7 - Converta uma lista em tupla e vice-versa.
lista_exemplo = [100, 200, 300]
tupla_convertida = tuple(lista_exemplo)
print("Tupla convertida da lista:", tupla_convertida)
lista_convertida = list(tupla_exemplo)
print("Lista convertida da tupla:", lista_convertida)

# EX. 8 - Imprima os índices e valores da tupla usando um loop.
for indice, valor in enumerate(tupla_exemplo):
    print(f"Índice: {indice}, Valor: {valor}")
    
# EX. 9 - Crie uma tupla aninhada e acesse um elemento interno.
tupla_aninhada = (1, 2, (3, 4, 5), 6)
elemento_interno = tupla_aninhada[2][1]  # Acessa o valor 4
print("Elemento interno da tupla aninhada:", elemento_interno)

# EX. 10 - Conte quantos itens existem na tupla.
contador = 0
for item in tupla_exemplo:
    contador += 1   
print("Número de itens na tupla:", contador)

# EX. 11 - Crie duas tuplas e junte-as.
tupla_a = ('a', 'b', 'c')
tupla_b = ('d', 'e', 'f')
tupla_junta = tupla_a + tupla_b
print("Tuplas juntadas:", tupla_junta)