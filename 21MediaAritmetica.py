#Algotimo ESTDEC_LT01_21
#Declarar.
n1: float = 0.0
n2: float = 0.0
n3: float = 0.0
n4: float = 0.0
media: float = 0.0

#Início.
def calcula_media():
    global media
    media = (n1 + n2 + n3 + n4) / 4
    if(media < 3.0):
        print("RETIDO. Media:", media)
    elif(media >= 6.0):
        print("APROVADO. Media:", media)
    else:
        print("EXAME. Media:", media)

def main():
    global n1
    global n2
    global n3
    global n4
    n1 = float(input('Digite o valor da 1a nota: '))
    n2 = float(input('Digite o valor da 2a nota: '))
    n3 = float(input('Digite o valor da 3a nota: '))
    n4 = float(input('Digite o valor da 4a nota: '))
    while(n1 < 0 or n1 > 10 or n2 < 0 or n2 > 10 or n3 < 0 or n3 > 10 or n4 < 0 or n4 > 10):
        n1 = float(input('Digite o valor da 1a nota: '))
        n2 = float(input('Digite o valor da 2a nota: '))
        n3 = float(input('Digite o valor da 3a nota: '))
        n4 = float(input('Digite o valor da 4a nota: '))
    calcula_media()
    
if(__name__ == "__main__"):
    main()
#Fim.