
numero = int(input('Digite um numero: '))

total = 0

total_divisoes = 0

divisores = []

for n in range(1 , numero + 1):

    if numero % n == 0:

        total  += 1

        total_divisoes = total

        divisores.append(n)

if total == 2:

    print('Foi feito: ',total_divisoes,'divisoes')

    print('O numero: ',numero,'é primo seus divisores são: ',divisores)

else:

    print('Foi feito: ',total_divisoes,'divisoes')

    print('O numero: ',numero,'nao é primo e seus divisores sao: ',divisores)
