n= int(input("Entrer un nombre: "))
i=1
f=1
while n!=1:
    f*=n
    n-=1
print("factorielle",n,"=",f)