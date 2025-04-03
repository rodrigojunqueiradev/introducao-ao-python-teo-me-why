# %%

def juros_compostos (capital:float, taxa:float, tempo:int):
    """
    juros_compostos serve para calcular o montante após uma taxa de juros e também saber qual é o valor total do juros.

    capital: 
        número float, representa o valor inicial do aporte
    
    taxa:
        número float, representa a porcentagem do juros, informar em formato percentual, exemplo, 10% representar como apenas 10

    tempo:
        número inteiro, tempo do juros
    """
    montante = capital * (1 + (taxa/100)) ** tempo
    juros = montante - capital
    return montante, juros

juros_compostos(capital=1000, taxa=13, tempo=4)

# %%

# Parei o vídeo em 32:58