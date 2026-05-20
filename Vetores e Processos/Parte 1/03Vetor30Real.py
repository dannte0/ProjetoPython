#10 - Python Vetores e Processos
vetor: float = [0]*5
acima_media: int = 0
abaixo_media: int = 0
media: float = 0.0

def main():
    acima_media = 0
    abaixo_media = 0
    soma_media = 0
    i: int = 0
    for i in range(5):
        vetor[i] = int(input(f"Digite a {i+1}a nota:"))
        while(vetor[i] < 0 or vetor[i] > 10):
            vetor[i] = int(input(f"Digite a {i+1}a nota:"))
        soma_media = soma_media + vetor[i] 
    media = soma_media / len(vetor)
    j: int = 0
    for j in range(5):
        if(vetor[j] > media):
            acima_media += 1
        if(vetor[j] < media):
            abaixo_media += 1
            
    print("A media dos valores é:", media)
    print("A quantidade de notas acima da media é:", acima_media)
    print("A quantidade de notas abaixo da media é:", abaixo_media)
    
if(__name__ == '__main__'):
    main()