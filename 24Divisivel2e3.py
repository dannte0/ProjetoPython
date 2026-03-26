#Algotimo ESTDEC_LT01_24
#Declarar.
valor: int = 0

#Início.
valor = int(input("Digite o valor: "))

if(valor % 2 == 0 and valor % 3 == 0):
    print("Divisivel por 2 e 3.")
    print(valor, "/ 2 = ", valor / 2)
    print(valor, "/ 3 = ", valor / 3)
elif(valor % 2 == 0):
    print("Divisivel apenas por 2.")
    print(valor, "/ 2 = ", valor / 2)
elif(valor % 3 == 0):
    print("Divisivel apenas por 3.")
    print(valor, "/ 3 = ", valor / 3)
else:
    print("Nao divisivel por 2 nem 3.")
    
#Fim.