"""
Docstring for pages.002-001_Listas_Filas

Utilizando Listas como Filas em Python
Simulando atendimento em uma fila de banco

Nesta simulação teremos 3 atendimentos principais: 
1 - Normal,
2 - Prioritário,
3 - Caixa.

-> Uma fila será representada por uma lista, onde os clientes serão adicionados ao final da lista e atendidos na ordem de chegada (FIFO - First In, First Out).

-> Teremos que saber quando vamos atender cada nível de atendimento, para isso, o usuário poderá escolher qual tipo de atendimento deseja realizar.

-> O cliente receberá uma senha baseada no tipo de atendimento escolhido e será adicionado à fila.
"""

menu = """
Auto Atendimento Bancário
=======================
Utilizando Listas como Filas em Python
Simulando atendimento em uma fila de banco
=======================
Selecione uma opção:
1. Adicionar cliente à fila
2. Atender próximo cliente
3. Ver fila atual
4. Sair
"""

menu_options = {
    1: "Normal",
    2: "Prioritario",
    3: "Caixa"
}

tipo_atendimento = {
    "Normal": "NOR",
    "Prioritario": "PRI",
    "Caixa": "CAX"
}

fila = []
contador_senhas = {
    "Normal": 0,
    "Prioritario": 0,
    "Caixa": 0
}

def gerar_senha(tipo: str) -> str:
    """Gera uma senha no formato TIPOnnn, ex: NOR001, PRI005."""
    contador_senhas[tipo] += 1
    return f"{tipo_atendimento[tipo]}{contador_senhas[tipo]:03d}"

def adicionar_cliente():
    print("\nTipos de atendimento:")
    for k, v in menu_options.items():
        print(f"{k} - {v}")
    try:
        opcao = int(input("Escolha o tipo de atendimento: "))
        if opcao not in menu_options:
            print("Opção inválida.")
            return
        tipo = menu_options[opcao]
        senha = gerar_senha(tipo)
        fila.append({"tipo": tipo, "senha": senha})
        print(f"Cliente adicionado à fila: {tipo} - Senha {senha}")
    except ValueError:
        print("Entrada inválida. Digite um número.")

def atender_cliente():
    if not fila:
        print("\nNenhum cliente na fila.")
        return
    cliente = fila.pop(0)  # FIFO: remove o primeiro da lista
    print(f"\nAtendendo cliente: {cliente['tipo']} - Senha {cliente['senha']}")

def ver_fila():
    if not fila:
        print("\nFila vazia.")
        return
    print("\nFila atual:")
    for pos, cliente in enumerate(fila, start=1):
        print(f"{pos}. {cliente['tipo']} - Senha {cliente['senha']}")

# Loop principal
if __name__ == "__main__":
    while True:
        print(menu)
        try:
            opc = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Opção inválida. Digite um número de 1 a 4.")
            continue

        if opc == 1:
            adicionar_cliente()
        elif opc == 2:
            atender_cliente()
        elif opc == 3:
            ver_fila()
        elif opc == 4:
            print("Encerrando o sistema. Até mais!")
            break
        else:
            print("Opção inválida. Escolha entre 1 e 4.")


