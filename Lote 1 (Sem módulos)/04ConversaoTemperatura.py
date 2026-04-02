#Algoritmo ESTSEQ_LT01_04
#Declarar.
celsius: float = 0.0
fahreinheit: float = 0.0

#Inicio.
celsius = float(input('Digite a temperatura em °C: '))
fahreinheit = (9 * celsius + 160) / 5
print('Temperatura: ', fahreinheit, '°F')

#Fim.