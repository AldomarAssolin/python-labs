"""
Docstring for projetos.library

Projeto simples de uma biblioteca.

"""

import os
from typing import Dict, List
import pandas as pd
import csv

BASE_DIR = os.path.dirname(__file__)
LIB_PATH = os.path.join(BASE_DIR, "..", "docs","library_books.csv")

# Lista que recebe dicionario de livros
livros: List[Dict] = []

# Modelo de dados do livro
def cria_livro(titulo:str, subtitulo:str, descricao:str, autor:str, editora:str, categoria:str, area:str) -> Dict:
    return {
        "titulo": titulo.strip(),
        "subtitulo": subtitulo.strip(),
        "descricao": descricao.strip(),
        "autor": autor.strip(),
        "editora": editora.strip(),
        "categoria": categoria.strip(),
        "area": area.strip()
        
    }
    
# Adiciona Livro na Lista
def add_book(lista, item):
    lista.append(item)
 
# Atualiza livro por nome    
def att_livro(lista,item):
    return True

# Deleta livro por nome
def del_livro(lista, item):
    return True

# Lista todos os livros
def lista_todos_livros(caminho) -> List[Dict]:
    if not os.path.exists(caminho):
        return []
    
    with open(caminho, "r", newline="", encoding="utf-8") as arquivo:
        reader = csv.DictReader(arquivo)
        return list(reader)

# Busca livro pelo titulo
def busca_livro_por_titulo(lista,titulo):
    return

# Busca livro pelo autor
def busca_livro_por_autor(lista,autor):
    return

# Recebe os dados do usuario referente ao livro
def input_livro():
    titulo = input("Digite o Título do livro: ")
    subtitulo = input("Digite o subtitulo do livro: ")
    descricao = input("Digite a descricao do livro: ")
    autor = input("Digite o nome do autor ou autores separados po ','.: ")
    editora = input("Digite o nome da editora: ")
    categoria = input("Digite a categoria do livro: ")
    area = input("Digite a área relacionada do livro, se tiver mais de uma separe por ','.: ")
    return cria_livro(
        titulo,
        subtitulo,
        descricao,
        autor,
        editora,
        categoria,
        area
    )

# novo_livro = input_livro()
novo_livro = {
        "titulo": "Meu Livro",
        "subtitulo": "Ponto COM",
        "descricao": "Livro sobre TI",
        "autor": "Aldomar Assolin",
        "editora": "ebook",
        "categoria": "TI",
        "area": "TI"
}

# Salvar Livro em arquivo CSV
def salvar_livro_csv(caminho:str,livro:dict):
    arq_existente = os.path.exists(caminho)
    
    with open(caminho, "a", newline="", encoding="utf-8") as arquivo:
        writer = csv.DictWriter(arquivo, fieldnames=livro.keys())
        
        if not arq_existente:
            writer.writeheader()
            
        writer.writerow(livro)

# Salva no arquivo CSV
# salvar_livro_csv(LIB_PATH,novo_livro)
# print(f"O livro {novo_livro['titulo']}: {novo_livro['subtitulo']}, escrito por {novo_livro['autor']} foi inserido com sucesso!")

livros = lista_todos_livros(LIB_PATH)

print("==========================")
print("Livros Cadastrados")
print("--------------------------")
for livro in livros:
    print(f"- {livro['titulo']} ({livro['autor']})")




