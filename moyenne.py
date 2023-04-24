n= float(input("entrez un nombre : "))
s=0
i=0
while True :
    if n>=0:
        s+=n
        i+=1
        n= float(input("entrez un nombre : "))
    else:
        moy= s/i
        print("la moyenne est de ",moy)
        break
    
        
