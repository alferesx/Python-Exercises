
quantidade_produtos = int(input('Quantos produtos voce deseja comprar ? : '))

preco_total = 0

print('Lojas Tabajara')

for q in range(1 , quantidade_produtos + 1):

    nome_produto = input('Produto:')

    preco_produto = int(input('Preco: '))

    print(nome_produto,'-', preco_produto)

    preco_total += preco_produto


