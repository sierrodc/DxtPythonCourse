from _01_basics import SpaceObject

class StarShip(SpaceObject):
    def __init__(self, position=(0,0)):
        super().__init__(position=position)
        self.acceleration = (0, 0)
    
    def accelerate(self, force):
        # print(list(zip(self.acceleration, force)))
        self.acceleration = tuple(x+y for x,y in zip(self.acceleration, force))


    def __str__(self):
        return f"StarShip at {self.position} moving at speed {self.speed} with acceleration {self.acceleration}"


if __name__ == '__main__':
    ss = StarShip()
    ss.accelerate((1, 2))
    print(ss)
    ss.accelerate((-1, 2))
    print(ss)
