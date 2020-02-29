fatorial = -1

while fatorial != 16:

    fatorial = int(input('Digite o valor da fatorial: '))

    if fatorial == 16:
        break

    total = 1

    while fatorial != 1:

        total  = total * fatorial

        fatorial = fatorial - 1

    print( 'Fatorial: ',total)



