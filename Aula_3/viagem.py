class viagem:
    def __init__(self):
        self.d = 0
        self.t = 0
    def velomedia(self):
        return self.d / self.t


x=viagem()
x.d = 200
x.t =5.5
print(x.velomedia())