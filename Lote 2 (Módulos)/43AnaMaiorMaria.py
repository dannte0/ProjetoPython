#Algoritmo ESTREP_LT02_43
#Declarar.
alturaMaria: float = 0.0
alturaAna: float = 0.0

#Inicio.
def calcula_altura(altura_a, altura_m):
    ano: int = 0
    while(altura_a <= altura_m):
        ano += 1
        altura_a = altura_a + 0.03
        altura_m = altura_m + 0.02
    return ano

def main():
    alturaAna = 1.10
    alturaMaria = 1.5
    qntdAnos: int = 0
    qntdAnos = calcula_altura(alturaAna, alturaMaria)
    print(f"Levara {qntdAnos} anos para Ana ultrapassar a altura de Maria.")
    
if(__name__ == '__main__'):
    main()
#Fim.