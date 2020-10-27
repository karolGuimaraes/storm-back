""""
Digamos que você tenha um array para o qual o elemento i
é o preço de uma determinada ação no dia i.

Se você tivesse permissão para concluir no máximo uma
transação (ou seja, comprar uma e vender uma ação), crie
um algoritmo para encontrar o lucro máximo.

Note que você não pode vender uma ação antes de
comprar.
"""

def lucro_maximo(transacoes):
    lucro = 0
    preco_min = transacoes[0]
    for preco in transacoes:
        preco_min = min(preco, preco_min)
        lucro = max(lucro, preco - preco_min)
    return lucro
    
print(lucro_maximo([7, 1, 5, 3, 6, 4]))
print(lucro_maximo([7, 6, 4, 3, 1]))