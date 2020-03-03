
quantidade_cd  = int(input('Digite a quantidade de cds que voce deseja comprar: '))

cds = [[],[]]

media_cds = 0

valor_total_cds = 0

for n in range(1,quantidade_cd + 1):

    nome_cd = input('Digite o nome do cd: ')

    preco_cd = float(input('Digite o preço do cd: '))

    cds.append(nome_cd)

    cds.append(preco_cd)

    valor_total_cds += preco_cd

    media_cds = preco_cd / quantidade_cd

    cds.append(media_cds)

print(cds)
print('Valor total: ',valor_total_cds)