# Ordena uma lista
# Autora: Paula de Pinho Monteiro

def ordenarLista (lista):

    if (len (lista) == 0):
        return 'A lista está vazia.'

    indice = 0
    proximoIndice = 1
    menorElemento = lista [indice]
    
    while (indice < len (lista) - 1):   
        while (proximoIndice < len (lista)):
            if (lista [proximoIndice] <= menorElemento):
                menorElemento = lista [proximoIndice]
                indiceMenorElemento = proximoIndice
                print ('índice do menor elemento:', indiceMenorElemento)
            proximoIndice = proximoIndice + 1
            print ('próximo índice:', proximoIndice)
        print ('menor elemento:', menorElemento)
        print ('índice do menor elemento:', indiceMenorElemento)

        lista.pop (indiceMenorElemento)
        lista.insert (indice, menorElemento)

        indice = indice + 1
        proximoIndice = indice + 1
        menorElemento = lista [indice]
        indiceMenorElemento = indice

        print (lista)
        print ('índice:', indice)
        print ('próximo índice:', proximoIndice)
    return lista


minhaLista = [3, 4, 6, 6, 2, 3, 1, 5, 4]
print (ordenarLista (minhaLista))
