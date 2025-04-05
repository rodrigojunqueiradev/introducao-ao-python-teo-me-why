# %%

arquivo = "data.csv"

with open(arquivo) as open_file:
    lines = open_file.readlines()

# Gerar uma lista
print(lines)
# %%

for l in lines:
    print(l)
# %%

# Gerar um dicionario com a lista gerada
# strip tira o dado solicitado
# split cria um separador no tempo informado

dados = dict()
chaves = lines[0].strip("\n").split(";")

for c in chaves:
    dados[c] = []

dados

# %%

# pular a posição 0
for l in lines[1:]:
    valores = l.strip("\n").split(";")

    # percorrer o i que começa em 0 e vai até o número de valores obtidos
    for i in range(len(valores)):
        dados[chaves[i]].append(valores[i])

dados
# %%

# calcular a média das idades:

idades = []
for i in dados["idade"]:
    idades.append(int(i))

media = sum(idades)/len(idades)
print(media)

# %%
