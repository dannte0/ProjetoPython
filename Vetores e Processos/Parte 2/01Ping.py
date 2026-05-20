#10 - Python Vetores e Processos
import platform
import subprocess

def os():
    system: str = ''
    system = platform.system()
    return system

def verifica_os(os):
    if(os == 'Windows'):
        return 'ping -4 -n 10 www.google.com.br'
    elif(os == 'Linux'):
        return 'ping -4 -c 10 www.google.com.br'
    else:
        return 'erro'

def le_processo(j):
    vetor_proc: str = []
    saida: str = ''
    linha: str = ''

    vetor_proc = j.split(' ')
    # print(vetor_proc)
    saida = subprocess.Popen(vetor_proc, stdout=subprocess.PIPE)
    linha = saida.stdout.readline().decode('utf-8', errors='ignore')
    while (linha != ''):
        if('Average' in linha):
            media = linha.split(' ') 
            print(f"Media = {media[12]}")
        elif('avg' in linha):
            media = linha.split('/')
            print(f"Avg = {media[4]}")
        linha = saida.stdout.readline().decode('utf-8', errors='ignore')

def main():
    processo: str = ''
    nome_os = os()
    processo = verifica_os(nome_os)
    le_processo(processo)
    
    
if(__name__ == '__main__'):
    main()

