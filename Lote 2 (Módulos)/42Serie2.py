#Algoritmo7 ESTREP_LT02_42
#Declarar.
a: int = 0
b: int = 0
i: int = 0

#Inicio.
def calcula_serie(x, y, cont):
    serie: float = 0.0
    serie = 1.0
    while(cont < 50):
        serie = serie + x/y
        x += 1
        y += 2
        cont += 1
    return serie

def main():
    a = 2
    b = 3
    i = 1
    res: float = 0.0
    res = calcula_serie(a, b, i)
    print("Serie =", res)
    
if(__name__ == '__main__'):
    main()
#Fim.