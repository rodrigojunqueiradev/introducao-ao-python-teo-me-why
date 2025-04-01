# Faça um programa que vende uma garrafa de água:
# a. Se o cliente escolher água mineral natural, será cobrado R$ 1,50
# b. Se o cliente escolher água mineral com gás, será cobrado R$ 2,50

print("Bem vindo a loja de águas!")
print("Qual água vocês quer comprar?")

agua = int(input("Digite 1 para água mineral natural ou 2 para água mineral com gás: "))

if agua == 1:
    print("Você deve pagar R$ 1,50")

elif agua == 2:
    print("VocÊ deve pagar R$ 2,50")

else:
    print("Não temos essa opção de água.")