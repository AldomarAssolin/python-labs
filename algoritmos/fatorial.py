"""Cálculo do fatorial de um número usando função recursiva em Python."""

# Calculo Fatorial
def fatorial(n):
    """Calcula o fatorial de n de forma recursiva."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
    
# Exemplo de uso
numero = 5
resultado = fatorial(numero)
print(f"O fatorial de {numero} é {resultado}.")

# Retorno esperado: O fatorial de 5 é 120.

"""
Explicação do código:
1. Definimos uma função chamada `fatorial` que recebe um parâmetro `n`.
2. A função verifica se `n` é 0 ou 1. Se for, retorna 1, pois o fatorial de 0 e 1 é 1.
3. Se `n` for maior que 1, a função retorna `n` multiplicado pelo resultado da função `fatorial` chamada com `n - 1`. Isso cria uma chamada recursiva que continua até atingir o caso base (0 ou 1).
4. No exemplo de uso, calculamos o fatorial de 5 e imprimimos o resultado, que é 120.

Nota: O fatorial de um número é uma função matemática importante em várias áreas, incluindo combinatória, probabilidade e análise de algoritmos. 
A definição recursiva é uma maneira elegante de expressar o cálculo do fatorial, embora para números grandes seja mais eficiente usar uma abordagem 
iterativa ou técnicas de memoização para evitar chamadas recursivas excessivas.

O fatorial de um número n (denotado como n!) é o produto de todos os números inteiros positivos de 1 até n.
Por exemplo, 5! = 5 * 4 * 3 * 2 * 1 = 120.
A função fatorial é definida de forma recursiva, onde o caso base é quando n é 0 ou 1, retornando 1. Para outros valores de n, a função chama a si 
mesma com n-1 até atingir o caso base.
"""

    
