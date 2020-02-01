# Soma números primos menores que n.

def somarNumerosPrimos (n):
    soma = 0

    for i in range (2, n):
        elemento = i
        divisor = 2

        numeroPrimo = False

        while (divisor < elemento and numeroPrimo == False):

            if (elemento % divisor == 0):
                divisor = elemento

            elif (divisor == elemento - 1):
                soma += elemento
                numeroPrimo = True
                print (elemento, 'é primo.')

            divisor += 1

        if (elemento == 2):
            soma += 2
            print (elemento, 'é primo.')

    return soma

print ('Soma dos números primos:', somarNumerosPrimos (100))
