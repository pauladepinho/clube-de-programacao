# Remove elementos duplicados da lista

def removerElementosDuplicados (lista):
    if (len (lista) == 0):
        return 'A lista está vazia.'
    
    indice = 0
    proximoIndice = 1
        
    while (indice < len (lista) - 1):
        
        elemento = lista [indice]
    
        while (proximoIndice < len (lista)):
            if (elemento == lista [proximoIndice]):
                lista.pop (proximoIndice)
            proximoIndice = proximoIndice + 1
        indice = indice + 1
        proximoIndice = indice + 1

    return lista

minhaLista = [3, 4, 6, 6, 2, 3, 1, 5, 4]
print ('Lista sem elementos duplicados:', removerElementosDuplicados (minhaLista))

minhaLista2 = []
print (removerElementosDuplicados (minhaLista2))
