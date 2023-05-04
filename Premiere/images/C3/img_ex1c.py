import turtle
import grille

papier = turtle.Screen()
crayon = turtle.Turtle()
papier.setup(width=450,height=450)



def ligneoe(x1,y1,x2,y2):
    crayon.penup()
    crayon.goto(x1,y1)
    crayon.pendown()
    crayon.goto(x2,y2)

def ligneoal(x1,y1,a,l):
    crayon.penup()
    crayon.goto(x1,y1)
    crayon.pendown()
    crayon.setheading(a)
    crayon.forward(l)

def cercle(x,y,r):
    crayon.penup()
    crayon.goto(x,y-r)
    crayon.setheading(0)
    crayon.pendown()
    crayon.circle(r)



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


grad = grille.Graduation(50,20,label=("Arial",14,"normal"))
grad.affiche()
grad2 =grille.Graduation(10,5,sub=5,show_label=False)
grad2.affiche()


papier.title("Cercles")
crayon.pensize(5)
crayon.color("navy")
ligneoe(0,-100,0,0)
cercle(0,100,100)
cercle(0,100,25)
    

papier.update()

papier.exitonclick()