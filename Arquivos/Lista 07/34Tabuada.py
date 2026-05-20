#07 - Python Arquivos
import os
valor: int = 0
dir: str = ''
arq: str = ''

def main():
    global valor
    contador: int = 0
    result: int = 0
    
    valor = int(input("Digite um valor entre 1 e 10: "))
    while(valor < 1  or valor > 10):
        valor = int(input("Digite um valor entre 1 e 10: "))
        
    for contador in range(11):
        result = mult(valor, contador)
        print(f"{valor} * {contador} = {result}")
        grava(contador, result)

def mult(vlr, tab):
    res = vlr * tab
    return res

def grava(c, rslt):
    global dir
    global arq
    dir = '/tmp/exercicios/'
    arq = 'ex34.txt'
    file: str = ''
    tipo: str = ''
    enc: str = ''
    linha: str = '' 
    linha = str(rslt) + '\n'
    os.makedirs(dir, exist_ok=True)
    os.chmod(dir, 0o744)
    if(os.path.exists(dir) and os.path.isdir(dir)):
        tipo = 'w'
        file = dir + arq
        enc = 'utf-8'
        if(os.path.exists(file) and c > 0):
            tipo = 'a'
        with open (file, tipo, encoding=enc) as file:
            file.write(linha)
    else:
        print("Diretorio invalido.")

if(__name__ == '__main__'):
    main()
