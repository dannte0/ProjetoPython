#10 - Python Vetores e Processos
vetor: int = [0]*50
soma_media: int = 0
soma_impar: int = 0
media: float = 0.0

def main():
    soma_impar = 0
    soma_media = 0
    for i in range(50):
        vetor[i] = int(input(f"Digite o {i+1}o numero:"))
        if(vetor[i] % 2 != 0):
            soma_impar = soma_impar + vetor[i]
        
        if(vetor[i] > 10 and vetor[i] < 200):
            soma_media = soma_media + vetor[i]
    media = soma_media / len(vetor)
    print("A media dos valores entre 10 e 200 é:", media)
    print("A soma dos numeros impares é:", soma_impar)
    
if(__name__ == '__main__'):
    main()