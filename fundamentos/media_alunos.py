"""
Criar sistema de cadastro de alunos, onde o usuário possa inserir o nome, idade e curso do aluno.

Parametros:
- Criar aluno: O usuário deve ser capaz de cadastrar um novo aluno, fornecendo nome, idade e curso.
- Listar alunos: O sistema deve permitir listar todos os alunos cadastrados.
- Buscar aluno: O sistema deve permitir buscar um aluno específico pelo nome.
- Cadastrar notas: O usuário deve ser capaz de cadastrar notas para cada aluno.
- Calcular média: O sistema deve calcular a média das notas de cada aluno e exibir-la.

Regras:
- O sistema deve validar as entradas
- idade seja um número positivo
- nome e curso não sejam vazios. 

"""

MENU = """
*********Cadastro de Alunos**********
-> Escolha uma das opcoes abaixo:
1. Cadastrar aluno
2. Listar alunos
3. Buscar aluno
4. Cadastrar notas
5. Calcular média
6. Sair
*************************************
"""

# Funcao para encontrar um aluno pelo nome
def encontrar_aluno(alunos: list, nome: str):
    """Encontra um aluno pelo nome"""
    nome = nome.strip().casefold()
    return next((a for a in alunos if a['nome'].casefold() == nome), None)

# Função para cadastrar um novo aluno
def cadastrar_aluno(alunos: list, proximo_id: int) -> int:
    """Cadastra um novo aluno"""
    nome = input("Digite o nome do aluno: ").strip()
    curso = input("Digite o curso do aluno: ").strip()
    
    if not nome or not curso:
        print("Nome e curso não podem ser vazios.")
        return proximo_id
    
    idade_str = input("Digite a idade do aluno: ").strip()
    try:
        idade = int(idade_str)
        if idade <= 0:
            print("Idade deve ser um número positivo.")
            return proximo_id
    except ValueError:
        print("Idade deve ser um número inteiro.")
        return proximo_id
    
    aluno = {
        'id': proximo_id,
        'nome': nome,
        'idade': idade,
        'curso': curso,
        'notas': []
        }
    
    alunos.append(aluno)
    print(f"Aluno {nome} cadastrado com sucesso.")
    return proximo_id + 1
    
# Função para Listar Alunos
def listar_alunos(alunos: list):
    """Lista todos os alunos cadastrados"""
    print("-------- Lista de Alunos --------")
    if not alunos:
        print("Nenhum aluno cadastrado.")
        print("--------------------------------")
        return
    
    for aluno in alunos:
        print(f"ID: {aluno['id']}, Nome: {aluno['nome']}, Idade: {aluno['idade']}, Curso: {aluno['curso']}")
    print("--------------------------------")
        
# Função para buscar um aluno específico pelo nome
def buscar_aluno(alunos: list):
    """Busca um aluno específico pelo nome"""
    nome = input("Digite o nome do aluno que deseja buscar: ").strip()
    
    aluno = encontrar_aluno(alunos, nome)
    if aluno:
        print(f"Aluno encontrado: ID: {aluno['id']}, Nome: {aluno['nome']}, Idade: {aluno['idade']}, Curso: {aluno['curso']}")
    else:
        print("Aluno não encontrado.")
    
# Função para cadastrar notas para cada aluno
def cadastrar_notas(alunos: list):
    """Cadastra notas para um aluno específico"""
    nome = input("Digite o nome do aluno para cadastrar notas: ").strip()
    
    aluno = encontrar_aluno(alunos, nome)
    
    if not aluno:
        print("Aluno não encontrado.")
        return
    
    nota_str = input("Digite a nota do aluno (0 a 10): ").strip()
    try:
        nota = float(nota_str)
        if 0 <= nota <= 10:
            aluno['notas'].append(nota)
            print(f"Nota {nota} cadastrada para o aluno {aluno['nome']}.")
        else:
            print("Nota deve ser entre 0 e 10.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número para a nota.")

# Função para calcular a média das notas de cada aluno
def calcular_media(alunos: list):
    """Calcula a média das notas de cada aluno"""
    print("-------- Médias --------")
    if not alunos:
        print("Nenhum aluno cadastrado.")
        print("-----------------------")
        return
    
    for aluno in alunos:
        if aluno['notas']:
            media = sum(aluno['notas']) / len(aluno['notas'])
            print(f"Aluno: {aluno['nome']}, Média: {media:.2f}")
        else:
            print(f"Aluno: {aluno['nome']}, Sem notas cadastradas.")
    print("-----------------------")
    
# Função principal para executar o sistema de cadastro de alunos
def main():
    alunos = []
    proximo_id = 1
    while True:
        print(MENU)
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            proximo_id = cadastrar_aluno(alunos, proximo_id)
        elif escolha == "2":
            listar_alunos(alunos)
        elif escolha == "3":
            buscar_aluno(alunos)
        elif escolha == "4":
            cadastrar_notas(alunos)
        elif escolha == "5":
            calcular_media(alunos)
        elif escolha == "6":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")
            
if __name__ == "__main__":
    main()