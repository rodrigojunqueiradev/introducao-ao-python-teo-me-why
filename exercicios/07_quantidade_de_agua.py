# Faça um programa que vende uma garrafa de água:
# a. Se o cliente escolher água mineral natural, será cobrado R$ 1,50
# b. Se o cliente escolher água mineral com gás, será cobrado R$ 2,50
# c. Pergunte a quantidade

print("Bem vindo a loja de águas!")
print("Qual água vocês quer comprar?")

escolha = int(input("Digite 1 para água mineral natural ou 2 para água mineral com gás: "))
quantidade = int(input("Quantas unidades você deseja? "))

if escolha == 1:
    print("Você deve pagar: R$ ", 1.5 * quantidade)

elif escolha == 2:
    print("Você deve pagar R$: ", 2.5 * quantidade)

else:
    print("Não temos essa opção de água.")