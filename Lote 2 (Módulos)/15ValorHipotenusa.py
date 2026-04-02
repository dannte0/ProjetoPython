#Algoritmo ESTSEQ_LT02_15
#Declarar.
cateto_a: int = 0
cateto_b: int = 0
hipotenusa: int = 0

#Início.
cateto_a = int(input('Digite o valor do primeiro cateto: '))
cateto_b = int(input('Digite o valor do segundo cateto: '))
hipotenusa = (cateto_a ** 2 + cateto_b ** 2) ** 0.5
print('Valor da hipotenusa:', hipotenusa)

#Fim.