#Algoritmo ESTDEC_LT01_18
#Declarar.
valor1: int = 0
valor2: int = 0
diferenca: int = 0

#Inicio.
def diferenca():
    global diferenca 
    if(valor1 > valor2):
        diferenca = valor1 - valor2
        print(f"A diferenca entre {valor1} - {valor2} = {diferenca}")

    elif(valor2 > valor1):
        diferenca = valor2 - valor1
        print(f"A diferenca entre {valor2} - {valor1} = {diferenca}")

    else:
        diferenca = 0
        print("valores iguais")

def main():
    global valor1
    global valor2
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))

    diferenca()
        
if (__name__ == '__main__'):
    main()
#Fim.