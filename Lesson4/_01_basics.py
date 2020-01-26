# Funzione: accetta dei parametri e ritona un risultato
# parametri opzionali sempre per ultimi
def somma(a, b, c = 0):
    return a+b+c

if __name__ == '__main__':
    print(somma(1,2)) # parametri posizionali
    print(somma(a=1, b=2)) # parametri nominali
    print(somma(1, b=2, c=3)) # misto (posizionali sempre prima dei nominali)



# funzioni accettano e tornano quello che volete (dizionari, set, list, tuple, funzioni, classi ...)
def somma_e_moltiplica(a, b, c = { 'k1' : 1, 'k2': 1 }):
    return (a*c['k1'] + b*c['k2'], a*c['k1'] * b*c['k2'])

if __name__ == '__main__':
    print(somma_e_moltiplica(1,2))



# migliora intellisense e documentazione del codice
def quadrato(parametro:int = 1) -> int:
    """
    Questo è un commento multilinea chiamato docstring.
    Documenta la funzione e migliora l'intellisense

    Args:
        parametro (int): Numero da elevare al quadrato

    Returns:
        int: quadrato del numero

    Examples:
        Examples should be written in doctest format, and should illustrate how
        to use the function.

        >>> print(quadrato(4))
        16
    """
    return parametro * parametro

if __name__ == '__main__':
    print(quadrato(2))
    print(type(quadrato))
    print(quadrato.__doc__)



def duplicate(parametro:int = 1) -> int:
    """
    Questo è un commento multilinea chiamato docstring.
    Documenta la funzione e migliora l'intellisense
    """
    return parametro + parametro

if __name__ == '__main__':
    print(duplicate())
    print(duplicate(2))
    print(duplicate("ciao"))



# *args = parametri indefiniti posizionali (tuple)
# **kwargs = parametri indefiniti nominali {dict}
def eseguiAll(parametroNormale, *args, **kwargs):
    print(type(args))
    print(type(kwargs))

    for argument in args:
        print(argument)
    for namedArgument in kwargs:
        print(f"{namedArgument} = {kwargs[namedArgument]}")

if __name__ == '__main__':
    eseguiAll("parametro", 1, 2, 3, 4, 5, tipo = "valore tipo", altro = "altro valore" )



if __name__ == '__main__':
    # AVANZATO... * e ** sono operatori di "unpacking"
    posizionali = (1,2)
    nominali = { 'c': 10 } 
    print(somma(*posizionali, **nominali))

    #* a volte è utile:
    a = {
        'a': 10,
        'b': 20
    }
    b = {
        'b': 100,
        'c': 1000
    }

    c = { **a, **b }
    print(c)