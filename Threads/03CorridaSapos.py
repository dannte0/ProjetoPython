#11 - Python Threads
import multiprocessing
import time
import random

def processamento(id, f):
    percorreu = 0
    print(f'Sapo #N{id} iniciou a corrida')
    while(percorreu < f):
        salto = random.randint(1, 5)
        percorreu += salto
        time.sleep(0.2)
        print(f"Sapo #N{id} saltou {salto} cm e percorreu {percorreu} cm")
    print(f'Sapo #N{id} terminou a corrida')
    
def main():
    cont: int = 0
    params: int = [(0,0)]*5
    percurso: int = int(input("Digite o percurso a ser percorrido em cm: "))
    
    for cont in range(5):
        sapo = [0] * 20
        for cont2 in range(20):
            sapo[cont2] = random.randint(1, 5)
    
        params[cont] = (cont, percurso)
        
    print(f"Trajeto = {percurso} cm")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
        
    with multiprocessing.Pool(processes=5) as pool:
        pool.starmap(processamento, params)
        
if(__name__ == '__main__'):
    main()