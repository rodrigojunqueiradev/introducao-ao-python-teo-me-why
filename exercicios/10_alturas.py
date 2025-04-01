# Faça um programa que receba 4 alturas usando um laço de repetição e realize a soma dessas alturas.

soma = 0
count = 4

while count > 0:
    altura = input("Informe sua altura: ")
    altura = float(altura)
    soma += altura
    count -= 1

print("Soma das alturas: ", soma)