# 📊 Sistema de Cadastro de Alunos e Cálculo de Média

## 🎯 Objetivo

Construir um sistema simples em Python (CLI) para:

* Cadastrar alunos
* Listar alunos cadastrados
* Buscar aluno por nome
* Cadastrar notas
* Calcular média das notas

Este exercício trabalha:

* Estruturas de dados (listas e dicionários)
* Funções
* Validação de entrada
* Tratamento de exceções
* Organização de fluxo com menu interativo

---

## 🧠 Conceitos Praticados

### 1️⃣ Estruturas de Dados

Cada aluno é representado como um dicionário:

```python
{
    "id": 1,
    "nome": "João",
    "idade": 20,
    "curso": "ADS",
    "notas": [8.0, 7.5]
}
```

Todos os alunos ficam armazenados em uma lista:

```python
alunos = []
```

---

### 2️⃣ Validação de Entrada

Regras aplicadas:

* Nome e curso não podem ser vazios
* Idade deve ser número inteiro positivo
* Nota deve estar entre 0 e 10

Exemplo de validação segura:

```python
idade_str = input("Digite a idade: ").strip()

try:
    idade = int(idade_str)
    if idade <= 0:
        print("Idade deve ser positiva.")
except ValueError:
    print("Idade deve ser um número inteiro.")
```

---

### 3️⃣ Funções Utilizadas

| Função              | Responsabilidade                   |
| ------------------- | ---------------------------------- |
| `cadastrar_aluno()` | Cria e adiciona novo aluno         |
| `listar_alunos()`   | Exibe todos os alunos              |
| `buscar_aluno()`    | Busca aluno pelo nome              |
| `cadastrar_notas()` | Adiciona nota a um aluno           |
| `calcular_media()`  | Calcula média das notas            |
| `main()`            | Controla o menu e fluxo do sistema |

---

## 🏗 Estrutura do Programa

```bash
media_alunos.py
└── main()
    ├── cadastrar_aluno()
    ├── listar_alunos()
    ├── buscar_aluno()
    ├── cadastrar_notas()
    └── calcular_media()
```

Fluxo principal:

```bash
Menu → Escolha do usuário → Execução da função → Retorno ao menu
```

---

## 📈 Cálculo da Média

A média é calculada usando:

```python
media = sum(aluno["notas"]) / len(aluno["notas"])
```

Formatação:

```python
print(f"Média: {media:.2f}")
```

Caso o aluno não possua notas:

```bash
Sem notas cadastradas
```

---

## ⚠️ Pontos de Atenção

✔ O sistema está em memória (dados são perdidos ao encerrar)   
✔ Busca por nome pode falhar se houver duplicados  
✔ ID é incremental simples (não persiste entre execuções)

---

## 🚀 Possíveis Evoluções (Próximo Nível)

### 🔹 1. Usar `dataclass`

```python
from dataclasses import dataclass, field

@dataclass
class Aluno:
    id: int
    nome: str
    idade: int
    curso: str
    notas: list[float] = field(default_factory=list)
```

---

### 🔹 2. Separar Camadas

* `model.py` → classe Aluno
* `service.py` → regras de negócio
* `cli.py` → interface com usuário

Assim busco conhecer arquitetura de verdade.

---

### 🔹 3. Persistência em Arquivo (JSON)

Salvar alunos:

```python
import json

with open("alunos.json", "w") as f:
    json.dump(alunos, f)
```

Carregar alunos:

```python
with open("alunos.json", "r") as f:
    alunos = json.load(f)
```

---

## 🧩 Habilidades Desenvolvidas

* Pensamento estruturado
* Organização de fluxo
* Validação de dados
* Controle de exceções
* Modelagem básica de domínio

---

## 📌 Conclusão

Esse exercício parece simples, mas é um excelente treino de:

* Estruturação de funções
* Separação de responsabilidades
* Modelagem de dados
* Preparação para projetos maiores
