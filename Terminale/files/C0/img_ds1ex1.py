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



papier.title('Exemple rectangle plein')


grille.set_crayon(crayon,epaisseur=1,couleur="navy",remplissage="navy")

grille.rectangle(crayon,-100,-100,80,120)

g.trace()

a = grille.Axe()
a.trace()


grad = grille.Graduation(50,20,label=("Arial",14,"normal"))
grad.affiche()
grad2 =grille.Graduation(10,5,sub=5,show_label=False)
grad2.affiche()
papier.update()
filename = input("Entrer le nom du fichier de sauvegarde : ")
papier.getcanvas().postscript(file=filename)
