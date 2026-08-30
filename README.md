
<img src="https://i.ibb.co/XkS3bNzQ/Chat-GPTPython-Labs.png" alt="Chat-GPTPython-Labs" width="460">

# Python Labs

Este é meu laboratório de estudos e evidências práticas em Python, Algoritmos, Dados, IA e Backend.

Organizo este repositorio por competencias, nao por curso ou plataforma. Minha regra de evolucao e:

> Conteudo -> laboratorio -> desafio -> aplicacao -> evidencia

## Dashboard

| Area | Status no repositorio | Onde acompanhar |
| :-- | :-- | :-- |
| Fundamentos de Python | Exercicios e anotacoes existentes | [fundamentos/](fundamentos/) |
| Listas, tuplas e dicionarios | Exemplos e pequenos sistemas de estudo | [listas/](listas/), [tuplas/](tuplas/), [dicionarios/](dicionarios/) |
| Algoritmos | Implementacoes iniciais, incluindo busca binaria e fatorial | [algoritmos/](algoritmos/) |
| Projetos praticos | Aplicacoes simples com CSV, pandas e Streamlit | [projetos/](projetos/) |
| Dados e IA | Trilha documentada e bases de dados organizadas | [dados-ia/](dados-ia/), [docs/trilhas/ia-python.md](docs/trilhas/ia-python.md) |
| Backend com Django | Area criada para estudos e laboratorios futuros | [backend/django/](backend/django/) |
| Documentacao | Trilhas, referencias e dados auxiliares | [docs/](docs/) |

## Trilhas

- [IA com Python](docs/trilhas/ia-python.md): minha trilha prática baseada no cronograma e no prompt de tutor existentes no repositorio.
- [Django Master](docs/trilhas/django-master.md): espaço inicial para registrar estudos de Django sem misturar material de curso com projetos de portfolio.

## Estrutura Atual

```text
python-labs/
├── algoritmos/
├── backend/
│   └── django/
├── dados-ia/
├── dicionarios/
├── docs/
│   ├── dados/
│   ├── referencias/
│   └── trilhas/
├── fundamentos/
├── listas/
├── pages/
├── projetos/
├── tuplas/
├── app.py
├── Dockerfile
├── requirements.txt
└── requirements.lock.txt
```

## Como Executar

Clone o repositorio:

```bash
git clone https://github.com/AldomarAssolin/python-labs.git
cd python-labs
```

Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate
```

No Windows:

```bash
venv\Scripts\activate
```

Instale as dependencias:

```bash
pip install -r requirements.txt
```

Execute um exemplo:

```bash
python fundamentos/variaveis.py
```

Execute a aplicacao Streamlit:

```bash
streamlit run app.py
```

## Projetos e Evidencias

A pasta [projetos/](projetos/) concentra aplicações pequenas, funcionais e explicáveis. Promovo um estudo para essa área quando ele tem objetivo claro, entrada e saída verificáveis, e potencial de demonstrar uma competência.

Exemplos existentes:

- [projetos/library.py](projetos/library.py)
- [projetos/social_media.py](projetos/social_media.py)

## Referencias

- [Introducao a Programacao com Python - Nilo Ney Coutinho Menezes](https://novatec.com.br/livros/introducao-programacao-python/)
- [Entendendo Algoritmos - Aditya Bhargava](https://novatec.com.br/livros/entendendo-algoritmos/)
- [Documentacao Oficial Python](https://docs.python.org/pt-br/3/)
- [Cronograma pessoal de IA com Python](docs/referencias/Cronograma_de_Aprendizado_de_IA_com_Python_para_An.pdf)
- [Prompt de tutor de IA com Python](docs/referencias/Prompt_para_IA__Tutor_de_Aprendizado_de_IA_com_Pyt.pdf)

## Autor

**Aldomar "Manex" Assolin**<br>
Desenvolvedor em evolução | Python, Backend, Dados, IA aplicada e Gestão da Indústria 4.0<br>
[LinkedIn](https://linkedin.com/in/aldomarassolin)<br>
[GitHub](https://github.com/AldomarAssolin)
