produto = input('Voce deseja latas de 18 litros , 3.6 litros ou ambos ?: ')

if produto == 'lata':

    tamanho = int(input('Digite a quantidade de metros: '))
    litros =  tamanho / 6
    print('Total de litros: ',litros)
    quantidade_latas_tinta = litros / 18
    total = quantidade_latas_tinta * 80
    print("O valor total das latas: R$",total)

elif produto == 'galao':
    tamanho = float(input('Digite a quantidade de metros: '))
    litros = tamanho / 6
    print('Total de litros: ', litros)
    quantidade_galoes_tinta = litros / 3.6
    total = quantidade_galoes_tinta * 25
    print("O valor total dos galoes: R$", total,)

elif produto == 'ambos' :
    tamanho = int(input('Digite a quantidade de metros: '))
    litros_lata = tamanho / 6
    litros_galao = tamanho / 6

    print('Total de litros por lata: ', litros_lata)
    print('Total de litros por galao: ', litros_galao)

    quantidade_latas_tinta = litros_lata / 18
    quantidade_galoes_tinta = litros_galao / 3.6
    total_latas = quantidade_latas_tinta * 80
    print("Valor de todas as latas:",total_latas)
    total_galoes = quantidade_galoes_tinta * 25
    print('Valor de todos os galoes:',total_galoes)
    desconto = (((total_latas + total_galoes) * 10) / 100)
    print("Voce teve um desconto de: ", desconto)
    total = total_latas + total_galoes - desconto
    print('Total da compra: ',total)

