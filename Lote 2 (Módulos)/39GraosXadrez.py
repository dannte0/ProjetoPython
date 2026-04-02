#Algoritmo ESTREP_LT02_39
#Declarar.
graos: int = 0
casa: int = 0
i: int = 0

#Inicio.
for i in range(1, 65):
    casa = i
    if(casa == 1):
        graos = 1
    else:
        graos = graos * 2
    print(f"Casa:{casa} Quantidade de Graos:{graos}")
    
#Fim.