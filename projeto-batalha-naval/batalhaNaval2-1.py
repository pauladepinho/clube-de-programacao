POSICOES_VALIDAS = ['horizontal', 'vertical']

class BatalhaException(Exception):
	
	def __init__(self, *args, **kwargs):
		super(BatalhaException, self).__init__(*args, **kwargs)		
		print(self)

	def __str__(self):
		return 'Erro do jogo: %s' % self.args[0]

class BatalhaNaval:

    def __init__ (self):
        
        self.tamanhoDoTabuleiro = 10
        self.meuTabuleiro = Tabuleiro (self.tamanhoDoTabuleiro)
        self.tabuleiroAdversario = Tabuleiro (self.tamanhoDoTabuleiro)
        
        self.meusNavios = self.criarNavios ()
        self.naviosAdversarios = self.criarNavios ()

        self.maquina = True

        self.montarTabuleiro (self.meuTabuleiro, self.meusNavios)
        self.montarTabuleiro (self.tabuleiroAdversario, self.naviosAdversarios)

    def coletarInput(self, msg, validation):
       entrada = input(msg)

       if validation(entrada):
           return entrada
       else:
           raise BatalhaException('Entrada invalida')



    def criarNavios (self):

        portaAvioes = Navio (6)
        submarino = Navio (5)
        cruzador = Navio (4)
        fragata = Navio (3)
        corveta = Navio (2)
        return [corveta, fragata, cruzador, submarino, portaAvioes]

        
    def montarTabuleiro (self, tabuleiro, navios):

        self.maquina = not self.maquina # maquina = False na primeira vez que o método é chamado e True na segunda.

        for i in range (len (navios)):
            
            self.colocarNavio (tabuleiro, navios [i])                           


    def colocarNavio (self, tabuleiro, navio):

        validationPosicao = lambda x: x in POSICOES_VALIDAS
        validationInteiro = lambda x: x.isdigit()

        if (not self.maquina):

            try:
                print ('Coloque o navio', navio.nome)

                orientacao = self.coletarInput('Colocar na horizontal ou na vertical? ', validationPosicao)
                # orientacao = input ('Colocar na horizontal ou na vertical? ')
                # if orientacao not in POSICOES_VALIDAS:
                #     raise BatalhaException('Orientacao invalida')

                x = self.coletarInput('Primeiro ponto x ', validationInteiro)
                y = self.coletarInput('Primeiro ponto y ', validationInteiro)
                # x = input ('Primeiro ponto X: ')
                # y = input ('Primeiro ponto Y: ')
            
                self.definirCoordenadas (tabuleiro, navio, orientacao, x, y)
                print (navio.nome, 'coordenadas:', navio.coordenadas)

            except BatalhaException:
               self.colocarNavio(tabuleiro, navio)
                        

        elif (self.maquina):
            pass
            # Gerar coordenadas randomicamente


    def definirCoordenadas (self, tabuleiro, navio, orientacao, x0, y0):
                
        self.x = int (x0)
        self.y = int (y0)
        
        if (orientacao == 'horizontal'):
            self.navioNaHorizontal (tabuleiro, navio, self.x, self.y) 
        elif (orientacao == 'vertical'):
            self.navioNaVertical (tabuleiro, navio, self.x, self.y)


    def navioNaHorizontal (self, tabuleiro, navio, x0, y):

        xn = x0 + navio.tamanho
        for x in range (x0, xn):
            if (x < self.tamanhoDoTabuleiro and y < self.tamanhoDoTabuleiro):
                navio.coordenadas.append ([x, y])
            else:
            	raise BatalhaException('O navio está fora do tabuleiro! Escolha outra coordenada!')
                # print ('O navio está fora do tabuleiro! Escolha outra coordenada!')
                # return self.colocarNavio (tabuleiro, navio)         
        return navio.coordenadas


    def navioNaVertical (self, tabuleiro, navio, x, y0):

        yn = y0 + navio.tamanho
        for y in range (y0, yn):
            if (x < self.tamanhoDoTabuleiro and y < self.tamanhoDoTabuleiro):
                navio.coordenadas.append ([x, y])
            else:
                print ('O navio está fora do tabuleiro! Escolha outra coordenada!')
                return self.colocarNavio (tabuleiro, navio)
        return navio.coordenadas



class Tabuleiro:

    def __init__ (self, tamanhoDoTabuleiro):

        self.tamTabuleiro = tamanhoDoTabuleiro    
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




