# Função para calcular juros

def calcularJuros (capitalInicial, tempoEmAnos, taxaDeJurosAnual):
    rendimento = capitalInicial * taxaDeJurosAnual * tempoEmAnos * 0.01
    capitalFinal = capitalInicial + rendimento
    return (rendimento, capitalFinal)


rendimento, capitalFinal = calcularJuros (1000, 2, 10)
print (rendimento, capitalFinal)