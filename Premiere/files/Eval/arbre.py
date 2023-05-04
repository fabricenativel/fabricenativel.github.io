import turtle
import grille

papier = turtle.Screen()
crayon = turtle.Turtle()
papier.setup(height=400,width=400)
crayon.pensize(1)
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

def tronc(larg,hauteur,couleur):
    crayon.fillcolor(couleur)
    crayon.begin_fill()
    crayon.forward(larg)
    crayon.left(90)
    crayon.forward(hauteur)
    crayon.left(90)
    crayon.forward(larg)
    crayon.left(90)
    crayon.forward(hauteur)
    crayon.left(90)
    crayon.end_fill()

def feuillage(rayon,couleur):
    crayon.fillcolor(couleur)
    crayon.begin_fill()
    crayon.circle(rayon)
    crayon.end_fill()

def arbre(larg,hauteur,rayon,ctronc,cfeuillage):
    tronc(larg,hauteur,ctronc)
    crayon.penup()
    crayon.forward(larg//2)
    crayon.setheading(90)
    crayon.forward(2*hauteur//3)
    crayon.setheading(0)
    feuillage(rayon,cfeuillage)

arbre(20,200,60,"brown","green")
origine(100,0)
arbre(30,150,50,"brown","green")
origine(-150,0)
arbre(50,150,90,"brown","green")


papier.update()
papier.exitonclick()
