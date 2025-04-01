# %%
nome = "Rodrigo Junqueira"

for letra in nome:
    print(letra)

# %%
numero = 2
max_numero = 100

for i in range(1, max_numero+1):
    print(numero, "x", i, "=", numero * i)
# %%
# Quais números são divisíveis por 4 no intervalos [4,100]?

for i in range(4, 101):
    if i % 4 == 0:
        print(i, "é divisível por 4")
# %%
