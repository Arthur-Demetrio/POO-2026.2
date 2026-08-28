import math 
class circulo:
    def __init__(self):
         self.r = 0
    def area(self):
        return math.pi * (self.r ** 2)
    def circumferencia(self):
        return 2 * math.pi * self.r

x = circulo()
x.r = 5
x.r = x.r/2
print(x.r)
print(x.area())
print(x.circumferencia())