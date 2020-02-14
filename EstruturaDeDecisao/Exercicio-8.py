produto1 = float(input("Digite o valor do primeiro produto:"))
produto2 = float(input("Digite o valor do segundo produto:"))
produto3 = float(input("Digite o valor do terceiro produto:"))

if produto1 < produto2 and produto1 < produto3:
    print("O produto mais barato é o produto 1 no valor : ",produto1)

elif produto2 < produto1 and produto2 < produto3:
    print("O produto mais barato é o produto 2 no valor: ",produto2)

elif produto3 < produto1 and produto3 < produto1:
    print("O produto mais barato é o produto 3 no valor: ",produto3)
