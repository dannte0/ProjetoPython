#Algoritmo ESTDEC_LT01_22
#Declarar.
a: int = 0
b: int = 0

#Início.
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))

if(a < b):
    print("Em ordem crescente:", a, b)
elif(a > b):
    print("Em ordem crescente:", b, a)
else:
    print("Valores iguais")
#Fim.