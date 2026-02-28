#Algoritmo ESTSEQ_LT01_08
#Declarar.
deposito: float = 0.0
poupanca: float = 0.0

#Início.
deposito = float(input('Digite o valor depositado: '))
poupanca = deposito * 1.3 / 100 + deposito
print('Valor final: R$', poupanca)

#Fim.