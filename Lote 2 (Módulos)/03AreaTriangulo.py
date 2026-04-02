#Algoritmo ESTSEQ_LT02_03
#Declarar.
base: float = 0.0
altura: float = 0.0

#Início.

#Calcula a area do triangulo
def calcula_area(b, h):
    area = b * h / 2
    return area

#Modulo principal
def main():
    global base
    global altura
    base = float(input('Digite o valor da base do triângulo (cm): '))
    altura = float(input('Digite o valor da altura do triângulo (cm): '))
    print(calcula_area(base, altura))

#Chama modulo principal
if(__name__ == '__main__'):
    main()
#Fim.