n= int(input("saisir le nombre de blocs: "))
i=0
a=n-1
while True:
    if s<n:
        a=a-1
        s=n-1
        s+=s
        i=i+1
    elif s>=n:
        print("la couche est: ",i)
        break
    else:
        print("a")
