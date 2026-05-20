#11 - Python Threads
import multiprocessing
import time

def processamento(id):
    time.sleep(0.5)
    print('Thread #', id)
    
def main():
    i: int = 0
    params: int = [0]*5
    
    for i in range(5):
        params[i] = i
        
    with multiprocessing.Pool(processes=5) as pool:
        pool.map(processamento, params)
        
if(__name__ == '__main__'):
    main()