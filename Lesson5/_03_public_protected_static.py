from _02_Inheritance import StarShip


class StarShipFactory(StarShip):

    def __init__(self):
        super().__init__()
        self.__maxGameStarShips = 100 # "privato" = non visibile dall'esterno e da sottoclassi
        self._createdStarShips = [] # "protected" = visibile da sottoclassi, **per convenzione** non usabile pubblicamente

    def createStarShip(self):
        if self.__maxGameStarShips == 0:
            raise ValueError("max number of ships created by StarShips")
        self.__maxGameStarShips = self.__maxGameStarShips - 1
        ss = StarShip()
        self._createdStarShips.append(ss)
        return ss

    def __getitem__(self, i): # accedo alla classe con un indice: oggetto[i]
        return self._createdStarShips[i]

    def __len__(self):
        return len(self._createdStarShips)

    def __next__(self):
        for ss in self._createdStarShips:
            yield ss

    # statico = non relativo all'istanza, non ha il parametro "self"
    @staticmethod
    def createNewStarShipFactory():
        ssf = StarShipFactory()
        ssf.relocate((100, 100))
        return ssf

class DeathStar(StarShipFactory):
    def __init__(self):
        super().__init__()

    def createStarShip(self):
        ss = StarShip()
        self._createdStarShips.append(ss) # posso usare attributo protected
        ## self.__maxGameStarShips = 10 # Non posso!!!
        return ss
    
    def createFleet(self, quantity):
        return list(map(lambda idx: self.createStarShip(()), range(quantity)))
        


if __name__ == '__main__':
    # static method
    fact = StarShipFactory.createNewStarShipFactory()
    ss1 = fact.createStarShip()
    ss2 = fact.createStarShip()
    print(f"total ships: {len(fact)}")
    for ss in fact:
        print(ss)

    deathStar = DeathStar()
    fleet = deathStar.createFleet(100)
    print(deathStar[50])

    print("flotta imperiale creata, tanto basterà un jedi per distruggerla")