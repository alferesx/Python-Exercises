
quantidade_numeros = int(input('Digite a quantidade de valores dentro do conjunto: '))

conjunto = []

soma = 0

maior = 1

menor = 1

for quantidade in range(quantidade_numeros):

    numero = int(input('Numero: '))

    conjunto.append(numero)

    if quantidade == 1:

        maior = conjunto[0]

        menor = conjunto[0]

    soma = soma + numero

    if numero > maior:

        maior = numero

    if numero < menor:

        menor = numero


print('Conjunto: ',conjunto)

print('Soma: ',soma)

print('Maior: ',maior)

print('Menor: ',menor)

'''
for quantidade in range(quantidade_numeros):

    numero = int(input('Numero: '))

    conjunto.append(numero)

    soma = soma + numero

print('Conjunto de numeros: ',conjunto)

print('Maior: ', max(conjunto))

print('Menor: ',min(conjunto))

print('Soma: ',soma)

'''