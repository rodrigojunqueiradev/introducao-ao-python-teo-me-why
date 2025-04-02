# Escreva um programa que solicite ao usuário frases. Para parar de solicitar frases ele pode apenas apertar enter.
# Seu programa deve apresentar cada frase e quantas vezes ela foi repetida.

dados = {}

while True:
    frase = input("Informe uma frase: ")

    if frase == "":
        break

    if frase not in dados:
        dados[frase] = 1
    else:
        dados[frase] += 1

for i, j in dados.items():
    print(i, "apareceu", j, "vezes")