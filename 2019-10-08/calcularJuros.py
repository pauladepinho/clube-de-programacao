# Calcula juros simples. (juros = capital * taxa * tempo)

capitalInicial = float (input ('Capital inicial: '))
i = float (input ('Taxa: '))
tempo = float (input ('Tempo: '))

j = capitalInicial * i * tempo

print ('Juros: ', j)