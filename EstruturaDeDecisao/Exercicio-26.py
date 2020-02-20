litros = float(input('Quantos litros voce deseja colocar: '))

if litros <= 20:

    desconto_alcool = litros *( 3 / 100)
    print('Desconto Alcool: ',desconto_alcool)

    preco_alcool = (1.90 * 20) - desconto_alcool
    print('Preço do alcool: ',preco_alcool)

    desconto_gasolina = litros * (4 / 100)
    print('Desconto da gasolina: ',desconto_gasolina)

    preco_gasolina = (litros * 2.50) - desconto_gasolina
    print('Desconto da gasolina',preco_gasolina)

elif litros <= 20:

    desconto_alcool = litros * (5 / 100)
    print('Desconto alcool: ',desconto_alcool)

    preco_alcool = (1.90 * 20) - desconto_alcool
    print('Preço do Alcool: ',preco_alcool)

    desconto_gasolina = litros * (6 / 100)
    print('Valor do desconto:',desconto_gasolina)

    preco_gasolina = (litros * 2.50) - desconto_gasolina
    print('Preço da gasolina: ',preco_gasolina)
