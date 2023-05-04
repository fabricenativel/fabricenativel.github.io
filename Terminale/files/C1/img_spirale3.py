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
'''grad.affiche()
grad2.affiche()
g.trace()
a.trace()'''
papier.title('carres imbriques')


grille.set_crayon(crayon,epaisseur=1,couleur="gray")

def carre(c):
    crayon.penup()
    crayon.setheading(90)
    crayon.forward(taille/2)
    crayon.setheading(0)
    crayon.forward(taille/2)
    crayon.pendown()
    crayon.setheading(180)
    for _ in range(4):
        crayon.forward(taille)
        crayon.left(90)
    crayon.penup()
    crayon.setheading(270)
    crayon.forward(taille/2)
    crayon.setheading(180)
    crayon.forward(taille/2)
    crayon.pendown()

taille = 200
while taille>=10:
    carre(taille)
    taille=taille-20


    
papier.update()
filename = input("Entrer le nom du fichier de sauvegarde : ")
papier.getcanvas().postscript(file=filename)
