import turtle
import grille

papier = turtle.Screen()
crayon = turtle.Turtle()
papier.setup(height=400,width=400)
crayon.pensize(3)
crayon.hideturtle()

def origine(x,y):
    crayon.penup()
    crayon.goto(x,y)
    crayon.pendown()

def carre_rempli(cote,couleur):
    crayon.fillcolor(couleur)
    crayon.begin_fill()
    crayon.forward(cote)
    crayon.left(90)
    crayon.forward(cote)
    crayon.left(90)
    crayon.forward(cote)
    crayon.left(90)
    crayon.forward(cote)
    crayon.left(90)
    crayon.end_fill()

def ligne_carres(n,cote,couleur,m):
    for k in range(n):
        if k+1 == m:
            carre_rempli(cote,"white")
        else:
            carre_rempli(cote,couleur)
        crayon.forward(cote)

def grand_carre(n,cote):
    for k in range(n):
        ligne_carres(n,cote,"lightgray",k+1)
        crayon.backward(n*cote)
        crayon.setheading(90)
        crayon.forward(cote)
        crayon.setheading(0)


crayon.setheading(45)
ligne_carres(5,20,"gray",0)

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
