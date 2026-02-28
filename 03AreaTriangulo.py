#Algoritmo ESTSEQ_LT01_03
#Declarar.
base: float = 0
altura: float = 0
area: float = 0

#Início.
base = float(input('Digite o valor da base do triângulo (cm): '))
altura = float(input('Digite o valor da altura do triângulo (cm): '))
area = base * altura / 2
print('A área do triângulo:', area, 'cm²')

#Fim.