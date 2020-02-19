nota1 = float(input("nota1:"))
nota2 = float(input("nota2:"))
nota3 = float(input("nota3:"))

media = (nota1 + nota2 + nota3) / 3

if media == 10:
    print("Aprovado com distinção")

elif media >= 7:
    print("Aprovado com a media:",media)

elif media < 7:
    print("Reprovado com a media:",media)
