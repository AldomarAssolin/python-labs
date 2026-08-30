"""
Docstring for projetos.social_media

Limpando dados de engajamento de mídia social usando pandas.

"""

import pandas as pd
import os

BASE_DIR = os.path.dirname(__file__)
CSV_PATH = os.path.join(BASE_DIR, "..", "docs", "dados", "social_media_engagement_data.csv")

raw = pd.read_csv(CSV_PATH, sep=";", header=None)

# acha a linha onde está 'DATE'
header_row = raw[raw[1] == "DATE"].index[0]

# pega só as 3 primeiras colunas a partir do header
data = raw.iloc[header_row:, :3].reset_index(drop=True)

# primeira linha vira cabeçalho
data.columns = data.iloc[0]
data = data[1:]

# ajusta tipos
data["DATE"] = pd.to_datetime(data["DATE"], dayfirst=True)
data["DAILY IMPRESSIONS"] = pd.to_numeric(data["DAILY IMPRESSIONS"])

OUTPUT_PATH = os.path.join(BASE_DIR, "..", "docs", "dados", "social_media_clean.csv")
data.to_csv(OUTPUT_PATH, index=False)
print("Arquivo limpo salvo: social_media_clean.csv")
