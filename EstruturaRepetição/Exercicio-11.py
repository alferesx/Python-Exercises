
numero1 = int(input('Numero1: '))

numero2 = int(input('Numero2: '))

soma = 0

for n in range(numero1,numero2):
    print(n)
    soma = soma + n

print('Total: ',soma)