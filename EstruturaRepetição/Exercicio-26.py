quantidade_eleitores = int(input('Digite a quantidade de eleitores: '))

eleitor_A = 0

eleitor_B = 0

eleitor_C = 0

print('Digite o seu voto.')

for e in range(1,quantidade_eleitores + 1):

    voto = input('Voto: ')
    print('Eleitor', e ,'Voto: ',voto)

    if voto == 'A' or voto == 'a':
        eleitor_A += 1

    elif voto == 'B' or voto == 'b':
        eleitor_B +=1

    elif voto == 'C' or voto == 'c':
        eleitor_C += 1

print('Total de votos')

print('Eleitor A: ',eleitor_A)

print('Eleitor B: ',eleitor_B)

print('Eleitor C: ',eleitor_C)