"""
Aula 1: entrada/saída e padrão main()

"""

def main():
    nome = input("Digite seu nome: ")
    print(f"Olá, {nome}! Este é o Python Labs.")
    
    
# ponto de entrada do programa recomendado
if __name__ == "__main__":
    main()
    
"""

Por que usar main() e o guard if __name__ == "__main__"?

-> Permite executar o arquivo diretamente ou importá-lo em testes/outros scripts sem rodar o código automaticamente.
->Facilita evoluir para testes unitários depois.

"""