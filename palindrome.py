print("Vérifions si un nombre est un palindrome...")
a= int(input("Entrer un nombre à 3 chiffres: "))
while a<100 or a>999:
    a= int(input("Attention! Un nombre à 3 chiffres: "))
i=a//100
j=(a%100)//10
k=(a%10)
palin=(k*100)+(j*10)+i
if palin==a:
    print(a,"est un palindrome")
else:
    print(a,"n'est pas un palindrome")