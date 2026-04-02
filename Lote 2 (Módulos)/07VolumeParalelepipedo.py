#Algoritmo ESTSEQ_LT02_07
#Declarar.
comprimento: float = 0.0
altura: float = 0.0
largura: float = 0.0

#Início.
#Calcula o volume do paralelepipedo
def volume_p(c, h, l):
    volume: float = 0.0
    volume = c * h * l
    return volume

#Modulo principal
def main():
    comprimento = float(input('Digite o comprimento do paralelepípedo: '))
    altura = float(input('Digite a altura do paralelepípedo: '))
    largura = float(input('Digite a largura do paralelepípedo: '))
    res = volume_p(comprimento, altura, largura)
    print('Volume do paralelepípedo:', res, 'cm³')

#Chama modulo principal
if(__name__ == '__main__'):
    main()
#Fim.