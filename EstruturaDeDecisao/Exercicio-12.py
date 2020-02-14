valor_hora = float(input('Digite seu valor por hora: '))
horas_trabalhadas_mes = int(input('Digite as horas trabalhadas no mes: '))

salario_bruto = valor_hora * horas_trabalhadas_mes
print('Seu salario bruto: ',salario_bruto)

if salario_bruto <= 900:
    print('Seu salario nao teve nenhum imposto descontado')
    print('O valor do seu salario: ',salario_bruto)

elif salario_bruto <= 1500:
    print('Seu salario teve um desconto de 5%')
    desconto = (salario_bruto * 5 )/100
    print('O valor descontado do salario foi de: ',desconto)
    salario_liquido = salario_bruto - desconto
    print('O seu salario liquido é: ',salario_liquido)

elif salario_bruto > 1500 and salario_bruto <= 2500:
    print('Seu salario teve um desconto de 10%')
    desconto = (salario_bruto * 10 )/100
    print('O valor descontado do salario foi de: ',desconto)
    salario_liquido = salario_bruto - desconto
    print('O seu salario liquido é: ',salario_liquido)

elif salario_bruto > 1500 and salario_bruto <= 2500:
    print('Seu salario teve um desconto de 20%')
    desconto = (salario_bruto * 20 )/100
    print('O valor descontado do salario foi de: ',desconto)
    salario_liquido = salario_bruto - desconto
    print('O seu salario liquido é: ',salario_liquido)


