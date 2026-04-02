#Algoritmo ESTREP_LT01_38
#Declarar.
n: int = 0
maior: int = 0
menor: int = 0
i: int = 0

#Inicio.
for i in range(100):
    n = int(input(f"Digite o numero {i}: "))
    if(n > 0):
        if(i == 0):
            maior = n
            menor = n
        elif(n > maior):
            maior = n
        elif(n < menor):
            menor = n
print("Menor numero:", menor)
print("Maior numero:", maior)

#Fim.