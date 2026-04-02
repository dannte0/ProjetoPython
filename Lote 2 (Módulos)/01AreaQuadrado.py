#Algoritmo ESTSEQ_LT02_01
#Declarar.
lado: int = 0
area: int = 0
#Início.
#Calcula a area do quadrado
def calcula_area():
    area = lado * lado
    print('Área do quadrado:', area, 'cm²')

#Modulo principal
def main():
    global lado
    lado = int(input('Digite o tamanho do lado do quadrado (cm): '))
    calcula_area()
    
#Chama modulo principal
if(__name__ == '__main__'):
    main()
    
#Fim.