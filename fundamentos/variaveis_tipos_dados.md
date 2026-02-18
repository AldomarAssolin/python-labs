# 🔹 1. Variáveis e Tipos Primitivos

Pensa variável como uma **caixa etiquetada** na sua bancada de soldagem.

A etiqueta diz o que tem ali dentro.
O tipo de dado é o “material” que você está armazenando.

Em Python, os principais tipos primitivos são:

* `int` → números inteiros
* `float` → números com casa decimal
* `str` → texto
* `bool` → verdadeiro ou falso

---

## 🔹 int (Inteiro)

```python
idade = 30
quantidade_pecas = 15
```

Aqui:

* `idade` é uma variável
* `30` é um valor do tipo `int`

Você pode verificar o tipo:

```python
print(type(idade))  # <class 'int'>
```

---

## 🔹 float (Número decimal)

```python
peso = 72.5
altura = 1.78
```

Uso típico:

* medidas
* valores financeiros
* médias

```python
print(type(peso))  # <class 'float'>
```

---

## 🔹 str (Texto)

Texto sempre entre aspas:

```python
nome = "Manex"
cargo = 'Desenvolvedor'
```

String é usada para:

* nomes
* mensagens
* descrições
* IDs alfanuméricos

```python
print(type(nome))  # <class 'str'>
```

---

## 🔹 bool (Booleano)

Só existem dois valores possíveis:

```python
ativo = True
aprovado = False
```

Muito usado para:

* validações
* flags
* controle de fluxo

Exemplo:

```python
if ativo:
    print("Usuário está ativo")
```

---

# 🔹 2. Conversão de Tipos (Type Casting)

Aqui começa a parte interessante.

Em sistemas reais, você sempre recebe dados como **string**.
Principalmente de:

* input()
* APIs
* banco
* CSV

Então você precisa converter.

---

## 🔹 Convertendo para int

```python
numero = "10"
numero_convertido = int(numero)

print(numero_convertido + 5)  # 15
```

Se não converter:

```python
print("10" + "5")  # 105 (concatenação)
```

Isso aqui já causou muito bug em sistema financeiro. Muito.

---

## 🔹 Convertendo para float

```python
valor = "19.99"
valor_float = float(valor)

print(valor_float * 2)  # 39.98
```

---

## 🔹 Convertendo para str

```python
idade = 30
idade_texto = str(idade)

print("Minha idade é " + idade_texto)
```

Sem converter daria erro:

```
TypeError: can only concatenate str (not "int")
```

---

## 🔹 Convertendo para bool

Aqui mora armadilha.

```python
bool("False")  # True
```

Por quê?

Porque qualquer string não vazia vira True.

Forma segura:

```python
valor = "True"

ativo = valor.lower() == "true"
```

Isso é padrão profissional.

---

# 🔹 3. Comentários e Boas Práticas

Agora começa a parte que separa iniciante de programador organizado.

---

## 🔹 Comentário simples

```python
# Calcula o valor total da compra
total = quantidade * preco_unitario
```

Comentário explica intenção, não o óbvio.

Ruim:

```python
# soma dois números
resultado = a + b
```

Isso qualquer pessoa vê.

Bom:

```python
# Soma valores já validados e convertidos para float
resultado = valor1 + valor2
```

---

## 🔹 Boas práticas simples

### 1️⃣ Nome de variável claro

Ruim:

```python
x = 10
```

Bom:

```python
quantidade_itens = 10
```

---

### 2️⃣ Use snake_case

Python usa:

```python
valor_total
nome_usuario
data_criacao
```

Nunca:

```python
valorTotal
ValorTotal
```

Isso é Java. Aqui é Python.

---

### 3️⃣ Não misture tipos sem saber

Evite:

```python
resultado = "Total: " + 10
```

Prefira:

```python
resultado = f"Total: {10}"
```

Ou:

```python
resultado = "Total: " + str(10)
```

---

### 4️⃣ Sempre valide antes de converter

```python
entrada = input("Digite um número: ")

if entrada.isdigit():
    numero = int(entrada)
else:
    print("Entrada inválida")
```

