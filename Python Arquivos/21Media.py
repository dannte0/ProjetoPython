#Algoritmo MODARQ_PYTHON_21
#Declarar.
import os
nome: str = ''
nota1: float = 0.0
nota2: float = 0.0
nota3: float = 0.0
nota4: float = 0.0
valor_media: float = 0.0
dir: str = ''
arq: str = ''

#Inicio.
#Recebe os valores
def entrada():
    global nome
    global nota1
    global nota2
    global nota3
    global nota4
    global valor_media
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite o valor da primeira nota: "))
    nota2 = float(input("Digite o valor da segunda nota: "))
    nota3 = float(input("Digite o valor da terceira nota: "))
    nota4 = float(input("Digite o valor da quarta nota: "))
    valor_media = med(nota1, nota2, nota3, nota4)
    print(valor_media)
    cadastro(nome, nota1, nota2, nota3, nota4, valor_media)
        
#Calcula a media
def med(n1, n2, n3 ,n4):
    media: float = 0.0
    media = (n1 + n2 + n3 + n4) / 4
    return media

#Registra a linha
def cadastro(nm, nt1, nt2, nt3, nt4, vlr_med):
    linha: str = ''
    global dir
    global arq
    dir = '/tmp/exercicios/'
    arq = 'ex21.txt'
    linha = (f"Nome: {nm} : Nota 1: {str(nt1)} ; Nota 2: {str(nt2)} ; Nota 3: {str(nt3)} ; Nota 4: {str(nt4)} ; Media final: {str(vlr_med)}\n")
    os.makedirs(dir, exist_ok=True)
    os.chmod(dir, 0o744)
    escreveArq(dir, arq, linha)

#Adiciona a linha ao arquivo txt
def escreveArq(caminho, arquivo, linha_arq):
    file: str = ''
    tipo: str = ''
    enc: str = ''
    if(os.path.exists(caminho) and os.path.isdir(caminho)):
        tipo = 'w'
        file = caminho + arquivo
        enc = 'utf-8'
        if(os.path.exists(file)):
            tipo = 'a'
        with open (file, tipo, encoding=enc) as file:
            file.write(linha_arq)
    else:
        print("Diretorio invalido.")

#Modulo principal
def main():
    contador = 0
    while(contador < 2):
        entrada()
        contador += 1

#Chama modulo principal
if(__name__ == '__main__'):
    main()
    
#Fim.