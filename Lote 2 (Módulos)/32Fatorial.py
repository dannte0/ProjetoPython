#Algoritmo ESTREP_LT02_32
#Declarar.
numero: int = 0
fatorial: int = 0
i: int = 0

#Início.
numero = int(input("Digite o numero que deseja receber o fatorial: "))
fatorial = 1
i = numero
while(i > 1):
    fatorial = fatorial * i
    i -= 1
print(f"{numero}! = {fatorial}")

#Fim