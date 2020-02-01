# Matricular alunos.

import json

class Arquivo:
    ''' Matricula novos alunos. '''

    def __init__ (self, nome, idade, matricula):

        self.nome = nome
        self.idade = idade
        self.matricula = matricula

        self.novoAluno = {'nome': self.nome, 'idade': self.idade,
                     'matricula': self.matricula}
        
    def incluirNaLista (self):
        ''' Cria arquivo com a lista de todos os alunos. '''

        json.dumps (self.novoAluno)
        f = open ('Lista de Alunos.text', 'a')
        f.write (self.novoAluno ['nome'] + " | " + str (self.novoAluno ['idade'])
                 + " | " + str (self.novoAluno ['matricula']) + '\n')
        f.close ()
        
        self.criarFicha ()
        self.ordenarLista ()


    def ordenarLista (self):
        ''' Ordena os alunos alfabeticamente. '''

        lista = []
        with open ('Lista de Alunos.text', 'r') as f:
            for line in f:
                lista.append (line)

        lista.sort ()

        f = open ('Lista de Alunos.text', 'w') # Apaga dados fora de ordem.
        f.close ()
        
        with open ('Lista de Alunos.text', 'a') as f:
            for i in lista:
                f.write (i)

        
    def criarFicha (self):
        ''' Cria um arquivo cada novo aluno matriculado. '''

        f = open (self.novoAluno ['nome'] + '.txt', 'a')
        f.write ('Aluno | Idade | Matrícula' + '\n')
        f.write (self.novoAluno ['nome'] + " | " + str (self.novoAluno ['idade'])
                 + " | " + str (self.novoAluno ['matricula']) + '\n')
        f.close ()
        

nome = input ('Nome: ')
idade = input ('Idade: ')
matricula = input ('Matrícula: ')

aluno = Arquivo (nome, idade, matricula)
aluno.incluirNaLista ()