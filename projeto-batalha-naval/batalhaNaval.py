class BatalhaNaval:

    def __init__ (self):

        self.criarNavios ()
        '''self.printInfosDosNavios ()'''

        print ('Meu tabuleiro:')
        self.meuTabuleiro = Tabuleiro (10)
        print ('Tabuleiro adversário:')
        self.tabuleiroAdversario = Tabuleiro (10)

        '''self.setupDoTabuleiro ()'''


    def criarNavios (self):

        self.portaAvioes = Navio (6)
        self.submarino = Navio (5)
        self.cruzador = Navio (4)
        self.fragata = Navio (3)
        self.corveta = Navio (2)   
        
    
    '''def printInfosDosNavios (self):

        print ('Navios:')
        self.portaAvioes.printInfos ()
        self.submarino.printInfos ()
        self.cruzador.printInfos ()
        self.fragata.printInfos ()
        self.corveta.printInfos ()
        print ()'''        
    
'''
    def setupDoTabuleiro (self):

        print ('Bem-vindo ao jogo Batalha Naval!')
        print ('Vamos começar colocando os navios no seu tabuleiro!')

        for i in range (0, 5):
    
            tamanhoDoNavio = input ('Qual navio você quer posicionar agora? (Digite o tamanho dele.)\n')
            x1 = input ('Digite x1 ')
            x2 = input ('x2 ')
            y1 = input ('y1 ')
            y2 = input ('y2 ')
    
            self.posicionarNavio (int (tamanhoDoNavio), int (x1), int (x2), int (y1), int (y2))


    def posicionarNavio (self, tamanhoDoNavio, x1, x2, y1, y2):

        #self.tamanhoDoNavio = tamanhoDoNavio
        #self.x = x1
        #self.y = y1

        if (self.tamanhoDoNavio - 1 == x2 - x1 and y1 == y2): #horizontal
            for i in range (self.tamanhoDoNavio):
                self.meuTabuleiro [self.x] [self.y + i] = 1

        elif (self.tamanhoDoNavio - 1 == y2 - y1 and x1 == x2): #vertical
            for i in range (self.tamanhoDoNavio):
                self.meuTabuleiro [self.x + 1] [self.y] = 1


        print (self.meuTabuleiro)
'''


class Taluleiro ():

    def __init__ (self, tamanhoDoTabuleiro):

        self.tamTabuleiro = tamanhoDoTabuleiro
        '''self.tabuleiro = self.criarTabuleiro ()'''

        self.ataques = []

'''
    def criarTabuleiro (self):
      
        matriz = [[0 for x in range (self.tamTabuleiro)] for y in range (self.tamTabuleiro)]
        #print (matriz)
        #print ()
        return matriz
'''

    def atacar (self, x, y):

        self.ataques.insert ([x,y])
        return ataques
    

    def testarBoundaries ():

        
    
                

class Navio ():

    def __init__ (self, tamanho):

        self.tamanho = tamanho
        self.nome = self.nomearNavio (self.tamanho)
        self.coordenadas = []


    def nomearNavio (self, tamanho):

        if (self.tamanho == 2): return 'Corveta'
        elif (self.tamanho == 3): return 'Fragata'
        elif (self.tamanho == 4): return 'Cruzador'
        elif (self.tamanho == 5): return 'Submarino'
        elif (self.tamanho == 6): return 'Porta-Aviões'


    def definirCoordenadas (orientacao, x0, y0):
        
        #self.orientacao = orientacao
        #self.x0 = x0
        #self.y0 = y0
        
        if (orientacao == 'horizontal'):
            self.navioNaHorizontal (x0, y0)
            
        elif (orientacao == 'vertical'):
            self.navioNaVertical (x0, y0)


    def navioNaHorizontal (self, x0, y0):

        self.y = y0
        self.x0 = x0
        self.xn = self.x0 + self.tamanho

        for x in range (self.x0, self.xn):
            self.coordenadas.insert ([x, self.y])

        return self.coordenadas


    def navioNaVertical (self, x0, y0):

        self.x = x0
        self.y0 = y0
        self.yn = self.y0 + self.tamanho

        for y in range (self.y0, self.yn):
            self.coordenadas.insert ([self.x, y])

        return self.coordenadas


'''    def printInfos (self):

        print (self.nome + ', tamanho: ' + str (self.tamanho))
        print ('Coordenadas:', self.coordenadas)'''


    def foiAtingido (self):

        if (self.tamanho > 0):
            print (self.nome, 'foi atingido!')
            self.tamanho -= 1
            
        else: print (self.nome, 'naufragou!')
        


novoJogo = BatalhaNaval ()




