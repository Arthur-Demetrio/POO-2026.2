x = int(input("digite o primeiro valor: "))
y = int(input("digite o segundo valor: "))
m=0
if x<y:
    m= x
    while m%x!=0 or m%y!=0:
        m+=1
elif x>y:
    m=y
    while m%x!=0 or m%y!=0:
        m+=1
print(m)