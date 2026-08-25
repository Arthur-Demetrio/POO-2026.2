class circulo:
    def __init__(self):
        self.r = 0
    def area(self):
        return 3.14 *self.r * self.r
    def circumferencia(self):
        return 2 * 3.14 * self.r

x = circulo()
x.r = 5
print(x.r)
print(x.area())
print(x.circumferencia())