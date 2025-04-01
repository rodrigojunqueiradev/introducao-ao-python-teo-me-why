# Faça um programa de uma sorveteria, onde o usuário pode escolher: 
# a. Tipo de sorvete: casquinha (R$ 1,00), cascão (R$ 2,50), cestinha (R$ 4,00)
# b. Sabor do sorvete: morango, creme, chocolate
# c. Cobertura: caramelho (R$ 1,50), morango (R$ 1,50), chocolate (R$ 1,50), sem cobertura (R$ 0,00)
# Apresente o valor a ser pago.

print("Bem-vindos a sorveteria Sorvete Gelado!")
print("Cardápio: ")
print("Tipo de sorvete: casquinha (R$ 1,00), cascão (R$ 2,50), cestinha (R$ 4,00)")
print("Sabor do sorvete: morango, creme, chocolate")
print("Cobertura: caramelo (R$ 1,50), morango (R$ 1,50), chocolate (R$ 1,50), sem cobertura (R$ 0,00)")
print("Faça o seu pedido abaixo: ")

tipo = input("Informe o tipo desejado: ")
sabor = input("Informe o sabor desejado: ")
cobertura = input("Informe a cobertura desejada: ")

if tipo == "casquinha" and cobertura != "sem cobertura":
    print("Tipo: ", tipo, "+ Sabor: ", sabor, "+ Cobertura: ", cobertura, "= R$ 2,50")

elif tipo == "cascão" and cobertura != "sem cobertura":
    print("Tipo: ", tipo, "+ Sabor: ", sabor, "+ Cobertura: ", cobertura, "= R$ 4,00")

elif tipo == "cestinha" and cobertura != "sem cobertura":
    print("Tipo: ", tipo, "+ Sabor: ", sabor, "+ Cobertura: ", cobertura, "= R$ 5,50")

elif tipo == "casquinha" and cobertura == "sem cobertura":
    print("Tipo: ", tipo, "+ Sabor: ", sabor, "+ Cobertura: ", cobertura, "= R$ 1,00")

elif tipo == "cascão" and cobertura == "sem cobertura":
    print("Tipo: ", tipo, "+ Sabor: ", sabor, "+ Cobertura: ", cobertura, "= R$ 2,50")

elif tipo == "cestinha" and cobertura == "sem cobertura":
    print("Tipo: ", tipo, "+ Sabor: ", sabor, "+ Cobertura: ", cobertura, "= R$ 4,00")

else:
    print("Opção inválida!")