"""
pendu.py

Le code complet du jeu du pendu, avec identification des parties
réalisées dans chacune des activités.

"""

# -------------------------------------------
# Activité 1 -- Notebook découverte de turtle
# -------------------------------------------

# --- Importer le module 

import turtle

# --- Créer la feuille et le crayon

feuille = turtle.Screen()
crayon = turtle.Turtle()
feuille.bgcolor('beige')

# --- Dessiner les deux premières barres de la potence

# crayon.color('red')
# crayon.pensize(5)

# crayon.penup()
# crayon.goto(-200,-150)
# crayon.pendown()
# crayon.goto(-100,-150)

# crayon.penup()
# crayon.goto(-150,-150)
# crayon.pendown()
# crayon.goto(-150,200)

# --- Dessiner les deux dernières barres de la potence (Exercice 1)

# crayon.goto(50,200)
# crayon.penup()
# crayon.goto(-150,150)
# crayon.pendown()
# crayon.goto(-100,200)

# --- Dessiner la corde (Exercice 2)

# crayon.color('black')
# crayon.pensize(3)
# crayon.penup()
# crayon.goto(0,200)
# crayon.pendown()
# crayon.goto(0,150)

# --- Dessiner la tête du pendu

# crayon.setheading(180)
# crayon.circle(25)


# -----------------------------------------------
# Activité 2 -- Notebook découverte des fonctions
# -----------------------------------------------

# On reprend une partie du code de l'activité 1
# sous forme de fonctions -- certaines probablement à faire en exercice

def ligne(x1,y1,x2,y2):
    crayon.penup()
    crayon.goto(x1,y1)
    crayon.pendown()
    crayon.goto(x2,y2)

def pendu_1():
    """Les 2 premières barres de la potence"""
    ligne(-200,-150,-100,-150)
    ligne(-150,-150,-150,200)

# --- Exercice 1 (les instructions, pas la fonction pendu_2)

def pendu_2():
    """Les 2 dernières barres de la potence et la corde"""
    ligne(-150, 150, -100, 200)
    ligne(-150, 200, 50, 200)    
    crayon.color('black')
    crayon.pensize(3)
    ligne(0, 200, 0, 150)

# --- Exercice 2 

def pendu_3():
    """La corde et la tête"""
    crayon.color('black')
    crayon.pensize(3)
    crayon.setheading(180)
    crayon.circle(25)

# --- Exercice 3 

def pendu_4():
    """Le corps"""
    ligne(0, 100, 0, 0)

def pendu_5():
    """Les 2 bras"""
    ligne(0, 80, -50, 50)
    ligne(0, 80, 50, 50)

def pendu_6():
    """Les 2 jambes"""
    ligne(0, 0, -50, -75)
    ligne(0, 0, 50, -75)



