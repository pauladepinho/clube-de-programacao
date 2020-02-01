# Função para calcular a área de um retângulo

def areaDoRetangulo (base, altura):
    return base * altura


testeBase = int (input ('base:'))
testeAltura = int (input ('altura:'))

testeDaFuncao = areaDoRetangulo (testeBase, testeAltura)
print (testeDaFuncao)