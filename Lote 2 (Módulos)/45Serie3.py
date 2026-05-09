#Algoritmo ESTREP_LT02_45
#Inicio.
def calcula_serie():
    a: int = 2
    b: int = 4
    i: int = 1
    serie: float = 1.0
    while(i < 15):
        if(i % 2 == 0):
            serie = serie + a/b
        else:
            serie = serie - a/b
        a += 1
        b = a ** 2
        i += 1
    return serie

def main():
    res = calcula_serie()
    print(res)
    
if(__name__ == '__main__'):
    main()    
    
#Fim.