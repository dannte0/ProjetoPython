#Algoritmo ESTDEC_LT02_28
#Declarar.
media_mensal: int = 0
preco_atual: float = 0.0

#Início.
def calcula_preco(pa, mm):
    preco_novo: float = 0.0
    if(pa >= 30 and pa < 80 and mm >= 500 and mm < 1000):
        preco_novo = pa + pa * 0.15
    elif(pa >= 80 and mm >= 1000):
        preco_novo = pa - pa * 0.05
    elif(pa < 30 and mm < 500):
        preco_novo = pa + pa * 0.10
    else:
        preco_novo = pa
    print("O novo valor do produto: ", preco_novo)

def main():
    global media_mensal
    global preco_atual
    media_mensal = float(input("Digite a media de vendas por mes: "))
    preco_atual = float(input("Digite o preco do produto: "))
    calcula_preco(preco_atual, media_mensal)
    
if(__name__ == '__main__'):
    main()
#Fim.