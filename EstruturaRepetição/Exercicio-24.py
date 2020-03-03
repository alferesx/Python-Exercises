
numero_notas = int(input('Digite a quantidade de notas: '))

notas = []

soma_notas = 0

media  = 0

for n in range(1,numero_notas + 1):

    nota = int(input('Nota: '))

    print('Nota',n,':',nota)

    notas.append(nota)

    soma_notas = ( soma_notas + nota )

media = soma_notas / numero_notas

print('Sua media foi: ',media)
