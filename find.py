phrase = input("Saisir une phrase: ")
lettre = input("Saisir la lettre à rechercher: ")
a= 0
for L in phrase:
    if L==lettre:
        a= a+1
print(a)
