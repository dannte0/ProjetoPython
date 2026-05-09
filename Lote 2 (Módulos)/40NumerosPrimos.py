#Algoritmo ESTREP_LT02_40
#Declarar.
n1: int = 0
n2: int = 0
primo: int = 0
i: int = 0
cont: int = 0

#Inicio.
#Atribui um numero primo a variavel 'primo'
def atribui_nprimo(c):
    global n1
    p: int = 0
    if(c == 0 and n1 > 1):
        p = n1
        print(p)  

#Verifica se numero possui multiplo
def verifica_nprimo():
    global n1
    global n2
    while(n1 < n2):
        cont = 0
        for i in range(2, n1):
            if(n1 % i == 0):
                cont = n1
                break
        atribui_nprimo(cont)       
        n1 += 1

#Modulo principal
def main():
    global n1
    global n2
    n1 = int(input("n1: "))
    n2 = int(input("n2: "))
    print(f"Numeros primos entre {n1} e {n2}:")
    verifica_nprimo()
    
#Chama modulo principal
if(__name__ == '__main__'):
    main()
    
#Fim.