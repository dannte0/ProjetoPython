#Algoritmo ESTSEQ_LT01_17
#Declarar.
litros: int = 0
tempo: int = 0
velocidade_media: int = 0
distancia: int = 0

#Início.
tempo = int(input('Digite a quantidade de horas dirigidas: '))
velocidade_media = int(input('Digite a velocidade média percorrida: '))
distancia = velocidade_media * tempo
litros = distancia / 12
print('A quantidade de litros gasta foi de:', litros, 'l')

#Fim.