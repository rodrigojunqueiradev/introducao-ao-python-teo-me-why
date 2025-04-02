# Escreva um programa que receba uma lista de números do usuário e conte quantas vezes um número específico aparece na lista.
# Solicite ao usuário um número e exiba a contagem.

lista = []
tamanho_lista = input("Quantos números sua lista vai ter? ")
tamanho_lista = int(tamanho_lista)
i = 1
conta_num = 0

while i <= tamanho_lista:
    item_lista = input("Informe um número: ")
    item_lista = int(item_lista)
    lista.append(item_lista)
    i += 1

print(lista)
verifica_numero = input("Qual número você deseja consultar? ")
verifica_numero = int(verifica_numero)

for numero in lista:
    if verifica_numero == numero:
        conta_num += 1
    
print("O número", verifica_numero, "apareceu ", conta_num, "vezes")