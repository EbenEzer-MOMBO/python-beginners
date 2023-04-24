import random
i=0
ianumber= random.randint(1,100)
mynumber = 0
typeGame = 0

#menu
print('-----------------------------------')
print('--------- Le Juste Prix -----------')
print('-----------------------------------\n\n')
while True:
    while(typeGame!="1" and typeGame!="2" and typeGame!="3"):
        print('1. Mode facile')
        print('2. Mode normal')
        print('3. Mode hardcore')
        typeGame = input('Choix du type de jeu: ')
        print()
    if typeGame == "1":
        print("J'ai choisi un nombre entre 1 et 100, devine lequel...?")
        while ianumber!=mynumber:
            mynumber= int(input("Entre un nombre entre 1 et 100: "))
            while mynumber<1 or mynumber>100:
                print("Haha, tu veux bug mon programme!")
                mynumber= int(input("Entre un nombre entre 1 et 100: "))
            
            if mynumber > ianumber:
                print("Plus petit...")
            if mynumber < ianumber:
                print("Plus grand...")
        print("Trouvé! Mon nombre était",ianumber)
        print()

    elif typeGame == "3":
        print("J'ai choisi un nombre entre 1 et 100, devine lequel...?(en 3 essais)")

        while ianumber!=mynumber:
            if i==3:
                break
            if i==2:
                print("Attention dernier essai!")
            mynumber= int(input("Entre un nombre entre 1 et 100: "))
            while mynumber<1 or mynumber>100:
                print("Haha, tu veux bug mon programme!")
                mynumber= int(input("Entre un nombre entre 1 et 100: "))
            
            if mynumber > ianumber:
                print("Plus petit...")
            if mynumber < ianumber:
                print("Plus grand...")
            i+=1
        if mynumber==ianumber:
            print("Trouvé! Mon nombre était",ianumber)
            print()
        else:
            print("Difficile n'est-ce pas?! Mon nombre était",ianumber)
            print()
    
    elif typeGame == "2":
        print("J'ai choisi un nombre entre 1 et 100, devine lequel...?(en 8 essais)")

        while ianumber!=mynumber:
            if i==8:
                break
            if i==7:
                print("Attention dernier essai!")
            mynumber= int(input("Entre un nombre entre 1 et 100: "))
            while mynumber<1 or mynumber>100:
                print("Haha, tu veux bug mon programme!")
                mynumber= int(input("Entre un nombre entre 1 et 100: "))
            
            if mynumber > ianumber:
                print("Plus petit...")
            if mynumber < ianumber:
                print("Plus grand...")
            i+=1
        if mynumber==ianumber:
            print("Trouvé! Mon nombre était",ianumber)
            print()
        else:
            print("Difficile n'est-ce pas?! Mon nombre était",ianumber)
            print()
    i=0
    ianumber= random.randint(1,100)
    mynumber = 0
    typeGame=0
