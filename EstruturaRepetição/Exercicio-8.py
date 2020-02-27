quantidade = 5

numeros = []

soma = 0

for n in range(quantidade):

    nota = float(input('nota: '))

    numeros.append(nota)

    soma = soma + nota

print('Notas: ',numeros)

print('Soma das notas: ',soma)

media = soma / 5

print('Media: ',media)