class Triangulo:
    def __init__(self):
        self.b = 0
        self.h = 0
    def calcular_area(self):
        return self.b * self.h / 2
x = Triangulo()
x.b = int(input())
x.h = int(input())
print(x.b,x.h)
print(x.calcular_area())