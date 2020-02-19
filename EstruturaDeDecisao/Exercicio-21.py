valor = int(input("Digite o valor que voce deseja sacar com valor minimo 10 e maximo 600: "))

notas_disponiveis = [100,50,10,5,1]

for n in notas_disponiveis:

        notas_100 = valor / notas_disponiveis[0]

        if valor % notas_disponiveis[0] == 0:
            print(notas_100,'notas de 100 reais')
            break

        else:
            print(notas_100,'notas de 100 reais')

            resto = valor % notas_disponiveis[0]
            notas_50 = resto / notas_disponiveis[1]
            print(resto)
        if valor % notas_disponiveis[1] == 0:
            print(notas_50, 'notas de 50 reais')
            break

        else:
            print(notas_50,'notas de 50 reais')
            resto = valor % notas_disponiveis[1]
            notas_10 = resto / notas_disponiveis[2]
            print(resto)

        if valor % notas_disponiveis[2] == 0:
            print(notas_10,'notas de 10 reais')
            break

        else:
            print(notas_10, 'notas de 10 reais')
            resto = valor % notas_disponiveis[2]
            notas_5 = resto / notas_disponiveis[3]
            print(resto)
        if valor % notas_disponiveis[3] == 0:
            print(notas_5,'notas de 5 reais')
        else:
            print(notas_5,'notas de 5 reais')
            resto = valor % notas_disponiveis[3]
            notas_1 = resto / notas_disponiveis[4]
            print(resto)
        if valor % notas_disponiveis[4] == 0:
            print(notas_1,'notas de 1 real')
            break





