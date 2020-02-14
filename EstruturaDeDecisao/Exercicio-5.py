nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1 + nota2) / 2

if media == 10:
    print('Aprovado com distinção')

elif media >= 7:
    print('Voce foi aprovado com a nota: ', media)

elif media < 7:
    print('Voce foi reprovado com a nota: ', media)

