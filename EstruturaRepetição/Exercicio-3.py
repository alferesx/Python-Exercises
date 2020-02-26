generos = ['f','m']
estados_civis = ['s','d','v','c']
nome = input('Nome: ')

while(len(nome) < 3):
    print('Digite seu nome completo')
    nome = input('Nome: ')

idade = int(input('Idade: '))

while(idade > 150):
    print('A idade tem que ser entre 0 a 150 anos')
    idade = int(input('Idade: '))

salario = float(input('Salario: '))

while(salario < 0):
    print('Digite o valor do seu salario')
    salario = float(input('Salario:'))

sexo = input('Sexo: ')
while(sexo not in generos):
    print('Digite se seu sexo é f-feminino ou m-masculino')
    sexo = input('Sexo: ')

estado_Civil = input('Estado Civil: ')
while(estado_Civil not in estados_civis):
    print('Digite um estado s-solteiro c-casado v-viuva e d-divorciado')
    estado_Civil = input('Estado Civil: ')
print('Informações do usuario')

print(nome)
print(idade)
print(salario)
print(sexo)
print(estado_Civil)