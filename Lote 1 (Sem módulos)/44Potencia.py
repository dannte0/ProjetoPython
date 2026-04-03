#Algoritmo ESTREP_LT01_44
#Declarar.
base: int = 0
expoente: int = 0
potencia: int = 0
i: int = 0

#Inicio.
base = int(input("Digite o valor da base: "))
expoente = int(input("Digite o valor do expoente: "))
for i in range(1, expoente):
    if(i == 1):
        potencia = base * base
    else:
        potencia = potencia * base
print(f"Potencia de {base} ^ {expoente} = {potencia}")

#Fim.