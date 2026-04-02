#Algoritmo ESTREP_LT02_36
#Declarar.
i: int = 0
n: int = 0
fatorial: int = 0
serie: float = 0.0

#Inicio.
n = int(input("Digite o numero para receber a serie (!): "))
fatorial = 1
serie = 1.0
for i in range(1, n + 1):
    fatorial = fatorial * i
    serie = serie + 1/fatorial
print(serie)

#Fim.