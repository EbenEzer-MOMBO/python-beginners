text= input("Entrer un texte ou un nombre: ")
possible= "0123456789"
trouver= True
for L in text:
    trouver= trouver and L in possible
if trouver:
    print("nombre")
