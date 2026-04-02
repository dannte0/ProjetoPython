#Algoritmo ESTSEQ_LT02_04
#Declarar.
celsius: float = 0.0
fahreinheit: float = 0.0

#Inicio.
#Converte graus celsius para fahrenheit
def converte_graus_f():
    fahrenheit = (9 * celsius + 160) / 5
    print('Temperatura: ', fahrenheit, '°F')

#Modulo principal
def main():
    global celsius
    celsius = float(input('Digite a temperatura em °C: '))
    converte_graus_f()

#Chama modulo principal
if(__name__ == '__main__'):
    main()
#Fim.