#Algoritmo ESTREP_LT02_44
#Declarar.
base: int = 0
expoente: int = 0

#Inicio.
def potencia(b, e):
    potencia: int = 0
    i: int = 0
    for i in range(1, e):
        if(i == 1):
            potencia = b * b
        else:
            potencia = potencia * b
    return potencia

def main():
    base = int(input("Digite o valor da base:"))
    expoente = int(input("Digite o valor do expoente:"))
    res = potencia(base, expoente)
    print(res)
    
if(__name__ == '__main__'):
    main()
#Fim.