# Função para calcular fatorial

def calcularFatorial (numero):
    fatorial = 1
    for contador in range (1, (numero + 1)):
        fatorial *= contador
    return fatorial

        

teste = calcularFatorial (int (input ('Entre um número.')))
print (teste)