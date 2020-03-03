print('Validador de numero primo')

numero = int(input('Digite um numero: '))

total_divisores = []

contador_divisores = 0

for n in range(1,numero + 1):
    if numero % n == 0:
        contador_divisores += 1
        total_divisores.append(n)

if contador_divisores == 2:
    print('O numero: ',numero,'é primo e os seus divisores sao',total_divisores)

else:
    print('O numero: ',numero,'não é primo e seus divisores sao',total_divisores)

