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



papier.title('Cercles')


grille.set_crayon(crayon,epaisseur=4,couleur="navy",remplissage="white")

rayon=5
for x in range(-200,200,50):
    grille.origine(crayon,x,0)
    if rayon==25:
        crayon.color("red")
    else:
        crayon.color("navy")
    crayon.circle(rayon)
    rayon=rayon+5


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
