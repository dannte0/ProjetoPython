#Algoritmo ESTSEQ_LT01_06
#Declarar.
x: int = 0
y: int = 0
z: int = 0

#Início.
x = int(input('Digite o primeiro valor (x): '))
y = int(input('Digite o segundo valor (y): '))
z = x
x = y
y = z
print('Valor de x:', x)
print('Valor de y:', y)

#Fim.