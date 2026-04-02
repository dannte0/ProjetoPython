#Algoritmo ESTDEC_LT02_19
#Declarar.
a: float = 0.0
b: float = 0.0

#Inicio.
def verificaMaior():
    global a
    global b
    if(a > b):
        print("Maior valor:", a)
    elif(b > a):
        print("Maior valor:", b)
    else:
        print("Valores iguais")

def main():
    global a
    global b
    a = float(input("Digite o primeiro valor: "))
    b = float(input("Digite o segundo valor: "))
        
    verificaMaior()
    
if (__name__ == '__main__'):
    main()
#Fim.