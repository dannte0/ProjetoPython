#Algoritmo ESTDEC_LT02_26
#Declarar.
valor1: int = 0
valor2: int = 0

#Início.
def valores_multiplos():
    global valor1
    global valor2
    if(valor1 > valor2):
        if(valor1 % valor2 == 0):
            print(valor1, "multiplo de:", valor2)
        else:
            print(valor1, "maior, mas nao multiplo de: ", valor2)

    elif(valor2 > valor1):
        if(valor2 % valor1 == 0):
            print(valor2, "multiplo de:", valor1)
        else:
            print(valor2, "maior, mas nao multiplo de: ", valor1)

    else:
        print("Os valores sao iguais.")

def main():
    global valor1
    global valor2
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    valores_multiplos()
    
if(__name__ == '__main__'):
    main()
#Fim.