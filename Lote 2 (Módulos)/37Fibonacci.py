#Algoritmo ESTREP_LT02_37
#Declarar.
anterior: int = 0
atual: int = 0
proximo: int = 0
n: int = 0

#Inicio
n = int(input("Digite o valor para receber a sequencia de Fibonacci: "))
atual = 1
anterior = 0
i = 2
while(i <= n):
    proximo = atual + anterior
    anterior = atual
    atual = proximo
    i += 1
    print(atual)
    
#Fim.