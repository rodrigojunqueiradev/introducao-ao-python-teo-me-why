# %%

# Dicionários = Pares de chave:valor

dados_rodrigo = {
    "nome": "Rodrigo",
    "sobrenome": "Junqueira",
    "idade": 32,
    "animal": "Tobi",
    "salario": 4000,
    "filhos": False,
    "formacao": ["analista de sistemas", "professor de matematica", "analista de dados"],
    "cargos": [
        {"nome": "analista jr", "empresa": "djsystem"},
        {"nome": "professor", "empresa": "bmq"},
        {"nome": "analista de sistemas jr", "empresa": "sustenidos"}
    ]
}

nome_completo = dados_rodrigo["nome"] + " " + dados_rodrigo["sobrenome"]

print(dados_rodrigo)
print(dados_rodrigo["nome"])
print(dados_rodrigo["sobrenome"])
print(nome_completo)

# Pegar a última formação: 
print(dados_rodrigo["formacao"][-1])

# Pegar o último trabalho:
print(dados_rodrigo["cargos"][-1])

# Pegar somenta a última empresa do última cargo:
print(dados_rodrigo["cargos"][-1]["empresa"])

dados_rodrigo["estado civil"] = "solteiro"

print(dados_rodrigo)


# %%

#Como buscar apenas os nomes das chaves?
print(dados_rodrigo.keys())

# %%

#Como buscar apenas os valores das chaves?
print(dados_rodrigo.values())
# %%

for i in dados_rodrigo:
    print(i, "->", dados_rodrigo[i])
# %%

for item in dados_rodrigo.items():
    print(item)
# %%

for chave, valor in dados_rodrigo.items():
    print(chave, ":", valor)
# %%
