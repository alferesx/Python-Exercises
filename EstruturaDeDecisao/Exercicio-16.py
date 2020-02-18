import math
import fractions

a = int(input('Digite o valor do a: '))

if a == 0:
    print('Não é uma equação do segundo grau')
else:
    b = int(input('Digite o valor do b: '))

    c = int(input('Digite o valor do c: '))

    delta = (b**2) - (4*a*c)
    print('Delta: ',delta)
    if delta < 0:
        print('A equação não possui raizes reais.')
    elif delta == 0:
        print('A equação possui apenas uma raiz real')
        x = (-b + math.sqrt(delta)) / (2 * a)
        print('O valor de x1 é igual: ',fractions.Fraction(x))
    elif delta > 0:
        print('A equação possui duas raizes reais')
        x = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print('x1: ',x)
        print('x2: ',x2)


