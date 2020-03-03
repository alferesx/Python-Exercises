print('Validador de primo')

numero = int(input('Digite um numero'))

total = 0

for n in range(1,numero + 1 ):
    print(n)
    if numero % n == 0:
        total += 1

print('Total de divisores: ',total)
if total == 2:
    print('O numero: ',numero,'é primo')
else:
    print('O numero: ',numero,'não é primo')