#Algoritmo ESTDEC_LT01_25
#Declarar.
hi:int = 0
mi:int = 0
hf:int = 0
mf:int = 0
hh:int = 0
mm:int = 0

#Inicio.
hi = int(input("Digite a hora inicial: "))
mi = int(input("Digite o minuto inicial: "))
hf = int(input("Digite a hora final: "))
mf = int(input("Digite o minuto final: "))

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

#Fim.