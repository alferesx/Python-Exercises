
numero = input("Digite um numero: ")

tamanho = len(numero)

array_numeros = list(numero)

if tamanho == 3:

    centena = int(array_numeros[0])

    dezena = int(array_numeros[1])

    unidade = int(array_numeros[2])

    if centena > 1 and dezena > 1 and unidade > 1:
        print(centena,'centenas',dezena,'dezenas',unidade,'unidades')

    elif centena > 1 and dezena > 1 and unidade <= 1:
        print(centena, 'centenas', dezena, 'dezenas', unidade, 'unidade')

    elif centena > 1 and dezena <= 1 and unidade <= 1:
        print(centena, 'centenas', dezena, 'dezena', unidade, 'unidade')

    elif centena <= 1 and dezena > 1 and unidade > 1:
        print(centena, 'centena', dezena, 'dezenas', unidade, 'unidades')

    elif centena <= 1 and dezena > 1 and unidade <= 1:
        print(centena, 'centena', dezena, 'dezenas', unidade, 'unidade')

    elif centena <= 1 and dezena <= 1 and unidade > 1:
        print(centena, 'centena', dezena, 'dezena', unidade, 'unidades')

    else:
        print(centena, 'centena', dezena, 'dezena', unidade, 'unidade')


elif tamanho == 2:
    dezena = int(array_numeros[0])

    unidade = int(array_numeros[1])

    if dezena > 1 and unidade > 1:
        print(dezena,'dezenas',unidade,'unidades')

    elif   dezena > 1 and unidade <= 1:
        print( dezena, 'dezenas', unidade, 'unidade')

    elif   dezena <= 1 and unidade <= 1:
        print( dezena, 'dezena', unidade, 'unidade')

    elif   dezena > 1 and unidade > 1:
        print( dezena, 'dezenas', unidade, 'unidades')

    elif  dezena > 1 and unidade <= 1:
        print( dezena, 'dezenas', unidade, 'unidade')

    elif  dezena <= 1 and unidade > 1:
        print( dezena, 'dezena', unidade, 'unidades')

    else:
        print( dezena, 'dezena', unidade, 'unidade')


elif tamanho == 1:

    unidade = int(array_numeros[0])
    if unidade <= 1:
        print(unidade, 'unidade')
    else:
        print(unidade, 'unidades')







