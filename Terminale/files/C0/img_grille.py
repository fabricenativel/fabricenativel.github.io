import turtle
import grille

papier = turtle.Screen()
crayon = turtle.Turtle()
papier.setup(width=500,height=500)






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

papier.bgcolor('beige')
papier.title('Grille')


grille.set_crayon(crayon,epaisseur=5,couleur="navy")

for l in range(-200,250,50):
    grille.ligne_bis(crayon,-200,l,200,l)
    grille.ligne_bis(crayon,l,-200,l,200)




papier.update()
filename = input("Entrer le nom du fichier de sauvegarde : ")
papier.getcanvas().postscript(file=filename)
