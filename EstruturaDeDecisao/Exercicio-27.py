
preco_ate_5kg_morango =2.50

preco_acima_5kg_morango =2.20

preco_ate_5kg_maca =1.80

preco_acima_5kg_maca =1.50

quantidade_morangos = float(input('Quantos kilos voce vai levar de morango: '))

quantidade_maca =  float(input('Quantos kilos voce vai levar de maca: '))

if quantidade_morangos > 5:

    preco_total_morango = quantidade_morangos * preco_acima_5kg_morango

    print('Preco Morango: ',preco_total_morango)

else:

    preco_total_morango = quantidade_morangos * preco_ate_5kg_morango

    print('Preco Morango: ',preco_total_morango)

if quantidade_maca > 5:

    preco_total_maca = quantidade_maca * preco_acima_5kg_maca

    print('Preco da maca: ',preco_total_maca)

else:

    preco_total_maca = quantidade_morangos * preco_ate_5kg_maca

    print('Preco da maca: ',preco_total_maca)

if quantidade_morangos > 8 or preco_total_morango > 25:

    desconto_morango = quantidade_morangos * (10 / 100)

    print('Voce teve um desconto de:',desconto_morango)

    preco_total_morango = preco_total_morango - desconto_morango

    print('Valor a ser pago no total no Morango: ',preco_total_morango)

else:

    print('Voce nao teve desconto')

    print('Valor a ser pago no total no Morango',preco_total_morango)

if quantidade_maca > 8 or preco_total_maca > 25:

    desconto_maca = quantidade_maca * (10 / 100)

    print('Voce teve um desconto de:',desconto_maca)

    preco_total_maca = preco_total_maca - desconto_maca

    print('Valor a ser pago no total na Maça: ',preco_total_maca)

else:

    print('Voce nao teve desconto')

    print('Valor a ser pago no total na Maça',preco_total_maca)