#Algoritmo ESTSEQ_LT02_02
#Declarar.
salario: float = 0.0
novo_salario: float = 0.0

#Início.
#Calcula o reajuste do salario
def calcula_salario():
    global novo_salario
    novo_salario = salario + (salario * 0.15)
    print('o salario com reajuste ficou: R$', novo_salario)

#Modulo principal
def main():
    global salario
    salario = float(input('Digite o salario: '))
    calcula_salario()

#Chama modulo principal
if(__name__ == '__main__'):
    main()
#Fim.