import random
ianumber=0
i=0
print("Salut, mon supercalculateur va deviner ton nombre...")
mynumber= int(input("Entre un nombre entre 1 et 100: "))
while mynumber<1 or mynumber>100:
    print("Haha, tu veux bug mon programme!")
    mynumber= int(input("Entre un nombre entre 1 et 100: "))
while mynumber!=ianumber:
    ianumber= random.randint(1,100)
    if ianumber<mynumber:
        print("Plus grand...")
    if ianumber>mynumber:
        print("Plus petit...")
    i=i+1
print("Ton nombre était",ianumber)
print("Je l'ai trouvé après",i,"tentatives")