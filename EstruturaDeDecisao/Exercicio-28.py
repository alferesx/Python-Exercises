
print('#################################### M E N U ####################################')

print('File Duplo')

print('Alcatra')

print('Picanha')

print('#################################################################################')

file_duplo_ate_5kg = 4.90

file_duplo_acima_5kg = 5.80

alcatra_ate_5kg = 5.90

alcatra_acima_5kg = 6.80

picanha_ate_5kg = 6.90

picanha_acima_5kg = 7.80

tipo_carne = input('Qual tipo de carne o senhor deseja: ')

if tipo_carne == 'file' or tipo_carne == 'File Duplo' or tipo_carne == 'file duplo' or tipo_carne == 'duplo':

    quantidade = int(input('Quantos kg voce deseja: '))

    if quantidade > 5:

        preco_file_duplo = quantidade * file_duplo_acima_5kg

        print(tipo_carne,quantidade,'Valor: ',preco_file_duplo)

    else:

        preco_file_duplo = quantidade * file_duplo_ate_5kg

        print(tipo_carne, quantidade, 'Valor: ', preco_file_duplo)

    forma_pagamento = input('Qual a forma de pagamento: ')

    if forma_pagamento =='cartao' or forma_pagamento == 'Cartao':

        desconto = preco_file_duplo * ( 5 / 100)

        print('Voce ganhou um desconto de 5% por usar cartao o valor descontado foi de: ',desconto)

        preco_file_duplo = preco_file_duplo - desconto

        print('O valor total com desconto é: ',preco_file_duplo)

    else:

        print('Voce não teve direito ao desconto')

        print('Valor total: ',preco_file_duplo)


if tipo_carne == 'alcatra' or tipo_carne == 'Alcatra':

    quantidade = int(input('Quantos kg voce deseja: '))

    if quantidade > 5:

        preco_alcatra = quantidade * alcatra_acima_5kg

        print(tipo_carne,quantidade,'Valor: ',preco_alcatra)

    else:

        preco_alcatra = quantidade * alcatra_ate_5kg

        print(tipo_carne, quantidade, 'Valor: ', preco_alcatra)

    forma_pagamento = input('Qual a forma de pagamento: ')

    if forma_pagamento == 'cartao' or forma_pagamento == 'Cartao':

        desconto = preco_alcatra * ( 5 / 100)

        print('Voce ganhou um desconto de 5% por usar cartao o valor descontado foi de: ',desconto)

        preco_alcatra = preco_alcatra - desconto

        print('O valor total com desconto é: ',preco_alcatra)

    else :

        print('Voce não teve direito ao desconto')

        print('Valor total: ',preco_alcatra)


if tipo_carne == 'Picanha' or  tipo_carne == 'picanha':

    quantidade = int(input('Quantos kg voce deseja: '))

    if quantidade > 5:

        preco_picanha = quantidade * picanha_acima_5kg

        print(tipo_carne,quantidade,'Valor: ',preco_picanha)

    elif quantidade < 5:

        preco_picanha = quantidade * picanha_ate_5kg

        print(tipo_carne, quantidade, 'Valor: ', preco_picanha)

    forma_pagamento = input('Qual a forma de pagamento: ')

    if forma_pagamento == 'Cartao' or forma_pagamento == 'cartao':

        desconto = preco_picanha * ( 5 / 100)

        print('Voce ganhou um desconto de 5% por usar cartao o valor descontado foi de: ',desconto)

        preco = preco_picanha - desconto

        print('O valor total com desconto é: ',preco)

    elif forma_pagamento == 'Dinheiro' or forma_pagamento == 'dinheiro':

        print('Voce não teve direito ao desconto')

        print('Valor total: ',preco_picanha)

