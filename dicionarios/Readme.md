## 📇 Agenda de Contatos em Python (CRUD + CSV)
### 🧠 Visão Geral

Este projeto implementa uma **Agenda de Contatos em Python**, utilizando:

>- Estruturas de dados (list e dict)
>- Operações CRUD (Create, Read, Update, Delete)
>- Persistência de dados em arquivo CSV
>- Interface via menu no terminal

O objetivo do projeto é **praticar fundamentos de Python**, organização de código e lógica de sistemas reais, simulando o funcionamento de uma pequena aplicação.

### 🎯 Funcionalidades

>- ➕ Adicionar contato
>- 📄 Listar contatos
>- 🔍 Buscar contato por email
>- ✏️ Atualizar contato
>- ❌ Excluir contato
>- 💾 Salvar e carregar contatos em CSV

### 📁 Estrutura do Projeto
```bash
dicionarios/
 └── agenda.py

docs/
 └── agenda.csv
```

✨ `agenda.py` → lógica do sistema (CRUD, menu, validações)

✨ `agenda.csv` → persistência dos dados

---

### 🧩 Modelo de Dados

Cada contato é representado por um **dicionário**:

```python
{
    "nome": "Alice",
    "telefone": "11999999999",  # ou None
    "email": "alice@email.com"
}
```

- nome → obrigatório

- email → obrigatório e identificador único

- telefone → opcional

O email é sempre salvo normalizado (`strip()` + `lower()`).

---

### 🔄 Fluxo do Sistema

1. Ao iniciar o programa:
    - os contatos são carregados do arquivo CSV para a memória

2. O usuário interage com o menu

3. Operações CRUD são feitas em memória

4. Após Create / Update / Delete, a agenda é salva novamente no CSV

5. Ao sair, os dados permanecem persistidos

### 📜 Menu de Opções
```bash
1 - Adicionar contato
2 - Listar contatos
3 - Buscar contato por email
4 - Atualizar contato
5 - Excluir contato
0 - Sair
```

---

### 🛠️ Decisões Técnicas Importantes

> - O CSV é sempre reescrito por completo (modo "w")\
> → evita duplicação e inconsistência\
>
>- Funções de negócio não imprimem nada\
>→ mensagens ficam no menu (UI)\
>
>- Uso de exceções (ValueError) para tratar erros\
> - Separação clara entre:\
>   - entrada de dados
>   - regras de negócio
>   - persistência
>   - exibição

## 🚀 Como Executar

1. Certifique-se de ter Python 3 instalado

2. Execute o arquivo:

```bash
python dicionarios/agenda.py
```

3. O arquivo `docs/agenda.csv` será criado automaticamente, se não existir

## 🧪 Próximos Passos (Roadmap)

- ⬜ Melhorar validação de email

- ⬜ Permitir atualização parcial (Enter para manter valor)

- ⬜ Refatorar em módulos (crud.py, storage.py, ui.py)

- ⬜ Criar versão com Streamlit (PythonLabs)

- ⬜ Adicionar testes automatizados

## 👤 Autor

**Aldomar Assolin – Manex**  
Desenvolvedor em formação • ADS • Python • Backend • IA  
Estudando com foco em lógica, estrutura de dados e engenharia de software.

<div align="center">
⭐ Se este módulo te ajudou, deixe uma estrela no repositório!<br>
🧿 Foco em Python, lógica, backend e construção de sistemas reais
</div>