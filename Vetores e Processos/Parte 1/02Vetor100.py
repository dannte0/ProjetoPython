#10 - Python Vetores e Processos
vetor: int = [0]*100
maior: int = 0
menor: int = 0
media: float = 0.0

def main():
    maior = 0
    menor = 0
    soma_media = 0
    i: int = 0
    for i in range(100):
        vetor[i] = int(input(f"Digite o {i+1}o valor:"))
        soma_media = soma_media + vetor[i]
        
        if(vetor[i] > maior):
            maior = vetor[i]
        elif(vetor[i] < menor):
            menor = vetor[i]
        else:
            continue
 
    media = soma_media / len(vetor)
    print("A media dos valores é:", media)
    print("O maior numero é:", maior)
    print("O menor numero é:", menor)
    
if(__name__ == '__main__'):
    main()