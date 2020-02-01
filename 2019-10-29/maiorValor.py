# 2 - Recebendo três valores do usuário.
# Faça um programa que indique qual o maior valor dos inputs recebido.

def maiorValor (inputs):

    maiorElemento = inputs [0]
    proximoIndice = 1

    print (maiorElemento)

    while (proximoIndice < len (inputs)):

        if (inputs [proximoIndice] > maiorElemento):
            maiorElemento = inputs [proximoIndice]
            print (maiorElemento)

        proximoIndice = proximoIndice + 1

    return maiorElemento

inputs = [0, 0, 0]
inputs [0] = int (input ('Digite o primeiro número.'))
inputs [1] = int (input ('Digite o segundo número.'))
inputs [2] = int (input ('Digite o terceiro e último número.'))

print (type (inputs [0]))

print ('O maior valor é:', maiorValor (inputs))
