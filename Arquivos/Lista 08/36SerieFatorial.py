#08 - Python Arquivos
import os
dir: str = 0
arq: str = 0

def grava(c, s):
    global dir
    global arq
    dir = '/tmp/exercicios/'
    arq = 'ex36.txt'
    file: str = ''
    tipo: str = ''
    enc: str = ''
    linha: str = ''
    linha = '1 / ' + str(c) + '! = ' + str(s)  + '\n'
    os.makedirs(dir, exist_ok=True)
    os.chmod(dir, 0o744)
    if(os.path.isdir(dir) and os.path.exists(dir)):
        tipo = 'w'
        file = dir + arq
        enc = 'utf-8'
        if(os.path.exists(file) and c > 1):
            tipo = 'a'
        with open (file, tipo, encoding=enc) as file:
            file.write(linha)
    else:
        print("Diretorio invalido.")
        
def fatorial(cont, n):
    fat = cont * n
    return fat

def divisao(f):
    div = 1 / f
    return div

def main():
    numero = int(input("Digite um numero: "))
    res_fat = 1
    res_serie = 1
    for i in range(1, numero+1):
        res_fat = fatorial(i, res_fat)
        res_serie = res_serie + divisao(res_fat)
        print(res_serie)
        grava(i, res_serie)
    
if(__name__ == '__main__'):
    main()