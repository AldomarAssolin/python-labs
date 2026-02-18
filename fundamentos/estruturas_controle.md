# 🔄 ESTRUTURAS DE CONTROLE

## 🧠 1. CONDICIONAIS

Condicional é decisão.

Na indústria seria:

> “Se a peça passou na inspeção → libera.
> Se não passou → volta para retrabalho.”

Simples. Direto. Objetivo.

---

## ✅ if, elif, else

### 🔹 Estrutura básica

```python
idade = 18

if idade >= 18:
    print("Maior de idade")
```

Se a condição for verdadeira, executa o bloco.

---

### 🔹 if + else

```python
idade = 16

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```

Se não for verdadeiro, executa o else.

---

### 🔹 if + elif + else

```python
nota = 7

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Bom")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")
```

Ele testa na ordem.
Quando encontra uma condição verdadeira, para.

Isso é importante. A ordem importa.

---

# ✅ Comparações

São operadores que retornam True ou False.

| Operador | Significado    |
| -------- | -------------- |
| ==       | Igual          |
| !=       | Diferente      |
| >        | Maior          |
| <        | Menor          |
| >=       | Maior ou igual |
| <=       | Menor ou igual |

Exemplo:

```python
saldo = 100

if saldo == 100:
    print("Saldo exato")
```

---

# ✅ Operadores Lógicos

Agora começa a parte que deixa código interessante.

## 🔹 and (E)

As duas condições precisam ser verdadeiras.

```python
idade = 25
tem_carteira = True

if idade >= 18 and tem_carteira:
    print("Pode dirigir")
```

Se uma falhar → não entra.

---

## 🔹 or (OU)

Uma das duas precisa ser verdadeira.

```python
cargo = "ADMIN"

if cargo == "ADMIN" or cargo == "GERENTE":
    print("Acesso permitido")
```

---

## 🔹 not (negação)

Inverte o valor booleano.

```python
ativo = False

if not ativo:
    print("Usuário inativo")
```

---

## 🔥 Exemplo mais profissional

```python
usuario_logado = True
eh_admin = False

if usuario_logado and not eh_admin:
    print("Usuário comum logado")
```

Aqui você já começa a pensar como arquiteto de regra de negócio.

---

# 🔁 LOOPS

Loop é repetição controlada.

Sem loop, você escreve o mesmo código 100 vezes.

E isso é coisa de quem sofre.

---

## ✅ for com listas

```python
nomes = ["Ana", "Carlos", "Manex"]

for nome in nomes:
    print(nome)
```

Ele percorre cada item da lista.

---

## ✅ for com range()

### 🔹 Range simples

```python
for i in range(5):
    print(i)
```

Saída:

```
0
1
2
3
4
```

---

### 🔹 Range com início e fim

```python
for i in range(1, 6):
    print(i)
```

---

### 🔹 Range com passo

```python
for i in range(0, 10, 2):
    print(i)
```

Vai de 2 em 2.

---

# ✅ while (com controle seguro)

While executa enquanto a condição for verdadeira.

```python
contador = 0

while contador < 5:
    print(contador)
    contador += 1
```

Se você esquecer de atualizar a variável…
Você cria um loop infinito.

E o programa trava.

Isso já derrubou sistema em produção.

---

## 🔐 Controle seguro no while

Sempre garanta:

* condição clara
* variável de controle atualizada
* saída previsível

Exemplo profissional:

```python
tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    print("Tentando conexão...")
    tentativas += 1
```

---

# ✅ break

Interrompe o loop imediatamente.

```python
for numero in range(10):
    if numero == 5:
        break
    print(numero)
```

Para no 5.

---

# ✅ continue

Pula para a próxima iteração.

```python
for numero in range(5):
    if numero == 2:
        continue
    print(numero)
```

Ele ignora o 2.

---

# 🔥 Exemplo aplicado ao seu contexto (produção)

Imagina um controle simples de OP:

```python
ops = [
    {"id": 1, "status": "MONTAGEM"},
    {"id": 2, "status": "INSPECAO"},
    {"id": 3, "status": "MONTAGEM"}
]

for op in ops:
    if op["status"] == "MONTAGEM":
        print(f"OP {op['id']} está em montagem")
```

Isso já é lógica de negócio.

---

# ⚠️ Erros comuns que programadores inseguros cometem

1. Esquecer operador lógico correto
2. Misturar comparação com atribuição (`=` vs `==`)
3. Criar while infinito
4. Colocar condição muito complexa no if

Exemplo ruim:

```python
if idade > 18 and salario > 2000 or cargo == "ADMIN" and ativo:
```

Isso fica ilegível.

Melhor:

```python
eh_maior = idade > 18
tem_salario = salario > 2000
eh_admin = cargo == "ADMIN"

if (eh_maior and tem_salario) or eh_admin:
```

>Clareza > heroísmo.

