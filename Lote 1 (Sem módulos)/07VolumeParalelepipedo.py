#Algoritmo ESTSEQ_LT01_07
#Declarar.
comprimento: float = 0.0
altura: float = 0.0
largura: float = 0.0
volume: float = 0.0

#Início.
comprimento = float(input('Digite o comprimento do paralelepípedo: '))
altura = float(input('Digite a altura do paralelepípedo: '))
largura = float(input('Digite a largura do paralelepípedo: '))
volume = comprimento * altura * largura
print('Volume do paralelepípedo:', volume, 'cm³')

#Fim.