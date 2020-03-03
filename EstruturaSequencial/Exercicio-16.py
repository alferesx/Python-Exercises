tamanho = int(input('Quantos metros voce vai pintar: '))
litros = tamanho / 3
print("Litros: ",litros)
lata = 18
total_latas_tinta = litros / lata
print("Numero de latas de tintas: ",total_latas_tinta,' latas')
valor = 80
print('Valor total: ',valor * total_latas_tinta,'Reais')
