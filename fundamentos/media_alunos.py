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
import json
import pandas as pd
from pathlib import Path


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

BASE_DIR = Path(__file__).resolve().parent
PROJETC_ROOT = BASE_DIR.parent
FILEPATH =  PROJETC_ROOT / "docs" / "alunos.csv"
COLS = ['id', 'nome', 'idade', 'curso', 'notas']  

print("Diretorio Base:", BASE_DIR)

# ------------ Infra CSV -------------
def garantir_csv(FILEPATH: Path):
    """Garante que CSV existe com cabecalho e pasta criada"""
    FILEPATH.parent.mkdir(parents=True, exist_ok=True)  
    if not FILEPATH.exists():
        pd.DataFrame(columns=COLS).to_csv(FILEPATH, index=False)
        
def ler_df(FILEPATH: Path) -> pd.DataFrame:
    """Lê o CSV garantindo existência e tipos mínimos."""
    garantir_csv(FILEPATH)
    df = pd.read_csv(FILEPATH, dtype={'id': "int64", 'nome': "string", 'curso': "string", 'notas': "string"})
    
    # idade pode vir como float se o CSV estiver bagunçado, mas vamos normalizar depois quando necessário
    if 'idade' in df.columns:
        df['idade'] = pd.to_numeric(df['idade'], errors='coerce')
    
    # notas vazias viram "[]"
    if 'notas' in df.columns:
        df['notas'] = df['notas'].fillna('[]')
    return df

def salvar_df(df: pd.DataFrame, FILEPATH: Path) -> None:
    """Salva o DF no CSV (sobrescreve)."""
    garantir_csv(FILEPATH)
    df.to_csv(FILEPATH, index=False)
    
def obter_proximo_id(df: pd.DataFrame) -> int:
    """Obtém o próximo ID disponível com base no DF atual."""
    df = ler_df(FILEPATH)
    
    if df.empty:
        return 1
    
    # Converte para int ignorando NaN
    max_id = pd.to_numeric(df['id'], errors='coerce').max()
    
    if pd.isna(max_id):
        return 1
    
    return int(max_id) + 1

# ---------- Utilidades de domínio ----------
def normalizar_nome(s: str) -> str:
    return s.strip().casefold()

def parse_notas(notas_str: str) -> list[float]:
    """Converte string JSON (ex: '[]', '[8.0, 7.5]') em lista."""
    if not notas_str or str(notas_str).strip() == '':
        return []
    
    try:
        notas = json.loads(notas_str)
        if isinstance(notas, list):
            return [float(x) for x in notas]
        return []
    except (json.JSONDecodeError,TypeError, ValueError):
        return []
    
def dump_notas(notas: list[float]) -> str:
    """Converte lista em JSON string."""
    return json.dumps(notas, ensure_ascii=False)

def encontrar_aluno_por_nome(FILEPATH: Path, nome: str) -> dict | None:
    """Encontra um aluno pelo nome (case-insensitive)."""
    nome_n = normalizar_nome(nome)
    df = ler_df(FILEPATH)
    
    if df.empty:
        return None
    
    # Comparação case-insensitive
    nomes = df['nome'].fillna('').astype(str).map(normalizar_nome)
    match = df[nomes == nome_n]
    
    if match.empty:
        return None
    
    return match.iloc[0].to_dict()

# ---------- Funcionalidades ----------
# Função para cadastrar um novo aluno
def cadastrar_aluno(FILEPATH: Path) -> None:
    """Cadastra um novo aluno"""
    
    nome = input("Digite o nome do aluno: ").strip()
    curso = input("Digite o curso do aluno: ").strip()
    
    if not nome or not curso:
        print("Nome e curso não podem ser vazios.")
        return
        
    
    idade_str = input("Digite a idade do aluno: ").strip()
    try:
        idade = int(idade_str)
        if idade <= 0:
            print("Idade deve ser um número positivo.")
            return
    except ValueError:
        print("Idade deve ser um número inteiro.")
        return
        
    df = ler_df(FILEPATH)  # Garantir que o CSV existe e ler o DF atual
    novo_id = obter_proximo_id(df)
    novo = pd.DataFrame([{ 
        'id': novo_id,
        'nome': nome,
        'idade': idade,
        'curso': curso,
        'notas': []
        }])
    
    df = pd.concat([df, novo], ignore_index=True)
    salvar_df(df, FILEPATH)
    print(f"Aluno {nome} cadastrado com sucesso! (ID: {novo_id})")
    
