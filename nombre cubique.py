#nombre cubique
a= int(input("Entrer un entier: "))
b= a
c= 0
while b>=10:
    c+=(b%10)**3
    b//=10
c+=(b%10)**3
if(a==c):
    print("ce nombre est cubique")
else:
    print("ce nombre n'est pas cubique")
