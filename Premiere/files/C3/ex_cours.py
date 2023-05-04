import turtle

crayon=turtle.Turtle()
papier=turtle.Screen()
crayon.color('navy')
papier.bgcolor('beige')
crayon.pensize(2)
crayon.setheading(0)

def trait(x,y,l,a):
    crayon.penup()
    crayon.goto(x,y)
    crayon.setheading(a)
    crayon.pendown()
    crayon.forward(l)

direction = 0
longueur = 10
for t in range(26):
    trait(0,0,longueur,direction)
    direction+=7.2
    longueur+=5
papier.exitonclick()