# Função para Listar Alunos
def listar_alunos(FILEPATH):
    """Lista todos os alunos cadastrados"""
    print("-------- Lista de Alunos --------")
    df = ler_df(FILEPATH)
    if df.empty:
        print("Nenhum aluno cadastrado.")
        print("--------------------------------")
        return
    
    # Exibe sem poluir com índice pandas
    for _, row in df.iterrows():
        notas = parse_notas(str(row.get('notas', '[]')))
        print(
            f"ID: {int(row['id'])} | Nome: {row['nome']} | Idade: {int(row['idade']) if pd.notna(row['idade']) else '-'}"
            f" | Curso: {row['curso']} | Notas: {len(notas)}"
        )
    print("--------------------------------")

# Função para buscar um aluno específico pelo nome
def buscar_aluno(FILEPATH: Path):
    """Busca um aluno específico pelo nome"""
    nome = input("Digite o nome do aluno que deseja buscar: ").strip()
    
    aluno = encontrar_aluno_por_nome(FILEPATH, nome)
    if not aluno:
        print("Aluno não encontrado.")
        return
    
    notas = parse_notas(str(aluno.get('notas', '[]')))
    print("-------- Aluno Encontrado --------")
    print(f"ID: {aluno['id']}, Nome: {aluno['nome']}, Idade: {aluno['idade']}, Curso: {aluno['curso']}, Notas: {notas}")

    
# Função para cadastrar notas para cada aluno
def cadastrar_notas(FILEPATH: Path):
    """Cadastra notas para um aluno específico"""
    nome = input("Digite o nome do aluno para cadastrar notas: ").strip()
    
    aluno = encontrar_aluno_por_nome(FILEPATH, nome)
    
    if not aluno:
        print("Aluno não encontrado.")
        return
    
    nota_str = input("Digite a nota do aluno (0 a 10): ").strip()
    try:
        nota = float(nota_str)
    except ValueError:
        print("Entrada inválida. Por favor, insira um número para a nota.")
        return
    
    if not (0 <= nota <= 10):
        print("Nota deve ser entre 0 e 10.")
        return
    
    df = ler_df(FILEPATH)
    aluno_id = int(pd.to_numeric(aluno['id'], errors='coerce'))
    mask = pd.to_numeric(df['id'], errors='coerce') == aluno_id
    
    if not mask.any():
        print("Aluno não encontrado no arquivo (inconsistência).")
        return
    
    notas_atual = parse_notas(str(df.loc[mask, 'notas'].iloc[0]))
    notas_atual.append(nota)
    df.loc[mask, 'notas'] = dump_notas(notas_atual)
    
    salvar_df(df, FILEPATH)
    print(f"Nota {nota:.2f} cadastrada para o aluno {aluno['nome']}.")
    

# Função para calcular a média das notas de cada aluno
def calcular_media(FILEPATH: Path) -> None:
    """Calcula a média das notas de cada aluno"""
    print("-------- Médias --------")
    df = ler_df(FILEPATH)
    if df.empty:
        print("Nenhum aluno cadastrado.")
        print("-----------------------")
        return
    
    for _, row in df.iterrows():
        nome = str(row.get('nome', ''))
        notas = parse_notas(str(row.get('notas', '[]')))
        
        if not notas:
            print(f"Aluno: {nome}, Sem notas cadastradas.")
        else:
            media = sum(notas) / len(notas)
            print(f"Aluno: {nome}, Média: {media:.2f}")
    print("-----------------------")
    
# Função principal para executar o sistema de cadastro de alunos
def main():
    garantir_csv(FILEPATH)  # Garantir que o CSV existe antes de iniciar o menu
    
    while True:
        print(MENU)
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            cadastrar_aluno(FILEPATH)
        elif escolha == "2":
            listar_alunos(FILEPATH)
        elif escolha == "3":
            buscar_aluno(FILEPATH)
        elif escolha == "4":
            cadastrar_notas(FILEPATH)
        elif escolha == "5":
            calcular_media(FILEPATH)
        elif escolha == "6":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")
            
if __name__ == "__main__":
    main()