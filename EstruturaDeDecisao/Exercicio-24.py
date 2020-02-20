
numero1 = float(input('Valor1: '))

numero2 = float(input('Valor2: '))

print('M E N U')

print('a.par ou impar')

print('b.positivo ou negativo')

print('c.inteiro ou decimal')


opcao = input('O que voce deseja fazer ?')


if opcao == 'a':

    if numero1 % 2 == 0 and numero2 % 2 == 0:
        print('Ambos os numeros são pares')

    elif numero1 % 2 == 0 and numero2 % 2 !=0:
        print('Valor 1 é par e valor 2 é impar')

    elif numero1 % 2 != 0 and numero2 % 2 == 0:
        print('Valor 1 é impar e valor2 é par')
    else:
        print('Ambos os dois valores são impares')

elif opcao == 'b':
    if numero1 > 0 and numero2 > 0:
        print('Ambos os numeros são positivos')

    elif numero1 > 0 and numero2 < 0:
        print('Valor 1 é positivo e valor 2 é negativo')

    elif numero1  < 0 and numero2 > 0:
        print('Valor 1 é negativo e valor2 é positivo')
    else:
        print('Ambos os dois valores são negativos')

elif opcao == 'c':
    if numero1 == round(numero1) and numero2 == round(numero2):
        print('Ambos os numeros sao inteiros')

    elif numero1 == round(numero1) and numero2 != round(numero2):
        print('Valor 1 é inteiro e valor 2 é decimal')

    elif numero1 != round(numero1) and numero2 == round(numero2):
        print('Valor 1 é decimal e valor 2 é inteiro')
    else:
        print('Ambos os valores são decimais')