# Funzione: accetta dei parametri e ritona un risultato

def somma(a, b):
    return a+b

print(somma(1,2))
print(somma(a=1, b=2))
print(somma(1, b=2))


def quadrato(parametro:int = 1):
    """
    Questo è un commento multilinea chiamato docstring.
    Documenta la funzione e migliora l'intellisense
    """
    return parametro * parametro


print(quadrato())
print(quadrato(2))
print(quadrato.__doc__)


def duplicate(parametro:int = 1):
    """
    Questo è un commento multilinea chiamato docstring.
    Documenta la funzione e migliora l'intellisense
    """
    return parametro + parametro

print(duplicate())
print(duplicate(2))
print(duplicate("ciao"))

# pro decorator: *args, **kwargs
# *args = parametri indefiniti posizionali (tuple)
# **kwargs = parametri indefiniti nominali {dict}

def eseguiAll(parametroNormale, *args, **kwargs):
    for argument in args:
        print(argument)
    for namedArgument in kwargs:
        print(f"{namedArgument} = {kwargs[namedArgument]}")

eseguiAll("parametro", 1, 2, 3, 4, 5, tipo = "valore tipo", altro = "altro valore" )
