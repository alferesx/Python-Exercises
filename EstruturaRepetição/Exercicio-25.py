quantidade_alunos = int(input('Digite a quantidade de alunos: '))

jovems = []

media_jovems = 0

adultos = []

media_adultos = 0

idosos = []

media_idosos = 0

for n in range(1,quantidade_alunos + 1):

    idade = int(input('Digite a idade do aluno(a): '))

    print('Aluno(a)',n,'idade: ',idade)

    if idade <= 26:

        print('Aluno(a)',n,': jovem')
        jovems.append(idade)
        media_jovems += idade

    elif idade > 26 and idade <= 60:

        print('Aluno(a)', n, ': Adulto')
        adultos.append(idade)
        media_adultos += idade

    elif idade > 60:

        print('Aluno(a)', n, ': Idoso')
        idosos.append(idade)
        media_idosos +=idade

print(jovems)

print('media dos jovems:',media_jovems)

print(adultos)

print('media dos adultos: ',media_adultos)

print(idosos)

print('media dos idosos: ',media_idosos)

media_turma = (media_jovems + media_adultos + media_idosos) / quantidade_alunos

print(media_turma)

if media_turma  <= 26:
    print('A  media da turma é jovem.')
elif media_turma > 26 and media_turma <= 60:
    print('A media da turma é adulta')
elif media_turma > 60:
    print('A media da turma é idosa')

