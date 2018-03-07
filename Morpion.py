from tkinter import *
from random import *

# Mettre sur True si on veut utiliser l'IA
global useIA
useIA = True


# On commence par creer la grille de 3*3
# Pour ça, on utilise trois listes, une pour chaque rangée.
global rHaut
global rMilieu
global rBas

# On ajoute trois fois une valeur à chaque rangée.
# La valeur changera lorsqu'un joueur prendra une case.
# La valeur de base est "null".

def ResetGrille():    
    global rHaut
    rHaut = []
    global rMilieu
    rMilieu = []
    global rBas
    rBas = []
    
    for i in range(3):
        valeur = "null"
        rHaut.append(valeur)
        rMilieu.append(valeur)
        rBas.append(valeur)

ResetGrille()


# On va maintenant creer la partie graphique.

# Pour faire apparaître le tout, on créer une instance Tkinter, puis un canvas.

FENETRE = Tk()
FENETRE.title("Morpion - ISN")
FENETRE.configure(bg = "white", width = 600, height = 600)

CANVAS = Canvas(FENETRE, width = 400, height = 400, bg = "white", bd = 1)
CANVAS.place(x = 100, y = 100)

# On définit les images globales.

global grille_img
global cercle_img
global croix_img

grille_img = PhotoImage(file="Images/Grille_400.gif")
cercle_img = PhotoImage(file="Images/Cercle.gif")
croix_img = PhotoImage(file="Images/Croix.gif")

# On fait apparaître l'image de fond.

grille = CANVAS.create_image(200, 200, image=grille_img)

# Et on créer une liste pour contenir toutes les croix et les cercles.

global images
images = []

# Avant de définir comment on selectionne une case, on creer la définition
# qui vérifie si un joueur à gagner et celle de la fin du jeu.

def Recommencer():
    global texteFin
    global boutonFin

    texteFin.destroy()
    boutonFin.destroy()

    global images

    for item in images:
        CANVAS.delete(item)

    ResetGrille()

def FinDuJeu(gagnant):
    global texteFin

    texteFin = Label(FENETRE, width = 55, height = 3, bg = "white", text = gagnant + " ont gagnés.")
    texteFin.configure(font=(32))
    texteFin.place(x = 60,y = 20)

def VerifieVictoire():
    global rHaut
    global rMilieu
    global rBas

    gagnant = str("")

    # On vérifie la colonne de gauche.
    if rHaut[0] == rMilieu[0] and rMilieu[0] == rBas[0]:
        gagnant = rHaut[0]

    # On vérifie la colonne du milieu.
    elif rHaut[1] == rMilieu[1] and rMilieu[1] == rBas[1]:
        gagnant = rHaut[1]

    # On vérifie la colonne de droite.
    elif rHaut[2] == rMilieu[2] and rMilieu[2] == rBas[2]:
        gagnant = rHaut[2]

    # On vérifie la ligne du haut.
    elif rHaut[0] == rHaut[1] and rHaut[1] == rHaut[2]:
        gagnant = rHaut[0]

    # On vérifie la ligne du milieu.
    elif rMilieu[0] == rMilieu[1] and rMilieu[1] == rMilieu[2]:
        gagnant = rMilieu[0]

    # On vérifie la ligne de bas.
    elif rBas[0] == rBas[1] and rBas[1] == rBas[2]:
        gagnant = rBas[0]

    # On vérifie la diagonale Haut-Gauche/Bas-Droite
    elif rHaut[0] == rMilieu[1] and rMilieu[1] == rBas[2]:
        gagnant = rHaut[0]
    
    # On vérifie la diagonale Bas-Gauche/Haut-Droit
    elif rHaut[2] == rMilieu[1] and rMilieu[1] == rBas[0]:
        gagnant = rHaut[2]

    else:
        gagnant = "null"

    if gagnant != "null":
        FinDuJeu(gagnant)

VerifieVictoire()

# Maintenant, creer les définitions qui vont creer les croix et les cercles
# aux bonnes positions.
# Les deux définitons sont les mêmes.

def CreationCercle(x,y):
    global images
    global cercle_img

    # On fait apparaître le cercle.
    nouveauCercle = CANVAS.create_image(x,y, image = cercle_img)

    # Et on l'ajoute à la liste.
    images.append(nouveauCercle)

def CreationCroix(x,y):
    global images
    global croix_img

    # On fait apparaître le cercle.
    nouvelleCroix = CANVAS.create_image(x,y, image = croix_img)

    # Et on l'ajoute à la liste.
    images.append(nouvelleCroix)

# Il ne reste plus qu'a detecter où le joueur clique.
# On va utiliser la fonction .bind qui associe une entrée (ici
# le click de la souris) à une fonction.

