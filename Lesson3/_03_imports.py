from math import pi, cosh # importa solo la variabile pi e la funzione cosh
import random as rnd # importa tutte le definizioni di random sotto il nome di "rnd"
import time # importa tutte le definizioni (classi, funzioni, variabili) sotto il nome originale

print(cosh(pi))

print(rnd.randint(1, 10))

startTime = time.time() # seconds since epoch = 01/01/1970 00:00:00
print(startTime)
time.sleep(1.5)
print(f"Elapsed: {time.time() - startTime}")


### import from where?!?!
import sys 
print(sys.executable)
for path in sys.path:
    print(path)


# attenzione al flusso di codice
import to_import._03_to_import as toImp
print(toImp.somma(toImp.a,2))