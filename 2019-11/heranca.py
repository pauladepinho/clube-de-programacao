class Veiculo:

    #cores = ['vermelho', 'amarelo', 'rosa', 'azul', 'preto']
    numeroDeVeiculos = 0
    
    def __init__ (self, cor, marca): # O primeiro argumento é sempre o próprio objeto (self).
        print ('Veículo criado.')
        self.__cor = cor
        self.marca = marca
        Veiculo.numeroDeVeiculos += 1
        print ('Veículo da cor', self.__cor, 'criado.')

    def getCor (self):
        return self.__cor

    def imprimirInformacoes (self):
        print (self.__cor, self.marca)
        
    def andar (self, metros):
        print ('Andei', metros, 'metros.')

    def __del__ (self): # Método destrutor.
        print ('Veículo da cor', self.__cor, 'destruído.')
        Veiculo.numeroDeVeiculos -= 1
        print ('Quantidade de veículos:', Veiculo.numeroDeVeiculos)

    @classmethod
    def getNumeroDeVeiculos (cls):
        return cls.numeroDeVeiculos

class Barco (Veiculo):

    def andar (self, metros):
        print ('Naveguei', metros, 'metros.')

'''
def f ():
    x = Veiculo ('rosa', 'fiat')
    
meuVeiculo = Veiculo ('vermelho', 'Honda')
meuVeiculo.andar (10)
f ()
meuVeiculo.imprimirInformacoes ()
meuVeiculo.cor = 'amarelo'
'''
