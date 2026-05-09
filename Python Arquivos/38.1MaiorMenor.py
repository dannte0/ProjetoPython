import os
dir: str = ''
arq: str = ''

def grava(nMaior, nMenor):
    global dir
    global arq
    dir = '/tmp/exercicios/'
    arq = 'ex38.1.txt'
    file: str = ''
    tipo: str = ''
    enc: str = ''
    linha: str = ''
    linha = "Maior:\n" + str(nMaior) + "\nMenor:\n" + str(nMenor)
    os.makedirs(dir, exist_ok=True)
    os.chmod(dir, 0o744)
    if(os.path.exists(dir) and os.path.isdir(dir)):
        tipo = 'w'
        file = dir + arq
        enc = 'utf-8'
        with open (file, tipo, encoding=enc) as file:
            file.write(linha)
    else:
        print("Diretorio invalido.")

    
def verificaNumeros(cont, n):
    global maior
    global menor
    if(cont == 0):
        maior = n
        menor = n
    elif(n > maior):
        maior = n
    elif(n < menor):
        menor = n

def main():
    for i in range(5):
        numero = int(input("Digite um numero: "))
        while(numero < 0):
            print("Nao pode ser um numero negativo")
            numero = int(input("Digite outro numero: "))
        verificaNumeros(i, numero)
    grava(maior, menor)
        
if(__name__ == '__main__'):
    main()