#Algoritmo ESTREP_LT01_42
#Declarar.
serie: float = 0.0
a: int = 0
b: int = 0
i: int = 0

#Inicio.
serie = 1
a = 2
b = 3
i = 1
while(i < 50):
    serie = serie + a/b
    a += 1
    b += 2
    i += 1
print("Serie =", serie)

#Fim.