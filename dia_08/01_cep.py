# %%

import requests # para realizar requisições na web
import json # para tratar de listas/dicionários para arquivos json
from tqdm import tqdm # status da execução do processo ; Não é performático!
import pandas as pd

ceps =[
    "18270250",
    "18270353",
    "01519000",
    "13329120",
    "14400760"
]

# o {cep} é um placeholder
url = "https://viacep.com.br/ws/{cep}/json/" #url base da API

dados = []

# lista para navegar entre os ceps
for i in tqdm(ceps):
    resposta = requests.get(url.format(cep=i))
    if resposta.status_code == 200:
        dados.append(resposta.json())

dados

# %%

dataset = pd.DataFrame(dados)
dataset.to_csv("ceps.csv", sep=";")

# %%

# criar e abrir o arquivo de ceps.json
with open("ceps.json", "w", encoding="utf-8") as open_file:
    json.dump(dados, open_file, ensure_ascii=False, indent=4)

# %%
