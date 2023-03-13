import json

with open('desafio3/dados.json') as file:
    valores = json.load(file)

faturamento_diario = []
dias_uteis = 0
for d in valores:
    faturamento_diario.append(d['valor'])
    if d['valor'] >0:
        dias_uteis += 1

valor_menor = min(faturamento_diario)
valor_maior = max(faturamento_diario)
media_mes = sum(faturamento_diario)/dias_uteis

superior_media = 0

for valor in faturamento_diario:
    if valor > media_mes:
        superior_media +=1
        
print("Menor valor do faturamento diario é de: ",+ valor_menor)
print("Maior valor do faturamento duario é de: ", +valor_maior)
print("O numero de dias no mes que o valor de faturamento diario foi superior a media mensal é de: ",+ superior_media )
