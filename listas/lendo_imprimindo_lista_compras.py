from datetime import datetime, date
compras = []

while True:
    item = input("Digite um item para adicionar à lista de compras (ou 'sair' para terminar): ")
    if item.lower() == 'sair':
        break
    compras.append(item)
print("\nSua lista de compras:")
for indice, item in enumerate(compras, start=1):
    print(f"{indice}. {item}")
