#Algoritmo ESTDEC_LT02_25
#Declarar.
hi:int = 0
mi:int = 0
hf:int = 0
mf:int = 0
hh:int = 0
mm:int = 0

#Inicio.

def verifica_duracao():
    global hi
    global mi
    global hf
    global mf
    global hh
    global mm
    if(hf >= hi):
        hh = hf - hi
        if(mf >= mi):
            mm = mf - mi
        elif(mi > mf):
            hh = hh - 1
            mi = 60 - mi
            mm = mi + mf
    elif(hf < hi): 
        hi = 24 - hi
        if(mf >= mi):
            hh = hi + hf
            mm = mf - mi
        elif(mi > mf):
            hh = hi + hf - 1
            mi = 60 - mi
            mm = mi + mf
    print(f"Duracao da partida: {hh}:{mm}")

def main():
    global hi
    global mi
    global hf
    global mf
    hi = int(input("Digite a hora inicial: "))
    mi = int(input("Digite o minuto inicial: "))
    hf = int(input("Digite a hora final: "))
    mf = int(input("Digite o minuto final: "))
    while(hi < 0 or hi > 24 or mi < 0 or mi >= 24 or hf < 0 or hf >= 24 or mf < 0 or mf >= 24):
        hi = int(input("Digite a hora inicial: "))
        mi = int(input("Digite o minuto inicial: "))
        hf = int(input("Digite a hora final: "))
        mf = int(input("Digite o minuto final: "))
    verifica_duracao()
    
if(__name__ == '__main__'):
    main()   
#Fim.