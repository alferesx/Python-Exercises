print('Calcular temperatura minima e maxima')

quantidade_temperaturas  =int(input('Quantas temperaturas voce deseja medir: '))

temperaturas = []

media_temperaturas  = 0

soma_temperaturas = 0

maior_temperatura = 1

menor_temperatura = 1

for q in range(1,quantidade_temperaturas + 1):

    temperatura = int(input('Temperatura:'))

    print('Temperatura: -', q, ':',temperatura)

    temperaturas.append(temperatura)

    if q == 1:
        maior_temperatura = temperaturas[0]
        menor_temperatura = temperaturas[0]

    if temperatura > maior_temperatura :
        maior_temperatura = temperatura

    if temperatura < menor_temperatura:
        menor_temperatura = temperatura

    soma_temperaturas = soma_temperaturas + temperatura

print(temperaturas)

print('Soma de todas as temperaturas: ',soma_temperaturas)

media_temperaturas = soma_temperaturas / quantidade_temperaturas

print('Media:',media_temperaturas)

print('Maior temperatura: ',maior_temperatura)

print('Menor temperatura: ',menor_temperatura)
