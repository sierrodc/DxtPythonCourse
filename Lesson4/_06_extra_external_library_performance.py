import sys
from operator import mul
from timeit import default_timer as perf_timer
import numpy as np


def StampaTempoFunzione(description:str):
    def decorator(funzione):
        def func_wrapper(*args, **kwargs):
            startTime = perf_timer()

            result = funzione(*args, **kwargs)
            
            endTime = perf_timer()
            print(f"{description} {funzione.__name__}: Elapsed {(endTime-startTime)*1000} ms")
            return result
        return func_wrapper
    return decorator


# METHOD 1: fullyPython
@StampaTempoFunzione("METHOD 1: Python")
def usingListComprehensionWithZip(la, lb):
    res = [a*b for (a,b) in zip(la,lb)]

# METHOD 2: fullyPython
@StampaTempoFunzione("METHOD 2: Python")
def usingMap(la, lb):
    res = list(map(mul,la,lb))

# METHOD 3: NUMPY
@StampaTempoFunzione("METHOD 3: Numpy")
def usingNumpy(npa, npb):
    res = npa * npb

# METHOD 4: NUMPY NO ALLOCATION
@StampaTempoFunzione("METHOD 4: Numpy no alloc")
def usingNumpyNoAlloc(npa, npb):
    res = np.multiply(npa, npb, out=npa, dtype=np.int)


# object definition
try:
    if len(sys.argv) > 1:
        num_el = int(sys.argv[1])
    else:
        num_el =  10_000
except:
    num_el =  10_000 # 1_000_000 # 10_000_000

print(f"Numbers of elements: {num_el:,.2f} total size: {num_el*4/1024/1024:,.2f} Mb")

listA = list(range(0, num_el, 1))
listB = list(range(-num_el, num_el, 2))

listAnp = np.array(listA, dtype=np.int)
listBnp = np.array(listB, dtype=np.int)

# execution

usingListComprehensionWithZip(listA, listB)
usingMap(listA, listB)
usingNumpy(listAnp, listBnp)
usingNumpyNoAlloc(listAnp, listBnp)