# puntatore: Etichetta che ha riferimento ad una funzione
from _01_basics import somma, quadrato

x = somma
print(somma(1,2))
print(x(1,2))


def ritornaOperazioneFactory(tipo):
    if tipo == "quadrato":
        return quadrato
    if tipo == "somma":
        return somma

print(ritornaOperazioneFactory("somma")(2, 3))
print(ritornaOperazioneFactory("quadrato")(2))
# print(ritornaOperazioneFactory("somma")(2))

# -------------------------------
# come può essere realmente usato:
def miaFunzioneRichiedeCallback(param1, param2, errorCallback):
    if type(param1) != int:
        errorCallback("Il primo parametro deve essere un intero")
    if type(param2) != str:
        errorCallback("Il secondo parametro deve essere un intero")


def myErrorCallback(message:str):
    print(message)


miaFunzioneRichiedeCallback(2, 3, myErrorCallback)