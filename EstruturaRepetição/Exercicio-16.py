posicao = 15

ultimo = 1

penultimo = 1

termo  = 0

for n in range(2,posicao):
    if termo <= 500:
        termo = ultimo + penultimo

        ultimo = termo

        penultimo = ultimo
else:
    print(termo)