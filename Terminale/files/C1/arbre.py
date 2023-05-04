import turtle
from math import sqrt

crayon = turtle.Turtle()
papier = turtle.Screen()
papier.tracer(30)
crayon.hideturtle()

def carre_trace(c):
    # Trace un carré et renvoie la position des sommets 3 et 4
    a=crayon.heading()
    for s in range(4):
        crayon.forward(c)
        crayon.left(90)
        if s==1:
            s2x,s2y=crayon.pos()
            a2 = crayon.heading()
        if s==2:
            s3x,s3y=crayon.pos()
            a3=crayon.heading()
    return s2x,s2y,s3x,s3y,a

def arbre(level,cote):
    if level==1:
        return carre_trace(cote)
    else:
        s2x,s2y,s3x,s3y,a = carre_trace(cote)
        crayon.setheading(a+45)
        crayon.penup()
        crayon.goto(s3x,s3y)
        crayon.pendown()
        arbre(level-1,cote*sqrt(2)/2)
        crayon.penup()
        crayon.goto(s2x,s2y)
        crayon.setheading(a+45)
        crayon.left(90)
        crayon.forward(cote*sqrt(2)/2)
        crayon.setheading(a-45)
        crayon.pendown()
        arbre(level-1,cote*sqrt(2)/2)
        
crayon.penup()
crayon.goto(-200,-350)
crayon.pendown()
arbre(13,200)
papier.update()
papier.exitonclick()