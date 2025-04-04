#args gera uma lista

def soma(a:float, b:float, *args):
    valores = [a,b] + list(args)
    return sum(valores)

def media(a:float, b:float, *args) -> float:
    return soma(a,b,*args) / (len(args)+2)

a = float(input("Número 1: "))
b = float(input("Número 2: "))
c = float(input("Número 3: "))
d = float(input("Número 4: "))

print("Média:", media(a,b,c,d))