#Algotimo ESTREP_LT01_35
#Declarar.
n1: int = 0
n2: int = 0
resultado: int = 0
i: int = 0

#Início.
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
resultado = 0
if(n1 > n2):
    i = n2
    while (i < n1):
        if(i % 2 == 1):
            resultado = resultado + i
        i += 1
    print(f"Somatoria de impares entre {n2} e {n1} = {resultado}")
    
elif(n1 < n2):
    i = n1
    while(i < n2):
        if(i % 2 == 1):
            resultado = resultado + i
        i += 1
    print(f"Somatoria de impares entre {n1} e {n2} = {resultado}")
#Fim.