# Rectangle and ArrayRectangles

class Rectangle:

    def __init__(self, sideA=8, sideB=8):
        self.sideA = sideA
        self.sideB = sideB
    def GetSideA(self):
        return self.sideA
    def GetSideВ(self):
        return self.sideB
    def Area(self):
        return self.sideA*self.sideB
    def Perimeter(self):
        return 2 * (self.sideA + self.sideB)
    def IsSquare(self):
        if self.sideA == self.sideB:
            print("The Rectangle is square")
        else:
            print("The Rectangle is NOT square")
    def ReplaceSides(self):
        self.sideA, self.sideB == self.sideB, self.sideA


r = Rectangle()
print(r.GetSideA(), r.GetSideВ(), r.Area(), r.Perimeter(), r.IsSquare(), r.ReplaceSides())

