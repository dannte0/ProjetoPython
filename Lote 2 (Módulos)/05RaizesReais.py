#Algotimo ESTSEQ_LT02_05
#Declarar.
a: float = 0.0
b: float = 0.0
c: float = 0.0

#Início.
#Calcula as raizes da equacao
def calcula_raiz():
    delta: float = 0.0
    raiz1: float = 0.0
    raiz2: float = 0.0
    delta = b ** 2 - 4 * a * c
    raiz1 = (-b + delta ** 0.5) / (2 * a)
    raiz2 = (-b - delta **  0.5) / (2 * a)
    print('Raiz 1:', raiz1)
    print('Raiz 2:', raiz2)

#Modulo principal
def main():
    global a
    global b
    global c
    a = float(input('Digite o coeficiente A: '))
    b = float(input('Digite o coeficiente B: '))
    c = float(input('Digite o coeficiente C: '))
    calcula_raiz()

#Chama modulo principal
if(__name__ == '__main__'):
    main()
  
#Fim.