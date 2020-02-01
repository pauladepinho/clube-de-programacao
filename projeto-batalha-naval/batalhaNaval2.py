class BatalhaNaval:

    def __init__ (self):
        
        self.tamanhoDoTabuleiro = 10
        self.meuTabuleiro = Tabuleiro (self.tamanhoDoTabuleiro)
        self.tabuleiroAdversario = Tabuleiro (self.tamanhoDoTabuleiro)
        
        self.meusNavios = self.criarNavios ()
        self.naviosAdversarios = self.criarNavios ()

        self.maquina = True
        self.montarTabuleiro (self.meusNavios)
        self.montarTabuleiro (self.naviosAdversarios)


    def criarNavios (self):

        portaAvioes = Navio (6)
        submarino = Navio (5)
        cruzador = Navio (4)
        fragata = Navio (3)
        corveta = Navio (2)
        return [corveta, fragata, cruzador, submarino, portaAvioes]

        
    def montarTabuleiro (self, navios):

        self.maquina = not self.maquina # maquina = False na primeira vez que o método é chamado e True na segunda.

        for i in range (len (navios)):
            self.colocarNavio (navios [i])


    def colocarNavio (self, navio):

        if (not self.maquina):
            print ('Coloque o navio', navio.nome)
            orientacao = input ('Colocar na horizontal ou na vertical? ')
            x = input ('Primeiro ponto X (de 0 a 9): ')
            y = input ('Primeiro ponto Y (de 0 a 9): ')
            
            self.definirCoordenadas (navio, orientacao, x, y)
            print (navio.nome, 'coordenadas:', navio.coordenadas)

        elif (self.maquina):
            # Gerar coordenadas randomicamente
            pass


    def definirCoordenadas (self, navio, orientacao, x0, y0):
        
        self.x = int (x0)
        self.y = int (y0)
        
        if (orientacao == 'horizontal'):
            self.navioNaHorizontal (navio, self.x, self.y) 
        elif (orientacao == 'vertical'):
            self.navioNaVertical (navio, self.x, self.y)


    def navioNaHorizontal (self, navio, x0, y):

        xn = x0 + navio.tamanho
        for x in range (x0, xn):
            if (x < self.tamanhoDoTabuleiro and y < self.tamanhoDoTabuleiro):
                navio.coordenadas.append ([x, y])
            else:
                print ('O navio está fora do tabuleiro! Escolha outra coordenada!')
                return self.colocarNavio (navio)         
        return navio.coordenadas


    def navioNaVertical (self, navio, x, y0):

        yn = y0 + navio.tamanho
        for y in range (y0, yn):
            if (x < self.tamanhoDoTabuleiro and y < self.tamanhoDoTabuleiro):
                navio.coordenadas.append ([x, y])
            else:
                print ('O navio está fora do tabuleiro! Escolha outra coordenada!')
                return self.colocarNavio (navio)
        return navio.coordenadas



class Tabuleiro:

    def __init__ (self):
   
        self.ataques = []
        
    
'''    def atacar (self, x, y):
        
        if (self.testarBoundaries (x, y)):
            self.ataques.insert ([x, y])
            return ataques      
        else: print ('Fora do limite do tabuleiro.')
     
        
    def estaNoTabuleiro (self, tabuleiro, navio):

        return x < tabuleiro.tamTabuleiro or y < tabuleiro.tamTabuleiro

'''
        

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


'''    def foiAtingido (self):

        if (self.tamanho > 0):
            print (self.nome, 'foi atingido!')
            self.tamanho -= 1
            
        else: print (self.nome, 'naufragou!')'''
        


novoJogo = BatalhaNaval ()




