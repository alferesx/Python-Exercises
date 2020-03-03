valor_hora = float(input('Informe o valor que voce ganha por hora: '))
horas_trabalhadas_mes = int(input('Quantas horas no mes voce trabalhou: '))
salario_bruto = valor_hora  * horas_trabalhadas_mes
print('Seu salario bruto é: R$',salario_bruto,)

print("Valor pago ao INSS")
ir = salario_bruto * (11 / 100)

print('Valor INSS:',ir)

print("Valor pago ao INSS")
inss = salario_bruto * (8 / 100)

print('Valor INSS:',inss)

print('Valor pago ao Sindicato')
sindicato = salario_bruto * (5 / 100)
print('Valor Sindicato: ',sindicato)

print('Salario liquido')
salario_liquido = salario_bruto - ir - inss - sindicato
print("Seu salario liquido: ",salario_liquido)


