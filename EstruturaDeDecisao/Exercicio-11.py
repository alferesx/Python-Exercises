nome_funcionario = input('Digite seu nome: ')
salario_funcionario = float(input('Por favor informe seu salario: '))

if salario_funcionario <= 280:
    print('Salario do ', nome_funcionario, 'antes do aumento: ', salario_funcionario)
    percentual = 20
    reajuste = (salario_funcionario * percentual) / 100
    salario_funcionario = salario_funcionario + reajuste
    print('Percentual aumentado: ',percentual)
    print(nome_funcionario,'Recebeu um reajuste de: R$',reajuste)
    print(nome_funcionario,'Seu novo salario é: R$',salario_funcionario)

elif salario_funcionario >= 280 and salario_funcionario <= 700:
    print('Salario do ', nome_funcionario, 'antes do aumento: ', salario_funcionario)
    percentual = 15
    reajuste = (salario_funcionario * 15) / 100
    salario_funcionario = salario_funcionario + reajuste
    print('Percentual aumentado: ', percentual)
    print(nome_funcionario, 'Recebeu um reajuste de: R$', reajuste)
    print(nome_funcionario, 'Seu novo salario é: R$', salario_funcionario)

elif salario_funcionario > 700 and salario_funcionario <= 1500:
    print('Salario do ', nome_funcionario, 'antes do aumento: ', salario_funcionario)
    percentual = 10
    reajuste = (salario_funcionario * percentual) / 100
    salario_funcionario = salario_funcionario + reajuste
    print('Percentual aumentado: ', percentual)
    print(nome_funcionario, 'Recebeu um reajuste de: R$', reajuste)
    print(nome_funcionario, 'Seu novo salario é: R$', salario_funcionario)

elif salario_funcionario > 1500:
    print('Salario do ', nome_funcionario, 'antes do aumento: ', salario_funcionario)
    percentual = 5
    reajuste = (salario_funcionario * 5) / 100
    salario_funcionario = salario_funcionario + reajuste
    print('Percentual aumentado: ', percentual)
    print(nome_funcionario, 'Recebeu um reajuste de: R$', reajuste)
    print(nome_funcionario, 'Seu novo salario é: R$', salario_funcionario)
