#Algotimo ESTREP_LT01_34
#Declarar.
numero: int = 0
resultado: int = 0

#Início.
numero = int(input("Digite o numero que deseja receber a tabuada: "))
for i in range(10):
    i += 1
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    
#Fim