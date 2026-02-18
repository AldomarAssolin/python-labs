"""Simula um sistema de entrega de restaurantes com menu interativo.

O usuário escolhe um restaurante a partir de um menu apresentado no console
e recebe a estimativa de tempo de entrega em minutos. Também é possível sair
do programa através de uma opção específica.

Parameters:
None
    Este módulo não recebe parâmetros na execução direta. As interações
    ocorrem via entrada padrão (input) durante a chamada de `main()`.

Returns:
None
    O script exibe mensagens no console informando o tempo de entrega
    ou a saída do programa, sem retornar valores para o chamador.

Raises:
ValueError
    Pode ocorrer se a conversão de entradas for adicionada futuramente
    (por exemplo, ao transformar opções em inteiros) e o usuário fornecer
    valores incompatíveis.

Notas:
O fluxo principal é coordenado pela função ``main()``, que:
- Exibe o cabeçalho com o menu de restaurantes.
- Lê a opção do usuário pela função ``entregas()``.
- Determina o restaurante selecionado, calcula o tempo de entrega e
  chama ``mensagem()`` para exibir o resultado.
- Encerra quando o usuário escolhe a opção de saída.

O padrão ``if __name__ == "__main__":`` é utilizado para permitir a
execução direta do script como programa ou a importação do módulo em
outros arquivos sem disparar automaticamente o fluxo principal.
"""



header = '''
    *********** Opções ***********
    [0] Macdonalds 08
    [1] Burger King 03
    [2] KFC 25
    [S] Para sair
    
    *********** ______ ***********
    '''


footer = '''
    *********** ______ ***********
    
        Você saiu...
        Volte sempre!
        
    *********** ______ ***********
    '''
 

# Função para ler a opção do usuário
def entregas(nome_restaurante):
    """Solicita a escolha do usuário e retorna a opção selecionada."""
    nome_restaurante = input('Escolha uma opção: ')
    return nome_restaurante

# Função para exibir a mensagem de tempo de entrega
def mensagem(restaurante, tempo_entrega):
    """Exibe o tempo de entrega para o restaurante selecionado."""
    return print(f'O restaurante {restaurante} entrega em {tempo_entrega} minutos.')
    

def main():
    
    print(header)
    
    
    nome_restaurante = ''
    tempo_entrega = 0

    while True:
        
        options = entregas(nome_restaurante)
        
        if options == "0":
            restaurante = 'MacDonalds'
            tempo_entrega = 21
            mensagem(restaurante, tempo_entrega)
        
        elif options == "1":
            restaurante = 'Burguer King 03'
            tempo_entrega = 27
            mensagem(restaurante, tempo_entrega)
            
        elif options == "2":
            restaurante = 'KFC 25'
            tempo_entrega = 17
            mensagem(restaurante, tempo_entrega)
            
        elif options == 's' or options == 'S':
            print(footer)
            break
        
        else:
            print('Ação inválida, por favor, entre em contato com o sac.')
            print(footer)

if __name__ == "__main__":
    main()