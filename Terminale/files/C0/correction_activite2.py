import turtle

# Création du "papier" et du "crayon"
crayon = turtle.Turtle()
papier = turtle.Screen()

# Taille, dimension et couleur pour le papier et le crayon
papier.bgcolor("beige")
papier.setup(width=500,height=500)
crayon.color("navy")
crayon.pensize(5)

# Tracé d'un trait avec les coordonnées des extrémités
crayon.penup()
crayon.goto(-50,-150)
crayon.pendown()
crayon.goto(-50,150)

# Tracé d'un trait en orientant et en faisant avancer la tortue
crayon.penup()
crayon.goto(50,-150)
crayon.pendown()
crayon.setheading(90)
crayon.forward(300)

# Correction question 2 : tracé des traits manquants
crayon.penup()
crayon.goto(-150,-50)
crayon.pendown()
crayon.goto(150,-50)
crayon.penup()
crayon.goto(-150,50)
crayon.pendown()
crayon.goto(150,50)

# Correction question 3 : tracé du cercle
crayon.color("darkred")
crayon.pensize(7)
crayon.penup()
crayon.goto(40,0)
crayon.pendown()
crayon.setheading(90)
crayon.circle(40)


# Attends un clic pour fermer la fenêtre de dessin
papier.exitonclick()