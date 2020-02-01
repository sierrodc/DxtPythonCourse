# Classe  = definisce la struttura di un oggetto (es: Int, str, List...)
#   - costruttore: funzione che inizializza
#   - metodi: funzioni definite dall'oggetto
#   - attributi: variabili legate alla classe o all'istanza
# Istanza = una valorizzazione di un oggetto (es: 3, "ciao", [2,3,4]...)


class StarObject:
    total_objects=0

    def __init__(self, position = (0, 0)):
        self.__position = position
        self.__speed = (0, 0)
        self._x = 9
    
    def relocate(self, newPosition):
        self.__position = newPosition

    def print(self):
        print(self._x)


class Starship(StarObject):
    def __init__(self):
        super().__init__()
        self._x = 10
    
    
    
ss = Starship()
print(ss._x)
ss.print()



