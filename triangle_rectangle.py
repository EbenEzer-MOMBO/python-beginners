print("Vérifions si ABC est un triangle rectangle...")
print()
end= False
while end!=True:
    a= int(input("Saisir la longueur a: "))
    b= int(input("Saisir la longueur b: "))
    c= int(input("Saisir la longueur c: "))
    if a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==a**2+b**2:
        print("Le triangle ABC est rectangle")
        end=True
    else:
        print("Le triangle ABC n'est pas rectangle")
        print()
