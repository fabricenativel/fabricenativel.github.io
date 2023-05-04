import turtle

papier = turtle.Screen()
crayon = turtle.Turtle()

papier.bgcolor('beige')

crayon.color("navy")

def carre(c):
    for _ in range(4):
        crayon.forward(c)
        crayon.left(90)

cote = 200
while cote>5:
     carre(cote)
     cote = cote * 0.9

papier.exitonclick()
