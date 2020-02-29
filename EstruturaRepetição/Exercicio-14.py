numeros = []

quantidade = 10

numeros_pares = 0

numeros_impares = 0

for n in range(quantidade):
    numero = int(input('Numero: '))
    if numero % 2 == 0:
        numeros.append(numero)
        numeros_pares  = numeros_pares + 1
    elif numero % 2 != 0:
        numeros.append(numero)
        numeros_impares = numeros_pares + 1

print(numeros)

print('Numeros pares: ',numeros_pares)

print('Numeros impares: ',numeros_impares)
