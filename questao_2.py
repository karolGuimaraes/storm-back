""""
Um bracket é considerado qualquer um dos seguintes caracteres: (, ), {, }, [ ou ].

Dois brackets são considerados um par combinado se o bracket de abertura (isto
é, (, [ou {) ocorre à esquerda de um bracket de fechamento (ou seja,),] ou} do
mesmo tipo exato. Existem três tipos de pares de brackets : [ ], { } e ( ).

Um par de brackets correspondente não é balanceado se o de abertura e o de
fechamento não corresponderem entre si. Por exemplo, { [ ( ] ) } não é balanceado
porque o conteúdo entre {e} não é balanceado. O primeiro bracket inclui o de
abertura, (, e o segundo inclui um bracket de fechamento desbalanceado,].

Dado sequencias de caracteres, determine se cada sequência de brackets é
balanceada. Se uma string estiver balanceada, retorne SIM. Caso contrário, retorne
NAO.
"""

def balanceado(brackets):
    aberto = ['(', '{', '[']
    fechado = [')', '}', ']']
    lista = []
    for bracket in brackets:
        if bracket in aberto:
            lista.append(bracket)
        elif bracket in fechado:
            if len(lista) > 0 and (aberto[fechado.index(bracket)] == lista[len(lista)-1]):
                lista.pop()
        
    return "SIM" if len(lista) == 0 else "NAO"

print(balanceado("{[()]}"))
print(balanceado("{[(])}"))
print(balanceado("{{[[(())]]}}"))