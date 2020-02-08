# al giorno d'oggi i processori sono multi-core = possono eseguire più thread in parallelo (1 thread per core)
# se eseguo codice multithread, riesco a utilizzare tutte le risorse del mio processore => il mio programma è più veloce
# MA... in python esiste il GIL :(

import time
from timeit import default_timer as perf_timer
import threading

def StampaTempoFunzione(funzione):
    def func_wrapper(*args, **kwargs):
        startTime = perf_timer()
        result = funzione(*args, **kwargs)
        
        endTime = perf_timer()
        print(f"{funzione.__name__}: Elapsed {(endTime-startTime)*1000} ms")
        return result
    return func_wrapper

def getFibonacciNumber(ith_value):
    index = 0
    a, b = 0, 1
    while index < ith_value:
        index = index + 1
        a, b = b, a + b
    
    return 
    
def getFibonacciNumberPrintingTime(ith_value):
    return StampaTempoFunzione(getFibonacciNumber)(ith_value)

if __name__ == '__main__':
    a = getFibonacciNumberPrintingTime(1000000)

if __name__ == '__main__':
    print("------ Using Thread Class ------")

class myThread(threading.Thread):
    def __init__(self, ith_value):
        super().__init__()
        self.ith_value = ith_value
        self.result = None

    def run(self):
        # time.sleep(5)
        self.result = getFibonacciNumberPrintingTime(self.ith_value)
        print("thread done")

@StampaTempoFunzione
def runThreads():
    # inizializzo i thread
    t1 = myThread(1000000)
    t2 = myThread(1000000)
    # faccio partire i thread
    t1.start()
    t2.start()
    # aspetto che i thread terminino
    t1.join()
    t2.join()

runThreads()


print("------ method 1: ThreadPoolExecutor ------")

import concurrent.futures
@StampaTempoFunzione
def usingMultiThread():
    with concurrent.futures.ThreadPoolExecutor() as executor: # default #core*5 --> min(32, os.cpu_count() + 4) --> used to I/O
        future1 = executor.submit(getFibonacciNumberPrintingTime, 1000000)
        future2 = executor.submit(getFibonacciNumberPrintingTime, 1000000)
        result1 = future1.result()
        result2 = future2.result()
        print("done with ThreadPoolExecutor")

usingMultiThread()


print("------ method 2: ProcessPoolExecutor ------")

import concurrent.futures
@StampaTempoFunzione
def usingMultiProcess():
    with concurrent.futures.ProcessPoolExecutor() as executor: # default 61
        future1 = executor.submit(getFibonacciNumberPrintingTime, 1000000)
        future2 = executor.submit(getFibonacciNumberPrintingTime, 1000000)
        result1 = future1.result()
        result2 = future2.result()
        print("done with ProcessPoolExecutor")

usingMultiProcess()