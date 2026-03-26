#Algotimo ESTREP_LT01_33
#Declarar.
numero: int = 0
fatorial: int = 0
i: int = 0

#Início.
numero = int(input("Digite o numero que deseja saber a serie: "))
serie = 1
i = 1
while(i < numero):
    serie = serie + 1/i
    i += 1
print("serie =", serie)

#Fim