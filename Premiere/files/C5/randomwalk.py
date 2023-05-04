import turtle
# randint(a,b) permet de tirer un nombre au sort entre a et b
from random import randint
tortue = turtle.Turtle()
papier = turtle.Screen()

# On fixe les dimensions de la feuille de papier
papier.setup(height=450,width=450)
# vitesse et forme de la souris
tortue.speed(0)
tortue.shape("turtle")

def cercle(rayon):
    tortue.pensize(2)
    tortue.color("red")
    tortue.penup()
    tortue.goto(rayon,0)
    tortue.pendown()
    tortue.setheading(90)
    tortue.circle(rayon)
    tortue.pensize(1)
    tortue.color("black")

def dans_cercle(rayon):
    x = tortue.xcor()
    y = tortue.ycor()
    if x**2+y**2 <= rayon**2:
        return True
    else:
        return False

def pas():
    direction = randint(1,4)
    if direction==1:
        tortue.setheading(0)
    elif direction==2:
        tortue.setheading(90)
    elif direction==3:
        tortue.setheading(180)
    else:
        tortue.setheading(270)
    tortue.forward(10)

cercle(200)
tortue.penup()
tortue.goto(0,0)
tortue.pendown()
while dans_cercle(200):
    pas()


papier.exitonclick()