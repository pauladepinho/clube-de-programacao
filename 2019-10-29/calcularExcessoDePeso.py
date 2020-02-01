# 1 - Recebendo o input do peso de uma bagagem
# e sabendo que o limite do peso é de 50Kg
# e o valor da multa é sempre o excesso multiplicado por 4.
# Faça uma calculadora de peso de bagagem,
# mostrando o excesso e o valor da multa.

def calcularExcessoDePeso (peso):

    if (peso > 50):

        excesso = peso - 50
        multa = excesso * 4
        print ('Excesso de peso:', excesso)
        print ('Valor da multa:', multa)

    else:
        print ('A bagagem não excede o limite de peso estabelecido.')

    return 0


calcularExcessoDePeso (50)
calcularExcessoDePeso (54)
