#Algoritmo ESTDEC_LT02_27
#Declarar.
voltas: int = 0
circuito: float = 0.0
tempo: int = 0

#Início.
def calcula_velocidade_media(v, c, t):
    velocidade_media: float = 0.0
    if(tempo > 0):
        velocidade_media = v * c / 1000 / (t / 60)
        print("Velocidade media =", velocidade_media,"km/h")
    else:
        print("Tempo nao pode ser menor ou igual a 0.")
    
def main():
    global voltas
    global circuito
    global tempo
    voltas = int(input("Digite a quantidade de voltas: "))
    circuito = float(input("Digite a quantidade de metros percorridos: "))
    tempo = int(input("Digite a quantidade de minutos gastos: "))
    calcula_velocidade_media(voltas, circuito, tempo)

if(__name__ == '__main__'):
    main()
#Fim.