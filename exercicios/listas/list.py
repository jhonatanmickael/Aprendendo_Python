list = [
    [12, 435, 23, 1],
    [90, 901, 3, 43],
    [12, 92, 5, 234]
]

#Estou selecionando todos os itens maiores ou iguais a 100:
newlist = [item for linha in list for item in linha if item >= 100]

[print(item) for item in newlist]