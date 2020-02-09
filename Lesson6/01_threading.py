# al giorno d'oggi i processori sono multi-core 
# ==> possono eseguire più thread in parallelo (1 thread per core)
# se eseguo codice multithread, riesco a utilizzare tutte le risorse del mio processore
# ==> il mio programma è più veloce

# MA... in python esiste il GIL :(... vediamo

import sys
import time
from timeit import default_timer as perf_timer
import threading
import concurrent.futures

# native!
from myrustlib import NativeFibonacciClass

try:
    method = int(sys.argv[1])
except:
    method =  0



def getFibonacciNumber(ith_value):
    """
    Compute ith fibonacci number
    """
    index = 0
    a, b = 0, 1
    while index < ith_value:
        index = index + 1
        a, b = b, a + b
    
    return a

if method == 0 and __name__=='__main__':
    print("Method 0: Running python code")
    startTime = perf_timer()
    a = getFibonacciNumber(900_000)
    print(f"Number computed: Elapsed {(perf_timer()-startTime)*1000} ms")
    b = getFibonacciNumber(1_000_000) # milionesimo numero di fibonacci => 1.000.000 "sums+?"
    print(f"Number computed: Elapsed {(perf_timer()-startTime)*1000} ms")

if method == 1 and __name__=='__main__':
    print("Method 1: multithread : Thread class")

    class myThread(threading.Thread):
        def __init__(self, ith_value):
            super().__init__()
            self.ith_value = ith_value
            self.result = None

        def run(self):
            startTime = perf_timer()
            time.sleep(5)
            # self.result = getFibonacciNumber(self.ith_value)
            print(f"Number computed: Elapsed {(perf_timer()-startTime)*1000} ms")

    # inizializzo i thread
    t1 = myThread(900_000)
    t2 = myThread(1_000_000)
    startTime = perf_timer()
    # faccio partire i thread
    t1.start()
    t2.start()
    # aspetto che i thread terminino
    t1.join()
    t2.join()

    print(f"Numbers computed: Elapsed {(perf_timer()-startTime)*1000} ms")


if method == 2 and __name__=='__main__':
    # https://en.wikipedia.org/wiki/Thread_pool
    print("Method 2: multithread : ThreadPoolExecutor")
    with concurrent.futures.ThreadPoolExecutor() as executor: # default #core*5 --> min(32, os.cpu_count() + 4) --> used to I/O
        startTime = perf_timer()
        future1 = executor.submit(getFibonacciNumber, 900_000)
        future2 = executor.submit(getFibonacciNumber, 1_000_000)
        result1 = future1.result()
        result2 = future2.result()
        print(f"Numbers computed: Elapsed {(perf_timer()-startTime)*1000} ms")
        print(result2)
        

if method == 3 and __name__=='__main__':
    #https://datanoon.com/blog/multiprocessing_in_python/#multiprocessing-vs-multithreading
    print("Method 3: multiprocess: ProcessPoolExecutor")

    with concurrent.futures.ProcessPoolExecutor() as executor: # default 61
        startTime = perf_timer()
        future1 = executor.submit(getFibonacciNumber, 900_000)
        future2 = executor.submit(getFibonacciNumber, 1_000_000)
        result1 = future1.result()
        result2 = future2.result()
        print(f"Numbers computed: Elapsed {(perf_timer()-startTime)*1000} ms")

## GOING NATIVE!
## https://github.com/sierrodc/DxtPythonCourse_Native
if method == 4 and __name__=='__main__':
    print("------ method 4: NATIVE: single thread ------")
    nativeInstance9 = NativeFibonacciClass(900_000)
    nativeInstance10 = NativeFibonacciClass(1_000_000)

    startTime = perf_timer()
    a = nativeInstance9.get_fibonacci()
    print(f"Number computed: Elapsed {(perf_timer()-startTime)*1000} ms")
    b = nativeInstance10.get_fibonacci() # milionesimo numero di fibonacci => 1.000.000 "sums+?"
    print(f"Number computed: Elapsed {(perf_timer()-startTime)*1000} ms")
    exit()

if method == 5 and __name__=='__main__':
    print("------ method 5: NATIVE: multi thread ------")
    nativeInstance9 = NativeFibonacciClass(900_000)
    nativeInstance10 = NativeFibonacciClass(1_000_000)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        startTime = perf_timer()
        future1 = executor.submit(nativeInstance9.get_fibonacci)
        future2 = executor.submit(nativeInstance10.get_fibonacci)
        result1 = future1.result()
        result2 = future2.result()
        print(f"Numbers computed: Elapsed {(perf_timer()-startTime)*1000} ms")

if method == 6 and __name__=='__main__':
    print("------ method 6: NATIVE: multi thread + Release GIL ------")
    nativeInstance9 = NativeFibonacciClass(900_000)
    nativeInstance10 = NativeFibonacciClass(1_000_000)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        startTime = perf_timer()
        future1 = executor.submit(nativeInstance9.get_fibonacci_mt)
        future2 = executor.submit(nativeInstance10.get_fibonacci_mt)
        result1 = future1.result()
        result2 = future2.result()
        print(f"Numbers computed: Elapsed {(perf_timer()-startTime)*1000} ms")
        
