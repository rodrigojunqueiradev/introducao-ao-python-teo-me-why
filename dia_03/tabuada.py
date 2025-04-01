numero = int(input("Informe o número que quer calcular a tabuada: "))
tabuada = 0
limite = int(input("Informe o valor limite da tabuada: "))

print("Tabuada do ", numero)
while tabuada <= limite:
    print(numero, "x", tabuada, "=", numero * tabuada)
    tabuada += 1