#Algoritmo ESTDEC_LT01_19
#Declarar.
a: float = 0.0
b: float = 0.0

#Inicio.
a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))

if(a > b):
    print("Maior valor:", a)
elif(b > a):
    print("Maior valor:", b)
else:
    print("Valores iguais")

#Fim.