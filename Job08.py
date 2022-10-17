largeur = int(input("Entrez la largeur : "))
hauteur = int(input("Entrez la hauteur : "))
if largeur == 0 or hauteur == 0:
    print("largeur ou hauteur nulle, pas de rectangle.")
    exit()
l, h = 1, 1
tiret = "-"
space = " "

while h <= hauteur:
    print("|", end="")
    if h == 1 or h == hauteur:
        print(largeur*tiret, end="")
    else:
        print(largeur*space, end="")
    print("|")
    h +=1

