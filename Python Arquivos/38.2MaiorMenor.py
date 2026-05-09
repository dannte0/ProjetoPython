import os

def gravaMultiplo(conteudo, dir):
    arq02 = 'ex38.2.txt'
    caminho = dir + arq02
    tipo = ''
    enc = ''
    l = 'Multiplo de 5:\n' + conteudo
    if(os.path.isdir(dir) and os.path.exists(dir)):
        tipo = 'w'
        enc = 'utf-8'
        if(os.path.exists(caminho)):
            tipo = 'a'
        with open(caminho, tipo, encoding=enc) as file:
            file.write(l)


def leArquivo(d, arq):
    arquivo = d + arq
    if(os.path.exists(d) and os.path.isdir(d)):
        with open(arquivo) as file:
            for linha in file:
                if('Maior' in linha or 'Menor' in linha):
                    continue
                else:
                    if(int(linha) % 5 == 0):
                        gravaMultiplo(linha, d)
def main():
    dir = '/tmp/exercicios/'
    arq01 = 'ex38.1.txt'
    leArquivo(dir, arq01)
        
if(__name__ == '__main__'):
    main()