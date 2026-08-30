# 🔍 Busca Binária – Entendendo a lógica passo a passo

Este documento registra **meu raciocínio** para entender a *busca binária* de forma intuitiva, indo além do código.

A ideia é que, no futuro, eu (Manex) volte aqui e relembre **não só a implementação**, mas principalmente **por que o algoritmo funciona** e **por que ele é tão rápido**.

---

## 🧠 Ideia central da busca binária

A busca binária funciona em **listas ORDENADAS**.

Em vez de olhar elemento por elemento (como na busca linear), ela segue sempre o mesmo raciocínio:

> **“Olha o elemento do meio e decide se continua na metade da esquerda ou da direita.”**

Ou seja, a cada passo ela **joga fora metade da lista**.

Por isso ela é tão eficiente.

---

## 🧩 Exemplo simples: lista de 1 a 99

Considere esta lista:

```python
lista = [1, 2, 3, ..., 99]
```

Quero buscar o número **23** usando busca binária.

1. **baixo = 0**, **alto = 98**, lista tem 99 elementos  
2. calculo o `meio`:

```python
meio = (baixo + alto) // 2
```

Uso `//` (divisão inteira), porque índices de lista **devem ser inteiros**.

---

## 🔎 Simulando a busca do número 23

Passo a passo:

1. `baixo = 0`, `alto = 98`  
   - `meio = 49`  
   - `lista[49] = 50`  
   - 50 **> 23** **-->** Aqui é descartado do **50** pra cima.

2. `baixo = 0`, `alto = 48`  
   - `meio = 24`  
   - `lista[24] = 25`  
   - 25 **> 23** **-->** Aqui é descartado do **25** pra cima.

3. `baixo = 0`, `alto = 23`  
   - `meio = 11`  
   - `lista[11] = 12`  
   - 12 **< 23** **-->** Aqui é descartado do **12** pra baixo.

4. `baixo = 12`, `alto = 23`  
   - `meio = 17`  
   - `lista[17] = 18`  
   - 18 **< 23** **-->** Aqui é descartado do **18** pra baixo.

5. `baixo = 18`, `alto = 23`  
   - `meio = 20`  
   - `lista[20] = 21`  
   - 21 **< 23** **-->** Aqui é descartado do **21** pra baixo.

6. `baixo = 21`, `alto = 23`  
   - `meio = 22`  
   - `lista[22] = 23` ✔ encontrado

---

## 📉 Comparando com a busca linear

Busca linear verificaria:

```
1, 2, 3, ..., 23 → 23 comparações
```

Busca binária realizou **6** comparações.

---

## 📏 Por que isso é tão rápido?

Porque a busca binária tem complexidade:

```
O(log₂ n)
```

Exemplos:

- 99 elementos → ~6 passos  
- 1 milhão de elementos → ~20 passos  
- 1 bilhão de elementos → ~30 passos  

Ela descarta metade da lista em cada passo.

É como fatorar um número:
```bash
1000 | 2
500  | 2
250  | 2
125  | 2
62   | 2
31   | 2
15   | 2
7    | 2
3    | 2
1
```

Contando quantas divisões foram feitas, temos 9 passos ou 9 operações.


---

## 🧾 Implementação da função em Python

```python
def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1

    return None
```

---

## 🎬 Versão visual com Streamlit

Criei uma página no Python Labs que:
[Veja aqui!](https://python.manexlabs.dev/Algoritmos)

- mostra passo a passo (baixo, alto, meio, chute)
- anima cada iteração com delay
- exibe tabela final dos passos

Essa visualização fortalece a compreensão do algoritmo.

---

## ✔ Conclusão

Busca binária não é sobre “achar um número rápido”.  
É sobre **descartar o que não importa** e reduzir o problema pela metade até chegar na resposta.

Este documento registra minha evolução real entendendo esse conceito.

