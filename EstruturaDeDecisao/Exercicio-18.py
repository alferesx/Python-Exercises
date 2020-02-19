dia = int(input('Digite o dia: '))
if dia > 31:
    print('Dia invalido')
else:

    mes = int(input('Digite o mes: '))
    meses_30_dias = [4,6,9,11]
    meses_31_dias = [1,3,5,7,8,10,12]
    if dia > 29 and mes == 2:
        print('O mes de fevereiro só tem 29 dias')

    else:
        ano=int(input('Digite o ano: '))

        if dia > 0 and dia < 31  and mes in meses_30_dias:
            print('Esse mes tem 30 dias')
            print(dia,'/',mes,'/',ano)

        else:
         print('Esse mes tem 31 dias')
        if dia > 0  and  dia <= 31  and mes in meses_31_dias:
            print(dia,'/',mes,'/',ano)


