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

def grava(result, cont):
    global dir
    global arq
    dir = 'c:\\temp\\exercicios\\'
    os.makedirs(dir, exist_ok=True)
    os.chmod(dir, 0o744)
    
    arq = 'ex37.txt'
    file: str = ''
    tipo: str = ''
    enc: str = ''
    linha: str = ''
    linha = str(result) + '\n'
    if(os.path.exists(dir) and os.path.isdir(dir)):
        tipo = 'w'
        file = dir + arq
        enc = 'utf-8'
        if(os.path.exists(file) and cont > 1):
            tipo = 'a'
        with open (file, tipo, encoding=enc) as file:
            file.write(linha)
    else:
        print("Diretorio invalido")
        
def main(): 
    global atual
    global anterior
    atual = 1
    anterior = 0
    numero: int = 0
    numero = int(input("Digite o numero para receber a sequencia de fibonacci equivalente:"))
    i: int = 0
    for i in range(1, numero+1):
        res = fibonacci()
        grava(res, i)       
        
if(__name__ == '__main__'):
    main()