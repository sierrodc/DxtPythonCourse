# Classe  = definisce la struttura di un oggetto (es: Int, str, List...)
#   - costruttore: funzione che inizializza
#   - metodi: funzioni definite dall'oggetto
#   - attributi: variabili legate alla classe o all'istanza
# Istanza = una valorizzazione di un oggetto (es: 3, "ciao", [2,3,4]...)


class StarObject:
    total_objects = 0

    def __init__(self, position = (0, 0)):
        StarObject.total_objects = StarObject.total_objects + 1
        self.position = position
        self.speed = (0, 0)
    
    def relocate(self, newPosition):
        self.position = newPosition

    def updatePosition(self, elapsedSeconds):
        #print(list(zip(self.position, speed)))
        self.position = tuple( pos + speed*elapsedSeconds for pos,speed in zip(self.position, self.speed))

    def __str__(self):
        return f"Object at {self.position} moving at speed {self.speed}"

    
if __name__ == '__main__':
    so = StarObject()
    print(f"There is an object at {so.position}")
    print(so)
    so.speed = (3, 5)
    so.updatePosition(2)
    print(so)




