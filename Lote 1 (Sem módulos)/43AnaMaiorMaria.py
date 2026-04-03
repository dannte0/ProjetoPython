#Algoritmo ESTREP_LT01_43
#Declarar.
alturaMaria: float = 0.0
alturaAna: float = 0.0
qntdAnos: int = 0

#Inicio.
alturaAna = 1.10
alturaMaria = 1.5
while(alturaAna <= alturaMaria):
    qntdAnos += 1
    alturaAna = alturaAna + 0.03
    alturaMaria = alturaMaria + 0.02
print(f"Levara {qntdAnos} anos para Ana ultrapassar a altura de Maria.")

#Fim.