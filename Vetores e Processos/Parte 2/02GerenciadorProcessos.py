#10 - Python Vetores e Processos
import platform
import subprocess

def os():
    system: str = ''
    system = platform.system()
    return system

def le_processo(j):
    vetor_proc: str = []
    vetor_proc = j.split(' ')
    subprocess.run(vetor_proc)
        
        
def verifica_os(os, op):
    if(os == 'Windows'):
        if(op == 1):
            return 'TASKLIST /FO TABLE'
        elif(op == 2):
            return 'TASKKILL /PID '
        elif(op == 3):
            return 'TASKKILL /IM '
        else:
            return 'Fim da aplicação no Windows'
    elif(os == 'Linux'):
        if(op == 1):
            return 'ps -ef'
        elif(op == 2):
            return 'kill -9 '
        elif(op == 3):
            return 'pkill -f '
        else:
            return 'Fim da aplicação no Linux'
    else:
        return 'S.O diferente'

def main():
    processo: str = ''
    info_processo: str = ''
    operacao: int = 0
    nome_os = os()
    
    while(operacao != 9):
        operacao = int(input("Digite um numero para uma operacao: \n1 – para listar os processos; \n2 – para matar por PID; \n3 – para matar por nome; \n9 – para encerrar a aplicação.\n=>"))
        processo = verifica_os(nome_os, operacao)
        
        if(operacao == 1):
            # print(processo)
            le_processo(processo)
        elif(operacao == 2):
            info_processo = input("Digite o numero do PID do processo: ")
            processo = processo + info_processo
            # print(processo)
            le_processo(processo)
        elif(operacao == 3):
            info_processo = input("Digite o nome do processo: ")
            processo = processo + info_processo
            # print(processo)
            le_processo(processo)
        else:
            print(processo)
        
    
if(__name__ == '__main__'):
    main()
