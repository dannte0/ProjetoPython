#Algoritmo ESTSEQ_LT01_11
#Declarar.
import math
raio: float = 0.0
comprimento: float = 0.0

#Início.
raio = float(input('Digite o valor do raio (cm): '))
comprimento = 2 * math.pi * raio
print('Comprimento da circunferência:', comprimento, 'cm')

#Fim.