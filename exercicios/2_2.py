# Faça um programa que receba um número. Verifique se o número informado é par ou ímpar. Exiba o resultado da seguinte maneira: "O número x é ímpar ou O número x é par"

def verifica_par(x:int):
    if x % 2 == 0:
        print("O número", x, "é par")
    else:
        print("O número", x, "é ímpar")

numero = int(input("Informe um número: "))
verifica_par(numero)