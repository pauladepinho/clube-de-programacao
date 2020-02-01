# Identifica o maior elemento de uma lista

#def maiorElementoDaLista (lista):
#    lista.sort ()
#    return lista [len (lista) - 1]

def maiorElementoDaLista (lista):   
    if (len (lista) == 0):
        return 'A lista está vazia.'

    maiorElemento = lista [0]
    proximoIndice = 1

    while (proximoIndice < len (lista)):
        if (lista [proximoIndice] > maiorElemento):
            maiorElemento = lista [proximoIndice]
        proximoIndice = proximoIndice + 1

    return maiorElemento


minhaLista = []
print (maiorElementoDaLista (minhaLista))

minhaLista2 = [66, 3, 1, 10, 28]
print (maiorElementoDaLista (minhaLista2))

minhaLista2 = [66, 7, 1, 10, 28]
print (maiorElementoDaLista (minhaLista2))

minhaLista2 = [7, 100, 8, 10, 1]
print (maiorElementoDaLista (minhaLista2))
