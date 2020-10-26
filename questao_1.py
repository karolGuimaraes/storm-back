""""
Dado um array de números inteiros, retorne os índices dos
dois números de forma que eles se somem a um alvo específico.

Você pode assumir que cada entrada teria exatamente uma
solução, e você não pode usar o mesmo elemento duas
vezes.
"""

def posicoes_alvo(lista, alvo):
    indices = []
    for index, numero in enumerate(lista):
        if index + 1 < len(lista):
            if lista[index] + lista[index+1] == alvo:
                indices.extend([index, index+1])
                break

    return indices

print(posicoes_alvo([2, 7, 11, 15], 9))