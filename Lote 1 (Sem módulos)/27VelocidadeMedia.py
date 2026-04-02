#Algoritmo ESTDEC_LT01_27
#Declarar.
voltas: int = 0
circuito: float = 0.0
tempo: int = 0
velocidade_media: float = 0.0

#Início.
voltas = int(input("Digite a quantidade de voltas: "))
circuito = float(input("Digite a quantidade de metros percorridos: "))
tempo = int(input("Digite a quantidade de minutos gastos:"))
if(tempo > 0):
    velocidade_media = voltas * circuito / 1000 / (tempo / 60)
    print("Velocidade media =", velocidade_media,"km/h")
else:
    print("Tempo nao pode ser menor ou igual a 0.")
#Fim.