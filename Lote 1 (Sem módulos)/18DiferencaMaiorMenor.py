#Algoritmo ESTDEC_LT01_18
#Declarar.
valor1: int = 0
valor2: int = 0
diferenca: int = 0

#Inicio.
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

if(valor1 > valor2):
    diferenca = valor1 - valor2
    print(diferenca)

elif(valor2 > valor1):
    diferenca = valor2 - valor1
    print(diferenca)

else:
    diferenca = 0
    print("valores iguais")

#Fim.