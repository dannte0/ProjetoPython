#Algoritmo ESTSEQ_LT02_08
#Declarar.
deposito: float = 0.0

#Início.
#Calcula o rendimento da poupanca
def calcula_poupanca():
    global deposito
    poupanca: float = 0.0
    poupanca = deposito * 1.3 / 100 + deposito
    print('Valor final: R$', poupanca)
    
#Modulo principal
def main():
    global deposito
    deposito = float(input('Digite o valor depositado: '))
    calcula_poupanca()

#Chama modulo principal
if(__name__ == '__main__'):
    main()
#Fim.