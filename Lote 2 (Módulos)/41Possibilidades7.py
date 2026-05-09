#Algoritmo ESTREP_LT02_41
#Declarar.
dado1: int = 0
dado2: int = 0

#Inicio.
def verifica_lados():
    for dado1 in range(1, 7):
        for dado2 in range(1, 7):
            if(dado1 + dado2 == 7):
                print(dado1, dado2)

def main():
    verifica_lados()

if(__name__ == '__main__'):
    main()
#Fim.