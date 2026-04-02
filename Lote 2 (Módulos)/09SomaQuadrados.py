#Algoritmo ESTSEQ_LT02_09
#Declarar.
n1: int = 0
n2: int = 0
#Início.
#Calcula a soma dos quadrados de dois numeros
def soma_quadrados(x, y):
    soma: int = 0
    soma = x * x + y * y
    return soma

#Modulo principal
def main():
    global n1
    global n2
    res: int = 0
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo valor: '))
    res = soma_quadrados(n1, n2)
    print('Soma dos quadrados:', res)

#Chama o modulo principal
if(__name__ == '__main__'):
    main()

#Fim.