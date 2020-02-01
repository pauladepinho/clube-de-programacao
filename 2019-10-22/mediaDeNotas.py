# Calcula a média de N notas salvas em uma lista

def mediaDeNotas (lista):
    
    indice = 0
    soma = 0
    
    while (indice < len (lista)):     # Soma os elementos da lista
        
           elemento = lista [indice]
           soma += elemento
           indice = indice + 1
           
    return soma/len (lista)     # Divide a soma pelo número de elementos


notas = [3,7,9,5,10,6]
print (mediaDeNotas (notas))


def somarNotasAlunos (aluno):
    for nota in aluno ['notas']:
        somaDasNotas +=nota
    return somaDasNotas


def calcularMediaDaTurma (turma):
    numeroDeNotas = len (turma) + len (turma [0] ['notas'])
    somaDasNotas = 0.0
    for aluno in turma:
        somaDasNotas += somarNotasAlunos (aluno)
    return somaDasNotas/numeroDeNotas


aluno = {'nome': 'ok', 'registro': 10, 'notas': [0, 10, 5]}
alunoA = {'nome': 'ok', 'registro': 10, 'notas': [10, 10, 5]}
alunoB = {'nome': 'ok', 'registro': 10, 'notas': [0, 10, 5]}
