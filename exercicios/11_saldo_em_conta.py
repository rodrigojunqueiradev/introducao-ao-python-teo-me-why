# Faça um programa que recebe uma quantidade indefinida de valores correspondentes a "saldo em conta", mas quando o usuário apertar "enter" sem digitar valor algum, o programa para de receber valores, e exibe a soma de todos o svalores digitados.

saldo_em_conta = 0

while True:
    valor = input("Digite um valor: ")
    
    if valor == "":
        break

    valor = float(valor)
    saldo_em_conta += valor

print("Saldo em conta: R$ ", saldo_em_conta)