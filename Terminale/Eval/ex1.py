import turtle
import grille 
# Création du "papier" et du "crayon"
crayon = turtle.Turtle()
papier = turtle.Screen()
papier.setup(width=500,height=500)


def rectangle(x,y,longueur,largeur):
    crayon.penup()
    crayon.goto(x,y)
    crayon.pendown()
    for _ in range(2):
        crayon.forward(longueur)
        crayon.left(90)
        crayon.forward(largeur)
        crayon.left(90)

#a.trace()
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

crayon.hideturtle()
for i in range(1,9):
    rectangle(-200+i*50,0,20,i*25)
    if i == 4:
        crayon.color("darkred")
    else:
        crayon.color("navy")

papier.update()
# Attends un clic pour fermer la fenêtre de dessin
papier.exitonclick()