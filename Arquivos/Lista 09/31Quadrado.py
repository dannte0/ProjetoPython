#09 - Python Arquivos
import os 
dir: str = ''
arq: str = ''

def calcula_quadrado(v):
    res: int = v * v
    return res

def grava(result, cont):
    global dir
    global arq
    dir = 'c:\\temp\\exercicios\\'
    os.makedirs(dir, exist_ok=True)
    os.chmod(dir, 0o744)
    
    arq = 'ex31.txt'
    file: str = ''
    tipo: str = ''
    enc: str = ''
    linha: str = ''
    linha = str(result) + '\n'
    if(os.path.exists(dir) and os.path.isdir(dir)):
        tipo = 'w'
        file = dir + arq
        enc = 'utf-8'
        if(os.path.exists(file) and cont > 10):
            tipo = 'a'
        with open (file, tipo, encoding=enc) as file:
            file.write(linha)
    else:
        print("Diretorio invalido")
        
def main():
    i: int = 0
    for i in range(10, 151):
        quadrado = calcula_quadrado(i)
        grava(quadrado, i)
        
        
if(__name__ == '__main__'):
    main()