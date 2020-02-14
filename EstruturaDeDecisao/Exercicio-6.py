numero1 = int(input('Digite o primeiro valor: '))
numero2 = int(input('Digite o segundo valor: '))
numero3 = int(input('Digite o terceiro valor: '))

if numero1 > numero2 and numero1 > numero3:
    print('O  maior valor é: ',numero1)
elif numero2 > numero1 and numero2 > numero3:
    print('O maior valor é: ',numero2)
elif numero3 > numero1 and numero3 > numero1:
    print('O maior valor é :',numero3)
