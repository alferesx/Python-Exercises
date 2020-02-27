
quantidade_habitantes_planeta_a =int(input('Quantidade de habitantes: '))

quantidade_habitantes_planeta_b =int(input('Quantidade de habitantes: '))

taxa_crescimento_populacao_a = float(input('Porcentagem de crescimento: '))

taxa_crescimento_populacao_b = float(input('Porcentagem de crescimento: '))

anos = 0

if quantidade_habitantes_planeta_b > quantidade_habitantes_planeta_a:

    crescimento_habitantes_a = quantidade_habitantes_planeta_a * (taxa_crescimento_populacao_a / 100)

    while quantidade_habitantes_planeta_a <= quantidade_habitantes_planeta_b:

       quantidade_habitantes_planeta_a = quantidade_habitantes_planeta_a + crescimento_habitantes_a
       anos = anos + 1
       print(anos)

    print('Planeta A vai ser maior que o Planeta B em ',anos,' anos')

elif quantidade_habitantes_planeta_a > quantidade_habitantes_planeta_b:

    crescimento_habitantes_b = quantidade_habitantes_planeta_b * (taxa_crescimento_populacao_b / 100)

    while quantidade_habitantes_planeta_b <= quantidade_habitantes_planeta_a:
        quantidade_habitantes_planeta_b = quantidade_habitantes_planeta_b + crescimento_habitantes_b
        anos = anos + 1
        print(anos)

    print('Planeta B vai ser maior que o Planeta A em ', anos, ' anos')