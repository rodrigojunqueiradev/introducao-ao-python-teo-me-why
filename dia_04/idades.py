idades = [17, 32, 56, 87]
print(idades)
# Para acessar os métodos de determinada 'coisa', colocar a 'coisa' e colocar um .
idades.append(42)
print(idades)

while True:
    idade = input("Entre com a idade: ")

    if idade == "":
        break

    idades.append(int(idade))

media = sum(idades) / len(idades)
minimo = min(idades)
maximo = max(idades)
quantidade = len(idades)
soma = sum(idades)

print("MEDIA: ", media)
print("MINIMO: ", minimo)
print("MAXIMO: ", maximo)
print("QUANTIDADE: ", quantidade)
print("SOMA: ", soma)