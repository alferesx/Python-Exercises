nome = input('Digite o seu nome: ')

print(nome,'Vamos calcular agora suas duas notas')

nota1 = float(input('Digite sua primeira nota: '))

nota2 = float(input('Digite sua segunda nota: '))

media = (nota1 + nota2) / 2

print('Nota1: ',nota1)

print('Nota2: ',nota2)

print('Media:',media)

if media >= 9:
    conceito = 'A'
    print(conceito,'APROVADO')
elif media >= 7.5 and media <= 9:
    conceito = 'B'
    print(conceito,'APROVADO')
elif media >= 6.0 and media <= 7.5:
    conceito = 'C'
    print(conceito,'APROVADO')
elif media >= 4 and media <= 6:
    conceito = 'D'
    print(conceito,'REPROVADO')
elif media >= 0 and media <= 4:
    conceito = 'E'
    print(conceito,'REPROVADO')
