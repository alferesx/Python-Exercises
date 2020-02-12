altura = float(input('Digite sua altura: '))
genero = input('Digite seu genero: ')

if genero == 'Masculino' or genero == 'masculino' or genero == 'm':
    peso = (72.7 * altura) - 58
    print('peso ideal para voce é: ',peso)

elif (genero == 'Feminino') or (genero == 'feminino') or (genero == 'f'):
    peso = (62.1*altura)-44.7
    print('O peso ideal para voce é: ',peso)
else:
    print("Informe o genero masculino ou feminino")
