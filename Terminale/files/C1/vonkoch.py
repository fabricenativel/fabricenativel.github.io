import turtle             

#Positionne la tortue en (x,y)
def origine(tortue,x,y):
    tortue.penup()
    tortue.goto((x,y))
    tortue.pendown()

def courbe_koch(tortue,longueur,ordre):
    if ordre==0:
        tortue.forward(longueur)
    else:
        ordre=ordre-1
        longueur=longueur//3
        courbe_koch(tortue,longueur,ordre)
        tortue.left(60)
        courbe_koch(tortue,longueur,ordre)
        tortue.right(120)
        courbe_koch(tortue,longueur,ordre)
        tortue.left(60)
        courbe_koch(tortue,longueur,ordre)

def flocon(tortue,longueur,profondeur):
    for _ in range(3):
        courbe_koch(tortue,longueur,profondeur)
        tortue.right(120)
        
#On crée une fenêtre et on fixe sa taille
fenetre = turtle.Screen()
fenetre.title("Courbe de Koch")
fenetre.setup(width=600,height=400)
#On crée une tortue (on l'appelle ... caroline)
caroline=turtle.Turtle()
caroline.speed(0)
#Pour dessiner il suffit maintenant de donner des instructions à la tortue : avancer, tourner, ...
origine(caroline,-250,-100)
courbe_koch(caroline,500,4)
#On termine le programme lorsqu'on click sur la fenetre
caroline.hideturtle()
fenetre.exitonclick()
