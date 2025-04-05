# %%

nome_arquivo = "historia.txt"

with open(nome_arquivo) as open_file:
    conteudo = open_file.read()

print(conteudo)

# forma menos usada:
# # Abre arquivo em formato de leitura:
# open_file = open(nome_arquivo)

# # Lê os dados do arquivo
# conteudo = open_file.read()
# print(conteudo)

# # Fecha o arquivo
# open_file.close()

# %%
