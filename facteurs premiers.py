b = int(input("Saisir un nombre: "))
i=2
while (b!=1):
    if b%i== 0:
        b= b/i
        print(i,"*",end="")
    else:
        i= i+1
print(1)