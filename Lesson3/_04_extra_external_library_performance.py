
# performance
# performance listA * listB
from operator import mul
from timeit import default_timer as perf_timer
import numpy as np

num_el = 10_000 # 1_000_000
listA = list(range(0, num_el, 1))
listB = list(range(-num_el, num_el, 2))

listAnp = np.array(range(0, num_el, 1))
listBnp = np.array(range(-num_el, num_el, 2))

# METHOD 1: fullyPython
startTime = perf_timer()
listAB = [a*b for (a,b) in zip(listA,listB)] # [a*b for (a,b) in [(1,10), (2,20), (3,-20), (4,66)...]]
res1 = perf_timer() - startTime
del listAB

# METHOD 2: fullyPython (>3.5)
startTime = perf_timer()
listAB = list(map(mul,listA,listB))
res2 = perf_timer() - startTime
del listAB

# METHOD 3: NUMPY
startTime = perf_timer()
listABnp = listAnp * listBnp
res3 = perf_timer() - startTime
del listABnp

# METHOD 4: NUMPY NO ALLOCATION
startTime = perf_timer()
listABnp = np.multiply(listAnp, listBnp, out=listAnp)
res4 = perf_timer() - startTime
del listABnp

resmax = float(max([res1, res2, res3, res4]))
resmin = float(min([res1, res2, res3, res4]))
print(f"Elapsed: min {resmin}, max: {resmax}")

print(f"1°: Elapsed: {res1} \t speedUp: {resmax/float(res1)}x")
print(f"2°: Elapsed: {res2} \t speedUp: {resmax/float(res2)}x")
print(f"3°: Elapsed: {res3} \t speedUp: {resmax/float(res3)}x")
print(f"4°: Elapsed: {res4} \t speedUp: {resmax/float(res4)}x")