import pandas as pd


menu = """
Lista de Compras
1 - Para Inserir um item
2 - Para Atualizar um item
3 - Para Remover um item
4 - Para Exibir a lista
0 - Para Sair
"""

# Criando a lista de compras como um DataFrame
dados = {
    'Produto': [],
    'Quantidade': [],
    'unidade': []
}

lista_compras = pd.DataFrame(dados)

while True:
    print(menu)
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        produto = input("Digite o nome do produto: ")
        quantidade = input("Digite a quantidade: ")
        unidade = input("Digite a unidade (ex: kg, litros, unidades): ")
        novo_item = pd.DataFrame({'Produto': [produto], 'Quantidade': [quantidade], 'unidade': [unidade]})
        lista_compras = pd.concat([lista_compras, novo_item], ignore_index=True)
        print(f"{produto} adicionado à lista.")

    elif escolha == '2':
        produto = input("Digite o nome do produto que deseja atualizar: ")
        if produto in lista_compras['Produto'].values:
            nova_quantidade = input("Digite a nova quantidade: ")
            nova_unidade = input("Digite a nova unidade: ")
            lista_compras.loc[lista_compras['Produto'] == produto, 'Quantidade'] = nova_quantidade
            lista_compras.loc[lista_compras['Produto'] == produto, 'unidade'] = nova_unidade
            print(f"{produto} atualizado na lista.")
        else:
            print(f"{produto} não encontrado na lista.")

    elif escolha == '3':
        produto = input("Digite o nome do produto que deseja remover: ")
        if produto in lista_compras['Produto'].values:
            lista_compras = lista_compras[lista_compras['Produto'] != produto]
            print(f"{produto} removido da lista.")
        else:
            print(f"{produto} não encontrado na lista.")

    elif escolha == '4':
        if lista_compras.empty:
            print("A lista de compras está vazia.")
        else:
            print("\nLista de Compras:")
            print(lista_compras)

    elif escolha == '0':
        print("Saindo da aplicação.")
        break

    else:
        print("Opção inválida. Tente novamente.")