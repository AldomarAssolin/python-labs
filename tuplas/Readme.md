<div align="center">

# 🟦 Python Labs – Módulo de **Tuplas em Python**  
### Estruturas Imutáveis • Lógica • Desempacotamento • Aplicações Reais

![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-blue)  
![Python](https://img.shields.io/badge/Python-3.10%2B-yellow)  
![Categoria](https://img.shields.io/badge/Estudos-Estruturas%20de%20Dados-purple)

</div>

---
## 🔗 Navegação Rápida
- [Objetivo do Módulo](#-objetivo-do-módulo)
- [Por que Tuplas?](#-por-que-tuplas)
- [Estrutura dos Arquivos](#-estrutura-dos-arquivos)
- [Conteúdo Abrangido no Módulo](#-conteúdo-abrangido-no-módulo)
- [Como Executar](#-como-executar)
- [Aplicações Reais de Tuplas](#-aplicações-reais-de-tuplas)
- [Roadmap dos Próximos Módulos](#-roadmap-dos-próximos-módulos)
- [Autor](#-autor)

---
## 🎯 Objetivo do Módulo
Dominar **tuplas em Python** por meio de exemplos e exercícios progressivos, aprendendo:

- Imutabilidade  
- Indexação  
- Desempacotamento  
- Conversão entre tipos  
- Uso de tuplas aninhadas  
- Tuplas como estruturas seguras  
- Aplicação em funções e dados estáticos  

Tuplas são essenciais para escrever código **seguro, performático e organizado**, principalmente quando você não quer que os dados mudem.

---
## 🧠 Por que Tuplas?

Tuplas existem em Python por **três grandes razões**:

### ✔ 1. Imutabilidade  
Depois de criada, a tupla **não pode ser alterada**.  
Isso evita erros e garante integridade dos dados.

### ✔ 2. Performance  
Tuplas são mais rápidas e usam menos memória do que listas.

### ✔ 3. Semântica  
Quando você usa tupla, comunica ao leitor do código:  
> "Isso não deve ser modificado."

São ideais para:
- dados fixos  
- múltiplos retornos de função  
- coordenadas  
- registros estáticos  
- chaves compostas de dicionário

---
## 📁 Estrutura dos Arquivos

```bash
tuplas/
├── tuplas_exemplos.py
└── tuplas_exercicios.py # opcional, caso você crie depois
```


- **tuplas_exemplos.py**  
  Contém exemplos didáticos demonstrando:
  - acesso por índice  
  - tentativa de modificação (erro)  
  - desempacotamento  
  - concatenação  
  - membership tests (`in`)  
  - `count()`  
  - conversão lista ↔ tupla  
  - tupla aninhada  
  - loops com `enumerate`  
  - contagem manual  

---
## 📘 Conteúdo Abrangido no Módulo

### 🟦 **1. Fundamentos das Tuplas**
- Sintaxe de criação  
- Acesso  
- Indexação negativa  
- Desempacotamento (“unpacking”)  
- Métodos nativos: `count()` e `index()`

---

### 🟩 **2. Imutabilidade na prática**
Você verá:

- por que tuplas não podem ser alteradas  
- como capturar erros com `try/except`  
- como proteger dados contra mutações acidentais  

---

### 🟨 **3. Operações com Tuplas**
- Concatenação  
- Repetição  
- Conversão para lista para edição temporária  
- Conversão de lista para tupla para segurança  

---

### 🟥 **4. Tuplas Aninhadas**
- Acesso a elementos internos  
- Estruturas compostas  
- Representações de matrizes e registros  

---

### 🟪 **5. Loops e Desempacotamento Avançado**
- `enumerate()`  
- desempacotamento múltiplo  
- retorno de múltiplos valores  

---
## 🚀 Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/python-labs.git
```

2. Entre na pasta:

```bash
cd python-labs/tuplas
```

3. Execute o arquivo de exemplos:

```bash
python tuplas_exemplos.py
```

---
## 🔧 Aplicações Reais de Tuplas

Tuplas são extremamente úteis em situações como:

### ✔ Dados fixos
Ex.: configurações, estados constantes, coordenadas.

### ✔ Retornos múltiplos de função
Python retorna tuplas naturalmente:
```python
return nome, idade, salario
```


### ✔ Chaves compostas em dicionários
Usado em:

- tabelas hash  
- caches  
- matrizes esparsas  

### ✔ Estruturas de registro
Semelhantes a uma linha de tabela:
```python
("Maria", 35, "Analista")
```


### ✔ Processamento de IA e Machine Learning
Muitos modelos retornam tuplas de:

- probabilidades  
- vetores  
- tokens  

---
## 📈 Roadmap dos Próximos Módulos

| Módulo                                | Status              |
|---------------------------------------|---------------------|
| ✔️ Listas                             | Concluído           |
| 🟦 Tuplas                             | Em desenvolvimento  |
| 🔜 Dicionários                        | Próximo módulo      |
| 🔜 Funções (args, kwargs, closures)   | Planejado           |
| 🔜 Sets & Estruturas Avançadas        | Planejado           |
| 🔜 Mini-projetos usando tudo          | Planejado           |

---
## 👤 Autor

**Aldomar Assolin – Manex**  
Desenvolvedor em formação • ADS • Python • Backend • IA  
Estudando com foco em lógica, estrutura de dados e engenharia de software.

<div align="center">
⭐ Se este módulo te ajudou, deixe uma estrela no repositório!
</div>
