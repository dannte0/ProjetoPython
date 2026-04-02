#Algoritmo ESTSEQ_LT02_06
#Declarar.
x: int = 0
y: int = 0

#Início.
#Realiza a troca dos valores
def troca_valores():
    global x
    global y
    z: int = 0
    z = x
    x = y
    y = z
    print('Valor de x:', x)
    print('Valor de y:', y)

#Modulo principal
def main():    
    global x
    global y
    x = int(input('Digite o primeiro valor (x): '))
    y = int(input('Digite o segundo valor (y): '))
    troca_valores()

#Chama o modulo principal
if(__name__ == '__main__'):
    main()
    
#Fim.