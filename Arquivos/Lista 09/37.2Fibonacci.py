#09 - Python Arquivos
import os 
dir: str = ''
arq: str = ''

def fibonacci():
    global atual
    global anterior
    proximo = atual + anterior
    anterior = atual
    atual = proximo
    return atual

def leArquivo(d, arq):
    arquivo = d + arq
    if(os.path.exists(d) and os.path.isdir(d)):
        with open(arquivo) as file:
            for linha in file:
                n = int(linha)
                num = verificaN(n)
                if(num != -1):
                    print(n)

def verificaN(num):
    if(num % 2 != 0):
        return num
    else:
        return -1
                        
def main(): 
    dir = 'c:\\temp\\exercicios\\'
    arq = 'ex37.txt'
    leArquivo(dir, arq)
        
if(__name__ == '__main__'):
    main()