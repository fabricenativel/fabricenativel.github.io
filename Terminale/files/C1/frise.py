import turtle
import grille

papier = turtle.Screen()
crayon = turtle.Turtle()
papier.setup(width=800,height=350)





papier.bgcolor("beige")
crayon.pensize(5)
crayon.color("navy")
#a.trace()
papier.update()
grille.set_crayon(grille.Axe.tortue_axe,couleur="darkgray")
grille.set_crayon(grille.Graduation.tortue_graduation,couleur="darkgray")
grille.set_crayon(grille.Pattern.tortue_pattern,couleur="darkgray")
p = grille.Pattern(20,(' ','-'),(90,10))
g = grille.Grille(50,p,50,p)


a = grille.Axe()



grad = grille.Graduation(50,20,label=("Arial",14,"normal"))

grad2 =grille.Graduation(10,5,sub=5,show_label=False)
grad.affiche()
grad2.affiche()
g.trace()
a.trace()
papier.title('Frise')




def motif(longueur):
    crayon.forward(longueur)
    crayon.left(90)
    crayon.forward(longueur)
    crayon.right(90)
    crayon.forward(longueur)
    crayon.right(90)
    crayon.forward(longueur)
    crayon.left(90)

def frise(nb,longueur):
    if nb>0:
        motif(longueur)
        frise(nb-1,longueur)
crayon.penup()
crayon.goto(-350,0)
crayon.pendown()
frise(7,50)


papier.update()
papier.exitonclick()
