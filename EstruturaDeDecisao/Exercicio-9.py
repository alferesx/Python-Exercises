valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite um valor: '))
valor3 = int(input('Digite um valor: '))

if valor1 > valor2 and valor1 > valor3 and valor2 < valor1 and valor2 > valor3:
    print(valor1)
    print(valor2)
    print(valor3)
elif valor2 >valor1 and valor2 > valor3 and valor1 < valor2  and valor3 > valor1:
    print(valor2)
    print(valor3)
    print(valor1)


elif valor3 > valor1 and valor3 > valor2 and valor1 < valor2 and valor2 > valor1:
    print(valor3)
    print(valor2)
    print(valor1)
