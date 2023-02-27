import json

with open('dados.json') as file:
    dados = json.load(file)

menor_faturamento = float('inf')
maior_faturamento = 0
soma_faturamento = 0
num_dias_acima_media = 0


for dia in dados:
    valor = dia['valor']
    soma_faturamento += valor
    if valor < menor_faturamento:
        menor_faturamento = valor
    if valor > maior_faturamento:
        maior_faturamento = valor

media_faturamento = soma_faturamento / len(dados)

for dia in dados:
    if dia['valor'] > media_faturamento:
        num_dias_acima_media += 1


print(f"Menor faturamento: R${menor_faturamento:.2f}")
print(f"Maior faturamento: R${maior_faturamento:.2f}")
print(f"Dias acima da média: {num_dias_acima_media}")
