"""
Escreva um programa que crie um dicionário com nomes de frutas como chaves e seus respectivos preços como valores.
Solicite ao usuário o nome de uma fruta e exiba o preço correspondente.
"""

frutas = {
    "maca": 1.5,
    "banana": 2.75,
    "uva": 1.9,
    "pera": 1.25,
    "laranja": 0.65,
    "limao": 1.25,
    "goiaba": 2.15,
    "abacaxi": 3.2,
    "jaca": 5.8
}

print("Bem-vindo ao hortifruti calvo, lugar onde nunca haverá fios de cabelo em suas frutas!")
print("Digite o nome de uma fruta ou pressione 0 para encerrar.")

while True:
    consulta_fruta = input("digite o nome da fruta sem usar acentuação: ").lower()

    if consulta_fruta == "0":
        break
    elif consulta_fruta in frutas:
        print(consulta_fruta, ": R$", frutas[consulta_fruta])
    else:
        print("Fruta não existente")
