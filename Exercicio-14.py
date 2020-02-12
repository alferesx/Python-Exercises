peso = float(input('Digite a quantidade que o joao esta levando: '))
peso_maximo = 50
valor_excedente = 4.0

if peso > peso_maximo:
    multa = (peso - peso_maximo) * valor_excedente
    print('Valor da multa por carregar alem ',peso_maximo,'kilos é: ',multa,' dolares')
else:
    print('Sem necessidade de multa')