def click(event):
    # Le paramètre event est donc envoyé par le click de la souris.
    # Grace à lui, on connait les coordonnées x et y du click.
    # On peut donc detecter où le joueur à cliquer.

    print("click",event.x, event.y)

    global rHaut
    global rMilieu
    global rBas

    x = event.x
    y = event.y

    imagePosX = 0
    imagePosY = 0

    case = str("")
    index = 0

    # Rangée du haut.
    if x > 0 and x < 130 and y > 0 and y < 130:
        # La case en haut à gauche a été selectionnée.
        imagePosX = 65
        imagePosY = 65
        case = "rHaut"
        index = 0

    elif x > 135 and x < 265 and y > 0 and y < 130:
        # La case en haut au milieu a été selectionnée.
        imagePosX = 65 + 135
        imagePosY = 65
        case = "rHaut"
        index = 1

    elif x > 270 and x < 400 and y > 0 and y < 130:
        # La case en haut à droite a été selectionnée.
        imagePosX = 65 + 135*2
        imagePosY = 65
        case = "rHaut"
        index = 2

    # Rangée du milieu.
    elif x > 0 and x < 130 and y > 135 and y < 265:
        # La case du milieu à gauche a été selectionnée.
        imagePosX = 65
        imagePosY = 65 + 135
        case = "rMilieu"
        index = 0

    elif x > 135 and x < 265 and y > 135 and y < 265:
        # La case du milieu au milieu a été selectionnée.
        imagePosX = 65 + 135
        imagePosY = 65 + 135
        case = "rMilieu"
        index = 1

    elif x > 270 and x < 400 and y > 135 and y < 265:
        # La case du milieu à droite a été selectionnée.
        imagePosX = 65 + 135*2
        imagePosY = 65 + 135
        case = "rMilieu"
        index = 2

    # Rangée du bas.
    elif x > 0 and x < 130 and y > 270 and y < 400:
        # La case du bas à gauche a été selectionnée.
        imagePosX = 65
        imagePosY = 65 + 135*2
        case = "rBas"
        index = 0

    elif x > 135 and x < 265 and y > 270 and y < 400:
        # La case du bas au milieu a été selectionnée.
        imagePosX = 65 + 135
        imagePosY = 65 + 135*2
        case = "rBas"
        index = 1

    elif x > 270 and x < 400 and y > 270 and y < 400:
        # La case du bas à droite a été selectionnée.
        imagePosX = 65 + 135*2
        imagePosY = 65 + 135*2
        case = "rBas"
        index = 2


    global tour
    global useIA
    
    # On place alors une image, si la case n'est pas utilisée.
    if case == "rHaut":
        if rHaut[index] == "null":
            if tour == 1:
                # On créer alors un cercle.
                CreationCercle(imagePosX, imagePosY)

                # Et on change la valeur de la case.
                rHaut[index] = "Cercle"
            else:
                # On créer alors une croix.
                CreationCroix(imagePosX, imagePosY)

                # Et on change la valeur de la case.
                rHaut[index] = "Croix"

            # Et on change de tour.
            tour = tour * -1
            if useIA == True:
                TourIA()            
                
    elif case == "rMilieu":
        if rMilieu[index] == "null":
            if tour == 1:
                # On créer alors un cercle.
                CreationCercle(imagePosX, imagePosY)

                # Et on change la valeur de la case.
                rMilieu[index] = "Cercle"
            else:
                # On créer alors une croix.
                CreationCroix(imagePosX, imagePosY)

                # Et on change la valeur de la case.
                rMilieu[index] = "Croix"

            # Et on change de tour.
            tour = tour * -1
            if useIA == True:
                TourIA() 
                
    else:
        if rBas[index] == "null":
            if tour == 1:
                # On créer alors un cercle.
                CreationCercle(imagePosX, imagePosY)

                # Et on change la valeur de la case.
                rBas[index] = "Cercle"
            else:
                # On créer alors une croix.
                CreationCroix(imagePosX, imagePosY)

                # Et on change la valeur de la case.
                rBas[index] = "Croix"

            # Et on change de tour.
            tour = tour * -1
            if useIA == True:
                TourIA() 

    VerifieVictoire()
    

# On fait la définition de l'IA.
def TourIA():
    global rHaut
    global rMilieu
    global rBas

    # On creer une liste de toutes les case libres.
    cases = []

    for i in range(3):
        if rHaut[i] == "null":
            c = "rHaut_"+str(i)
            cases.append(c)
        if rMilieu[i] == "null":
            c = "rMilieu_"+str(i)
            cases.append(c)
        if rBas[i] == "null":
            c = "rBas_"+str(i)
            cases.append(c)


    caseRandom = randint(0,len(cases)-1)

    caseSTR = cases[caseRandom]
    print("CaseSTR", caseSTR)

    # On a donc une case libre tirée au hasard.
    # Le text contient la rangée et la colone de la case.
    # Il faut juste analyser le texte pour savoir quelle case choisir pour
    # obtenir des coordonnées.

    colonne = str("")

    for caracter in caseSTR:
        if caracter.isdigit() == True:
            colonne = colonne + caracter

    # On converti colonne en nombre.
    colonne = eval(colonne)
    print("Colonne",colonne)

    posX = 0
    posY = 0

    # Si caseSTR contient "rHaut"
    if caseSTR.count("rHaut") > 0:
        posX = 65 + 135 * colonne
        posY = 65
        rHaut[colonne] = "Croix"
        
    if caseSTR.count("rMilieu") > 0:
        posX = 65 + 135 * colonne
        posY = 65 + 135
        rMilieu[colonne] = "Croix"
        
    if caseSTR.count("rBas") > 0:
        posX = 65 + 135 * colonne
        posY = 65 + 135 * 2
        rBas[colonne] = "Croix"

    # On place ensuite la croix.
    CreationCroix(posX, posY)

    global tour
    tour = tour * -1
    VerifieVictoire()

# On définit à quel tour on est.
# 1 = cercles
# -1 = croix
global tour
tour = 1

FENETRE.bind("<Button-1>", click)

FENETRE.mainloop()
    
