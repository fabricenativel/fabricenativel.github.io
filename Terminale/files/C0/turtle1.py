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

# Attends un clic pour fermer la fenêtre de dessin
papier.exitonclick()