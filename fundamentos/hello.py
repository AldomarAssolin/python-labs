"""Aula 1: entrada/saída e padrão main().

Este módulo demonstra:
- Leitura de dados digitados pelo usuário via função input.
- Exibição de mensagens no console com print.
- Uso do padrão main() como ponto de entrada da aplicação.
- Utilização do guard if __name__ == "__main__" para controlar a execução do script.

Ao executar este arquivo diretamente, a função main() é chamada e o programa solicita o nome do usuário e exibe uma saudação personalizada.
Quando o módulo é importado em testes ou em outros scripts, o código dentro de main() não é executado automaticamente, o que facilita a reutilização das funções e a criação de testes unitários.
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
-> Facilita evoluir para testes unitários depois.

"""