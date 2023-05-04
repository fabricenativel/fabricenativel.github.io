import turtle
import grille


# Constantes
LARGEUR_ECRAN=1000
HAUTEUR_ECRAN=600
C_FOND = "lightgray"
C_BORD = "darkblue"
E_BORD = 8
LIG_TITRE = HAUTEUR_ECRAN//2 - 8*E_BORD
FONTE_TITRE = ("Arial",24,"bold")
FONTE_MOT = ("Arial",16,"bold")
E_POTENCE = 5
C_POTENCE = "brown"
E_CORDE = 3
C_CORDE = "black"
E_CORPS = 3
C_CORPS = "darkred"
C_MOT = "darkgreen"
E_CADRE = 2
C_CADRE = "black"
C_LETTRE = "blue"
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
VOYELLES = "AEIOUY"
LIGNE_MOT = - 250
LIG_ALPHABET = -200
F_CADRE = "white"
FICHIERS_MOTS = ["faciles.txt","moyens.txt","difficiles.txt"]
NIVEAU = ["Facile","Moyen","Difficile"]
C_NIVEAU = ["green","orange","red"]
level = None
OK = "A"
POK = "G"

papier = turtle.Screen()
crayon = turtle.Turtle()


crayon.pensize(5)
crayon.color("black")
crayon.fillcolor("gray")
crayon.penup()
crayon.goto(-100,-200)
crayon.pendown()
crayon.begin_fill()
for _ in range(2):
    crayon.forward(200)
    crayon.left(90)
    crayon.forward(400)
    crayon.left(90)
start=[-175,-50,75]
cstart=["green","orangered","darkred"]
bstart=["lightgreen","orange","red"]
for i in range(3):
    crayon.end_fill()
    crayon.color(cstart[i])
    crayon.fillcolor(bstart[i])
    crayon.begin_fill()
    crayon.penup()
    crayon.goto(0,start[i])
    crayon.pendown()
    crayon.circle(50)
    crayon.end_fill()

#a.trace()
papier.update()
grille.set_crayon(grille.Axe.tortue_axe,couleur="darkgray")
grille.set_crayon(grille.Graduation.tortue_graduation,couleur="darkgray")
grille.set_crayon(grille.Pattern.tortue_pattern,couleur="darkgray")
p = grille.Pattern(20,(' ','-'),(90,10))
g = grille.Grille(50,p,50,p)
g.trace()

a = grille.Axe()
a.trace()
papier.update()

grad = grille.Graduation(50,20,label=("Arial",14,"normal"))
grad.affiche()
grad2 =grille.Graduation(10,5,sub=5,show_label=False)
grad2.affiche()


def init(mot):
    crayon.setheading(0)
    start = -50 * (len(mot)//2)
    grille.set_crayon(crayon,epaisseur=E_CADRE,couleur=C_CADRE,remplissage=F_CADRE)
    for k in range(len(mot)):
        grille.rectangle(crayon,start+k*50,LIGNE_MOT,40,40)    
    for ind in range(len(ALPHABET)):
        if ALPHABET[ind] in VOYELLES:
            crayon.color("darkred")
        else:
            crayon.color("navy")
        grille.ecrit(crayon,-300+25*ind,LIG_ALPHABET,ALPHABET[ind],FONTE_MOT)
    papier.update()


papier.update()
papier.exitonclick()
