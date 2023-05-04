import turtle             

## Constantes pour la taille des disques, les espaces entres les tours etc ...
HAUTEUR_BASE = 25
LARGEUR_BASE = 250
COULEUR_BASE = "black"
HAUTEUR_TOUR = 300
HAUTEUR_DISQUE = 30
LARGEUR_TOUR = 20
COULEUR_TOUR="#333333"
LARGEUR_DISQUE_MIN = 50
VARIATION_TAILLE_DISQUE = 25
ESPACE_TOUR = 50
MARGE=40
LARGEUR_FENETRE=LARGEUR_BASE*3+ESPACE_TOUR*2+MARGE*2
HAUTEUR_FENETRE=HAUTEUR_TOUR+MARGE*2
ORIGINE_X = -LARGEUR_FENETRE/2+MARGE
ORIGINE_Y = -HAUTEUR_FENETRE/2+MARGE
COULEURS_DISQUES=['lightgreen','limegreen','yellow','gold','orangered2','red3','purple3','brown']


#Positionne la tortue en (x,y)
def origine(tortue,x,y):
    tortue.penup()
    tortue.goto((x,y))
    tortue.pendown()


#Trace un rectangle à partir de la position courante de la tortue
def rectangle(tortue,longueur,largeur,couleur='white'):
    tortue.fillcolor(couleur)
    tortue.begin_fill()
    for _ in range(2):
        tortue.forward(longueur)
        tortue.left(90)
        tortue.forward(largeur)
        tortue.left(90)
    tortue.end_fill()   

#Dessine la tour de numéro num
def dessine_tour(tortue,num,color=COULEUR_TOUR):
        origine(tortue,ORIGINE_X+num*(LARGEUR_BASE+ESPACE_TOUR),ORIGINE_Y)
        rectangle(tortue,LARGEUR_BASE,HAUTEUR_BASE,COULEUR_BASE)
        tortue.forward(LARGEUR_BASE/2-LARGEUR_TOUR/2)
        rectangle(tortue,LARGEUR_TOUR,HAUTEUR_TOUR,color)

#Dessine les tours
def dessine_tours(tortue):
    for i in range(3):
        dessine_tour(tortue,i)
        

#dessine le disque de largeur taille à la hauteur indiqué sur la tour
def dessine_disque(tortue,hauteur,taille,tour):
    origine(tortue,ORIGINE_X+tour*(LARGEUR_BASE+ESPACE_TOUR)+(LARGEUR_BASE-LARGEUR_DISQUE_MIN-taille*VARIATION_TAILLE_DISQUE)/2,ORIGINE_Y+HAUTEUR_BASE+HAUTEUR_DISQUE*hauteur)
    rectangle(tortue,LARGEUR_DISQUE_MIN+taille*VARIATION_TAILLE_DISQUE,HAUTEUR_DISQUE,COULEURS_DISQUES[taille])



#Dessine l'état de départ du jeu pour le nombre de disque passé en paramètre
#Utilisation de variables globales de façon à ce que les appels à cette fonction se fasse de façon transparente pour les él_ves
def dessine_depart(nb):
    assert type(nb) is int, "La variable doit être de type entier"
    assert 8>=nb>=1, "Le nombre de disque doit être compris entre 1 et 8 (inclus)"
    ## Création de variable globales necessaires au dessin du  jeu : la fenêtre et les tortues
    global fenetre,caroline,tortues_disques, etat, nb_disque
    nb_disque=nb
    fenetre = turtle.Screen()
    fenetre.setup(width=LARGEUR_FENETRE,height=HAUTEUR_FENETRE)
    fenetre.tracer(1)
    caroline=turtle.Turtle()
    caroline.speed(0)
    caroline.hideturtle()
    dessine_tours(caroline)
    # etat du jeu (un triplet contenant 3 listes qui représente les disques sur chacune des tours)
    etat = ([nb_disque-i for i in range(nb_disque)],[],[])
    # Création d'une tortue par disque (pour effacement)
    tortues_disques=[turtle.Turtle() for _ in range(nb_disque)]
    for tortue in tortues_disques:
        tortue.speed(0)
        tortue.hideturtle()
    for d in range(nb_disque):
        dessine_disque(tortues_disques[d],nb_disque-d-1,d,0)
    
#Deplace un disque d'une tour de départ vers une tour d'arrivée
def deplace_disque(depart,arrive):
    valide=True
    arrive=arrive-1
    depart=depart-1
    # Tester si le mouvement est valide (départ non vide, arrivée vide ou avec un disque plus grande):
    if etat[depart]==[]:
        valide=False
        message="** Erreur : La TOUR de départ est vide"
    elif etat[arrive]!=[] and etat[arrive][-1]<etat[depart][-1]:
        valide=False
        message="** Erreur : On ne peut pas déplacer un disque sur un disque plus petit"
    if valide:
        disque=etat[depart].pop()-1
        tortues_disques[disque].clear()
        etat[arrive].append(disque+1)
        dessine_disque(tortues_disques[disque],len(etat[arrive])-1,disque,arrive)
        message=">> Ok : déplacement du disque "+str(disque+1)+" de "+str(depart+1)+" à "+str(arrive+1)
    return message

def resolu(nd_disque):
    return len(etat[2])==nb_disque

def fin():
    origine(caroline,0,-HAUTEUR_FENETRE/2+MARGE/2)
    caroline.color("red")
    caroline.write("Cliquer pour terminer",align="center",font=("arial",14,"normal"))
    fenetre.exitonclick()

def solution_hanoi(nbd,depart,arrivee):
    tours=[1,2,3]
    tours.remove(depart)
    tours.remove(arrivee)
    intermediaire=tours[0]
    if nbd==1:
        deplace_disque(depart,arrivee)
    else:
        solution_hanoi(nbd-1,depart,intermediaire)
        deplace_disque(depart,arrivee)
        solution_hanoi(nbd-1,intermediaire,arrivee)
        
def solution_hanoi2(nbd,depart,intermediaire,arrivee):
    if nbd>0:
        solution_hanoi2(nbd-1,depart,arrivee,intermediaire)
        deplace_disque(depart,arrivee)
        solution_hanoi2(nbd-1,intermediaire,depart,arrivee)

def sol(nb_disque,dep,inter,arr):
    if nb_disque>1:
        sol(nb_disque-1,dep,arr,inter)
        deplace_disque(dep,arr)
        sol(nb_disque-1,inter,dep,arr)
    else:
        deplace_disque(dep,arr)

