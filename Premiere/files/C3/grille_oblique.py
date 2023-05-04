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

papier.setup(height=400,width=500)

def ligne(x1,y1,x2,y2):
    crayon.penup()
    crayon.goto(x1,y1)
    crayon.pendown()
    crayon.goto(x2,y2)

def carre(x,y,c):
    crayon.penup()
    crayon.goto(x,y)
    crayon.pendown()
    for _ in range(4):
        crayon.forward(c)
        crayon.left(90)

crayon.color("darkgreen")
crayon.pensize(3)
for x in range(-200,200,50):
    ligne(x,-150,x+100,150)
crayon.hideturtle()

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
