#Algoritmo ESTREP_LT01_45
#Declarar.
serie: float = 0.0
a: int = 0
b: int = 0
i: int = 0

#Inicio.
serie = 1
a = 2
b = 4
i = 1
while(i < 15):
    if(i % 2 == 0):
        serie = serie + a/b
    else:
        serie = serie - a/b
    a += 1
    b = a ** 2
    i += 1
print("Serie =", serie)

#Fim.