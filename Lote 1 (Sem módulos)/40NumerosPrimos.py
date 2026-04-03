#Algoritmo ESTREP_LT01_40
#Declarar.
n1: int = 0
n2: int = 0
primo: int = 0
i: int = 0
cont: int = 0

#Inicio.
n1 = int(input("n1: "))
n2 = int(input("n2: "))
print(f"Numeros primos entre {n1} e {n2}:")
while(n1 < n2):
    cont = 0
    for i in range(2, n1):
        if(n1 % i == 0):
            cont = n1
            break
            
    if(cont == 0 and n1 > 1):
        primo = n1
        print(primo)        
    n1 += 1
    
#Fim.