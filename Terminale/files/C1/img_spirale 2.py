import turtle
import grille

papier = turtle.Screen()
crayon = turtle.Turtle()
papier.setup(width=500,height=500)





papier.bgcolor("white")
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
#grad.affiche()
#grad2.affiche()
#g.trace()
#a.trace()
papier.title('Spirale')


grille.set_crayon(crayon,epaisseur=1,couleur="gray")

taille = 200
while taille>10:
    for _ in range(4):
        crayon.forward(taille)
        crayon.left(90)
    crayon.left(20)
    taille=taille*0.9

crayon.setheading(0)
taille=200
grille.set_crayon(crayon,epaisseur=3,couleur="black")
for _ in range(4):
        crayon.forward(taille)
        crayon.left(90)
    
papier.update()
filename = input("Entrer le nom du fichier de sauvegarde : ")
papier.getcanvas().postscript(file=filename)
