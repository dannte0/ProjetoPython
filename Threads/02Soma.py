#11 - Python Threads
import multiprocessing
import time
import random

def processamento(id, n):
    soma: int = 0
    print(f"Inicio do processo {id}")
    j: int = 0
    for i in n:
        j+=1
        soma = soma + i
        time.sleep(0.2)
        print(f"Linha {j} ==> {id} Soma: {soma}")
        
    print(f"Fim do processo {id}")
  
def main():
    params = [(0,0)] * 3
    cont: int = 0
    cont2: int = 0
    
    for cont in range(3):
        valores: int = [0] * 5
        
        for cont2 in range(5):
            valores[cont2] = random.randint(1, 100)
        params[cont] = (f"#J{cont}", valores)
        
    with multiprocessing.Pool(processes=3) as pool:
        pool.starmap(processamento, params)
        
if(__name__ == '__main__'):
    main()