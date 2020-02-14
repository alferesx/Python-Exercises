dia = int(input('Digite um numero de 1 a 7: '))

dias_semana = {
    1:'Segunda-Feira',
    2:'Terca-Feira',
    3:'Quarta-Feira',
    4:'Quinta-Feira',
    5:'Sexta-Feira',
    6:'Sabado',
    7:'Domingo',
}

if dia in dias_semana:
    print(dias_semana[dia])
