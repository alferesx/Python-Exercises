
pergunta1 = input('Telefonou para a vitima ?: ')

pergunta2 = input('Esteve no local do crime ?: ')



pergunta3 = input('Mora perto da vitima ?: ')

pergunta4 = input('Devia para a vitima ?: ')

pergunta5 = input('ja trabalhou com a vitima ?: ')

total = 0


if pergunta1 == 'sim':
    total = total + 1

if pergunta2 == 'sim':
    total = total + 1

if pergunta3 == 'sim':
    total = total + 1

if pergunta4 == 'sim':
    total = total + 1

if pergunta5 == 'sim':
    total = total + 1

print(total)

if total == 5:
    print("Assasino")

elif total == 4 or total == 3:
    print('Cumplice')

elif total == 2:
    print('Suspeito')
else:
    print('inocente')