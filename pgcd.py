#pgcd
a = int(input("Saisir a: "))
b = int(input("Saisir b: "))
while True:
    if a<b:
        a,b = b,a
    if a-b == 0:
        break
    print(a,"-",b,"=",a-b)
    a = a-b
print(a)