
# performance
# performance listA * listB
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

num_el = 10_000 # 1_000_000 # 10_000_000
listA = list(range(0, num_el, 1))
listB = list(range(-num_el, num_el, 2))

listAnp = np.array(range(0, num_el, 1))
listBnp = np.array(range(-num_el, num_el, 2))


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
    res = np.multiply(npa, npb, out=npa)


usingListComprehensionWithZip(listA, listB)
usingMap(listA, listB)
usingNumpy(listAnp, listBnp)
usingNumpyNoAlloc(listAnp, listBnp)