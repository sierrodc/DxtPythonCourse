# puntatore: Etichetta che ha riferimento ad una funzione
from _01_basics import somma, quadrato

if __name__ == '__main__':
    x = somma
    print(somma(1,2))
    print(x(1,2))


def ritornaOperazioneFactory(tipo: str):
    if tipo == "quadrato":
        return quadrato
    if tipo == "somma":
        return somma

if __name__ == '__main__':
    print(ritornaOperazioneFactory("somma")(2, 3))
    funzioneQuadrato = ritornaOperazioneFactory("quadrato")
    print(funzioneQuadrato(2))
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

if __name__ == '__main__':
    miaFunzioneRichiedeCallback(2, 3, myErrorCallback)