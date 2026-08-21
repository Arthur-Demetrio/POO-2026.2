x = int(input("digite o primeiro valor: "))
y = int(input("digite o segundo valor: "))
m=0
if x<y:
    m= x
    while x%m!=0 or y%m!=0:
        m-=1
elif x>y:
    m=y
    while x%m!=0 or y%m!=0:
        m-=1
print(m)
