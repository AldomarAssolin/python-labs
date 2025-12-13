"""
Docstring for dicionarios.agenda

"""

import csv
import os

BASE_DIR = os.path.dirname(__file__)
CSV_PATH = os.path.join(BASE_DIR, "..", "docs", "agenda.csv")

CAMPOS = ["nome", "telefone", "email"]

# Carrega a agenda de um arquivo CSV
def carregar_csv(caminho):
    
    if not os.path.exists(caminho):
        return []
    
    agenda = []
    
    with open(caminho, mode="r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=",")
        
        for row in reader:
            contato = {
                "nome": (row.get("nome") or "").strip().title(),
                "telefone": (row.get("telefone") or "").strip() or None,
                "email": (row.get("email") or "").strip().lower()
            }
            agenda.append(contato)
    
    return agenda
# ********** Fim carregar_csv ***************

# Salva a agenda em um arquivo CSV
def salvar_csv(agenda, caminho):
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    
    with open(caminho, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CAMPOS, delimiter=",")
        writer.writeheader()
        
        for contato in agenda:
            writer.writerow({
                "nome": contato.get("nome", ""),
                "telefone": contato.get("telefone") or "",
                "email": contato.get("email", "")
            })
# ********** Fim salvar_csv ***************

# Função para adicionar um contato à agenda
def add_contato(agenda, nome, email, telefone=None):
    if len(nome) < 3 or email.count("@") != 1:
        raise ValueError("Nome ou email inválido")
    email = email.strip().lower()
    
    for contato in agenda:
        if contato.get('email') == email:
            raise ValueError("Contato já existe")
        
    novo_contato = {
        "nome": nome.strip().title(),
        "telefone": str(telefone).strip() if telefone else None,
        "email": email
    }
    
    agenda.append(novo_contato)
    return True
# ********** Fim add_contato ***************

# Busca contato por email
def buscar_contato_por_email(agenda, email):
    email = email.strip().lower()
    
    if not email or email.count("@") != 1:
        return None
    
    for contato in agenda:
        if contato.get('email') == email:
            return contato
# ********** Fim buscar_contato_por_email ***************

# Atualiza um contato existente
def att_contato(agenda, email_atual, novo_email, nome=None, telefone=None):
    email_atual = email_atual.strip().lower()
    novo_email = novo_email.strip().lower()
    
    if not novo_email:
        novo_email = email_atual  # Mantém o email atual se o novo for inválido
        
    contato = buscar_contato_por_email(agenda, email_atual)
    
    if novo_email == email_atual:
        return # Nenhuma alteração necessária
    elif not contato:
        raise ValueError("Contato não encontrado")
    elif novo_email != email_atual:
        if buscar_contato_por_email(agenda, novo_email):
            raise ValueError("Já existe um contato com o novo email")
    
    contato["nome"] = nome.strip().title() if nome else contato["nome"]
    contato["telefone"] = telefone.strip() if telefone else contato["telefone"]
    contato["email"] = novo_email
    return True

# ********** Fim att_contato ***************


# Exclui um contato da agenda
def del_contato(agenda, email):
    email = email.strip().lower()
    contato = buscar_contato_por_email(agenda, email)
    
    if not contato:
        raise ValueError("Contato não encontrado")
    
    agenda.remove(contato)
    return True

# ********** Fim del_contato ***************

# Formatar e exibir contatos
def formatar_contato(contato):
    nome = contato.get("nome") if contato.get("nome") else None
    telefone = contato.get("telefone") if contato.get("telefone") else None
    email = contato.get("email") if contato.get("email") else None
    return f"Nome: {nome}\nTelefone: {telefone}\nEmail: {email}\n" + "-" * 40

# Lista todos os contatos
def listar_contatos(agenda):
    contatos = agenda
    print(f"Total de contatos: {len(contatos)}")
    print("-" * 40)
    for contato in contatos:
        print(formatar_contato(contato))
# ********** Fim listar_contatos ***************

# Lê e valida o nome do usuário
def ler_nome():
    while True:
        nome = input("Digite o nome: ").strip()
        if len(nome) < 3:
            print("Nome deve ter pelo menos 3 caracteres.")
        else:
            return nome.title()
# ********** Fim ler_nome ***************

# Lê e valida o email do usuário
def ler_email():
    while True:
        email = input("Digite o email: ").strip()
        if "@" not in email:
            print("Email inválido. Certifique-se de que contenha '@'.")
        else:
            return email.lower()
# ********** Fim ler_email ***************

# Lê o telefone do usuário
def ler_telefone():
    telefone = input("Digite o telefone (opcional): ").strip()
    if telefone and len(telefone) < 9:
        print("Telefone deve ter pelo menos 10 dígitos.")
        return ler_telefone()
    return telefone or None
# ********** Fim ler_telefone ***************

# Atualiza nome
def novo_nome():
    while True:
        nome = input("Digite o novo nome: ").strip()
        if not nome:
            return ""  # Permite manter o nome atual
        if len(nome) < 3:
            print("Nome deve ter pelo menos 3 caracteres.")
        else:
            return nome.title()

# Atualiza email
def ler_novo_email():
    while True:
        email = input("Digite o novo email: ").strip()
        if not email:
            return ""  # Permite manter o email atual
        if "@" not in email:
            print("Email inválido. Certifique-se de que contenha '@'.")
        return email.lower()
# ********** Fim ler_novo_email ***************

# Atualiza telefone
def ler_novo_telefone():
    telefone = input("Digite o novo telefone (opcional): ").strip()
    if not telefone:
        return ""  # Permite manter o telefone atual
    if len(telefone) < 9:
        print("Telefone deve ter pelo menos 10 dígitos.")
        return ler_novo_telefone()
    return telefone

# Função principal do programa
def main():
    agenda = carregar_csv(CSV_PATH)  # Carrega a agenda no início

    while True:
        print("\n1 - Adicionar contato")
        print("2 - Listar contatos")
        print("3 - Buscar contato por email")
        print("4 - Atualizar contato")
        print("5 - Excluir contato")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                nome = ler_nome()
                email = ler_email()
                telefone = ler_telefone()
                add_contato(agenda, nome, email, telefone)
                salvar_csv(agenda, CSV_PATH)
                print("Contato adicionado com sucesso.")
            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == "2":
            try:
                if not agenda:
                    print("A agenda está vazia.")
                else:
                    listar_contatos(agenda)
            except Exception as e:
                print(f"Erro ao listar contatos: {e}")

        elif opcao == "3":
            try:
                email = ler_email()
                contato = buscar_contato_por_email(agenda, email)
                if contato:
                    print(f"Contato encontrado: \n{formatar_contato(contato)}")
                else:
                    print("Contato não encontrado.")
            except Exception as e:
                print(f"Erro ao buscar contato: {e}")

        elif opcao == "4":
            try:
                email_atual = ler_email()
                novo_email = ler_novo_email() or email_atual
                nome = novo_nome() or None
                telefone = ler_novo_telefone() or None
                att_contato(agenda, email_atual, novo_email, nome, telefone)
                salvar_csv(agenda, CSV_PATH)
                print("Contato atualizado com sucesso.")
            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == "5":
            try:
                email = ler_email()
                del_contato(agenda, email)
                salvar_csv(agenda, CSV_PATH)
                print("Contato excluído com sucesso.")
            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()