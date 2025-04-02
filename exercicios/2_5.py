"""
Considere a lista: [120, "Python", 120.01, "asw", [10,20]]
Faça um programa que retorne as seguintes informações:
- Elemento na posição -1 da lista
- Elemento na primeira posição da lista
- O último caractere do segundo elemento da lista
"""

lista = [120, "Python", 120.01, "asw", [10,20]]

# Elemento na posição -1 da lista
print("Elemento -1:", lista[-1])

# Elemento na primeira posição da lista
print("Primeiro elemento:", lista[0])

# O último caractere do segundo elemento da lista
print("Último caractere do segundo elemento:", lista[1][-1])