"""
Docstring for projetos.social_media

Limpando dados de engajamento de mídia social usando pandas.

"""

import pandas as pd
import os

BASE_DIR = os.path.dirname(__file__)
CSV_PATH = os.path.join(BASE_DIR, "..", "docs", "social_media_engagement_data.csv")

raw = pd.read_csv(CSV_PATH, header=None)

# pega só as colunas 1 e 2 (data e impressões)
df = raw.iloc[:, 1:3].copy()

# primeira linha vira cabeçalho
df.columns = df.iloc[0]      # linha 0 = ["DATE", "DAILY IMPRESSIONS"]
df = df[1:]                  # remove linha do header

# ajusta tipos
df["DATE"] = pd.to_datetime(df["DATE"])
df["DAILY IMPRESSIONS"] = pd.to_numeric(df["DAILY IMPRESSIONS"])

print("Limpo:")
print(df.head())

df.to_csv("social_media_engagement_data.csv", index=False)
print("Arquivo limpo salvo: social_media_engagement_data.csv")
