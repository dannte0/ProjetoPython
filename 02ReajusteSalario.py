#Algoritmo ESTSEQ_LT01_02
#Declarar.
salario: float = 0.0
novo_salario: float = 0.0

#Início.
salario = float(input('Digite o salario: '))
novo_salario = salario + (salario * 0.15)
print('o salario com reajuste ficou: R$', novo_salario)

#Fim.