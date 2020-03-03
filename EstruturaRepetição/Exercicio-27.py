
numero_turmas = int(input('Digite o numero de turmas: '))

turma_alunos = [[],[]]

medias_turmas = [[],[]]

for t in range(1,numero_turmas + 1):

    quantidade_alunos = int(input('Quantidade de alunos na turma: '))

    turma_alunos.append(t)

    turma_alunos.append(quantidade_alunos)

    media = quantidade_alunos / numero_turmas

    turma_alunos.append(media)

print(list(turma_alunos))
