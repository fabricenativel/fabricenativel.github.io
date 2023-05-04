import turtle
import grille



papier = turtle.Screen()
crayon = turtle.Turtle()

papier.setup(height=1000,width=1000)
crayon.pensize(2)

def carre(c):
    for _ in range(4):
        crayon.forward(c)
        crayon.left(90)

def spirale(taille):
    while taille>1:
        carre(taille)
        crayon.left(10)
        taille = taille*0.9
        crayon.forward(10)

spirale(200)



crayon.hideturtle()

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
papier.update()

grad = grille.Graduation(50,20,label=("Arial",14,"normal"))
grad.affiche()
grad2 =grille.Graduation(10,5,sub=5,show_label=False)
grad2.affiche()


def init(mot):
    crayon.setheading(0)
    start = -50 * (len(mot)//2)
    grille.set_crayon(crayon,epaisseur=E_CADRE,couleur=C_CADRE,remplissage=F_CADRE)
    for k in range(len(mot)):
        grille.rectangle(crayon,start+k*50,LIGNE_MOT,40,40)    
    for ind in range(len(ALPHABET)):
        if ALPHABET[ind] in VOYELLES:
            crayon.color("darkred")
        else:
            crayon.color("navy")
        grille.ecrit(crayon,-300+25*ind,LIG_ALPHABET,ALPHABET[ind],FONTE_MOT)
    papier.update()

papier.update()
papier.exitonclick()
