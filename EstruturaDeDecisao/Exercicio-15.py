a = int(input('Digite o valor do primeiro lado do triangulo: '))
b = int(input('Digite o valor do segundo lado do triangulo: '))
c = int(input('Digite o valor do terceiro lado do triangulo: '))

if a == b and a == c:
    print('É um triangulo equilatero')
elif a == b or a == c  or b == a or b == c or c == a or c == b:
    print('É um triangulo isósceles')
elif a != b and a != c and b != a and b != c and c != a and c != b:
    print('É um triangulo escaleno')
