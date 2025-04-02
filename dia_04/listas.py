# %%

# Listas = sempre usar colchetes

# Uma maneira de definir listas:
idades = [28, 42, 43, 35, 39, 28, 38]

print(idades)
print(len(idades))

# %%

lista_qualquer = ["Rodrigo", 32, "Junqueira", "sei la", 1.80, 90, "Tobi", "Lucky", True]
print(lista_qualquer)
print(len(lista_qualquer))
type(lista_qualquer)
# %%

# Acessar as posições usando indíces:

print(lista_qualquer[0])
print(lista_qualquer[1])
print(lista_qualquer[2])
print(lista_qualquer[3])
print(lista_qualquer[4])
print(lista_qualquer[5])
print(lista_qualquer[6])
print(lista_qualquer[7])
print(lista_qualquer[8])
print(lista_qualquer[-1])
print(lista_qualquer[-9])
print(lista_qualquer[0:2])
print(lista_qualquer[0:4])
print(lista_qualquer[1:4])
print(lista_qualquer[1:-4])
# %%
print("Soma idade: ", sum(idades))
print("Média idades: ", sum(idades)/len(idades))
print("Maior idade: ", max(idades))
print("Menor idade: ", min(idades))
# %%
lista_qualquer[3][0:3] #sei

lista_qualquer2 = ["Rodrigo", 32, ["Tobi", "Lucky"], ["Final Fantasy", "Harry Potter", "Senhor dos Anéis"], 1992]
print(len(lista_qualquer2))
print(lista_qualquer2[2])
print(lista_qualquer2[2][0])

cachorros = lista_qualquer2[2]
print(cachorros[0])
print(cachorros[1])

# lista [start : stop]