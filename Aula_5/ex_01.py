class Triangulo :
    def __init__(self, b, h):
        self.b = b
        self.h = h
    
    def __str__(self):
        return f"olá, eu sou um triangulo, minha base é {self.b}, minha altura é {self.h}"

x = Triangulo(10, 20)
print(x)
print(x.b, x.h)