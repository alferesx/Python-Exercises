quantidade = int(input('Digite a quantidade de numeros que vao estar dentro do conjunto'))

conjuntos = []

maior = 0

menor = 0

soma = 0

q = 0

while q <= quantidade :

    numero = int(input('Numero: '))

    if numero >= 0 and numero <= 1000:
        conjuntos.append(numero)

    else:
        print('numero invalido')

    soma = soma + numero

    if q == 1:
        maior = conjuntos[0]

        menor = conjuntos[0]


    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

    q = q + 1

print('Conjuntos: ',conjuntos)

print('Maior: ',maior)

print('Menor: ',menor)

print('Soma: ',soma)