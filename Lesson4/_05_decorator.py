# Decorator: una funzione che "wrappa", circonda un altra funzione
import time

def StampaTempoFunzione(funzione):
   def func_wrapper(*args, **kwargs):
       #start = time.time_ns()
       result = funzione(*args, **kwargs)
       #end = time.time_ns()
       #print(f"{funzione.__name__}: Elapsed {(end-start)/1000/1000} ms")
       return result

   return func_wrapper


def AreaTrapezio(baseMinore, baseMaggiore, altezza):
    time.sleep(1)
    return (baseMinore+baseMaggiore)*altezza / 2

print(StampaTempoFunzione(AreaTrapezio)(10, 100, 5))
#print(StampaTempoFunzione(AreaTrapezio(10, 100, 5)))


# short way
@StampaTempoFunzione
def AreaTrapezio(baseMinore, baseMaggiore, altezza):
    time.sleep(1)
    return (baseMinore+baseMaggiore)*altezza / 2

print(AreaTrapezio(10, 100, 5)) # 275


# esempio altri usi: https://flask.palletsprojects.com/en/1.1.x/quickstart/