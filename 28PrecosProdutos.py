#Algotimo ESTDEC_LT01_28
#Declarar.
media_mensal: int = 0
preco_atual: float = 0.0
preco_novo: float = 0.0

#Início.
media_mensal = float(input("Digite a media de vendas por mes: "))
preco_atual = float(input("Digite o preco do produto: "))

if(preco_atual >= 30 and preco_atual < 80 and media_mensal >= 500 and media_mensal < 1000):
    preco_novo = preco_atual + preco_atual * 0.15
elif(preco_atual >= 80 and media_mensal >= 1000):
    preco_novo = preco_atual - preco_atual * 0.05
elif(preco_atual < 30 and media_mensal < 500):
    preco_novo = preco_atual + preco_atual * 0.10
else:
    preco_novo = preco_atual
print("O novo valor do produto: ", preco_novo)

#Fim.