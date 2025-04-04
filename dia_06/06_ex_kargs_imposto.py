# kwargs gera um (se comporta como um) dicionário
# kwargs gera parâmetros nomeados de forma infinita

# %%
def calculo_imposto(preco:float, taxa_base:float, **kwargs):
    imposto = preco * taxa_base
    
    for i in kwargs:
        print(i, kwargs[i])
        imposto += preco * kwargs[i]
    
    return imposto

# %%

impostos_gerais = {
    "municipio":0.01,
    "estadual":0.005,
    "nacional":0.001
}

calculo_imposto(100, 0.03, **impostos_gerais, internacional=0.00001)
# %%
