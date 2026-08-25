print("digite 4 numeros")
e=4
l=[]
while not(e==0):
    x=int(input())
    l.append(x)
    e-=1

p=0
i=0
for e in l:
    if e%2==0:
        p+=e
    else:
        i+=e
print("soma dos pares = ", p)
print("soma dos ímpares = ", i)
