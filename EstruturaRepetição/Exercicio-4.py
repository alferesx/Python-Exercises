habitantes_a = 80000
habitantes_b = 200000
crescimento_populacao_a = habitantes_a * (3 / 100)
ano = 0
print(crescimento_populacao_a)

crescimento_populacao_b =  habitantes_b * (1.5 / 100)
print(crescimento_populacao_b)

while(habitantes_a <= habitantes_b):
    habitantes_a = habitantes_a + crescimento_populacao_a
    ano = ano + 1
    print(ano)

print('Vai levar ',ano,'para o A ser maior que o planeta b')