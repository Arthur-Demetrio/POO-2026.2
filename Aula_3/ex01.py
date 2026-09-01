class Triangulo:
    def __init__(self):
        self.__b = 0
        self.__h = 0
    
    def set_base(self, v):
        if v >= 0: self.__b = v
        else: raise ValueError()
    def set_altura(self, v):
        if v >= 0: self.__h = v
        else: raise ValueError()
    def get_base(self):
        return self.__b
    def get_altura(self):
        return self.__h
def calcular_area(self):
        return self.__b * self.__h / 2


class UI:
    @staticmethod
    def main():
        x = Triangulo()
        x.b = int(input())
        x.h = int(input())
        print(x.b,x.h)
        print(x.calcular_area())

UI.main()