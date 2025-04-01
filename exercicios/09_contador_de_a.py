# Faça um programa que conte quantas vezes a letra "a" aparece em uma palavra.

palavra = input("Digite uma palavra qualquer: ")
conta_a = 0

for letra in palavra:
    if letra == 'a':
        conta_a += 1
    
print("A palavra:", palavra, "tem", conta_a, "letras 'a'")