import turtle
import grille

papier = turtle.Screen()
crayon = turtle.Turtle()
papier.setup(width=400,height=300)






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


papier.title('QCM')


grille.set_crayon(crayon,epaisseur=5,couleur="navy")



crayon.setheading(270)
crayon.forward(100)
crayon.left(90)
crayon.forward(50)

papier.update()

papier.exitonclick()