#11 - Python Threads
import multiprocessing
import platform
import subprocess

def threads(id, j):
    vetor_proc = []
    media_final: int = 0
    vetor_proc = j.split(' ')
    saida = subprocess.Popen(vetor_proc, stdout=subprocess.PIPE)
    linha = saida.stdout.readline().decode('utf-8', errors='ignore')
    while (linha != ''):
        if('bytes' in linha):
            print(f"Ping {vetor_proc[4]} executando:")
            print(linha)
        if('Average' in linha):
            media = linha.split(' ')
            media_final = media[12]
        elif('avg' in linha):
            media = linha.split('/')
            media_final = media[4]
        linha = saida.stdout.readline().decode('utf-8', errors='ignore')
    print(f"{vetor_proc[4]} foi terminado.")
    print(f"Thread #{id} ({vetor_proc[4]}) levou em media {media_final}")
    
def verifica_os(os):
    if(os == 'Windows'):
        return 'ping -4 -n 10'
    elif(os == 'Linux'):
        return 'ping -4 -c 10'
    else:
        return 'erro'
    
def os():
    system: str = ''
    system = platform.system()
    return system

def main():
    so: str = ''
    so = os()
    params = [(0,0)] * 3
    processo = verifica_os(so)
    cont: int = 0
    servidor = [''] * 3
    for cont in range(3):
        if(cont == 0):
            servidor[cont] = processo + ' www.uol.com.br'
        elif(cont == 1):
            servidor[cont] = processo + ' www.google.com.br'
        elif(cont == 2):
            servidor[cont] = processo + ' www.terra.com.br'
        params[cont] = (cont, servidor[cont])

    with multiprocessing.Pool(processes=3) as pool:
        pool.starmap(threads, params)
    
if(__name__ == '__main__'):
    main()