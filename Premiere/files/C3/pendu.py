#! /usr/bin/python3
import time
import random
import turtle



# La tortue et l'écran de jeu
papier = turtle.Screen()
crayon = turtle.Turtle()


# Constantes
LARGEUR_ECRAN=1000
HAUTEUR_ECRAN=600
C_FOND = "lightgray"
C_BORD = "darkblue"
E_BORD = 8
LIG_TITRE = HAUTEUR_ECRAN//2 - 8*E_BORD
FONTE_TITRE = ("Arial",24,"bold")
FONTE_MOT = ("Arial",16,"bold")
E_POTENCE = 5
C_POTENCE = "brown"
E_CORDE = 3
C_CORDE = "black"
E_CORPS = 3
C_CORPS = "darkred"
C_MOT = "darkgreen"
E_CADRE = 2
C_CADRE = "black"
C_LETTRE = "blue"
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LIGNE_MOT = - 250
LIG_ALPHABET = -200
F_CADRE = "white"
FICHIERS_MOTS = ["faciles.txt","moyens.txt","difficiles.txt"]
NIVEAU = ["Facile","Moyen","Difficile"]
C_NIVEAU = ["green","orange","red"]
level = None
OK = "A"
POK = "G"


# Taille et couleur du papier + coordonnées
papier.bgcolor(C_FOND)
papier.setup(width=LARGEUR_ECRAN,height=HAUTEUR_ECRAN)


# Accélération des dessins
crayon.speed(0)
papier.tracer(400)

def origine(tortue,x,y):
    tortue.penup()
    tortue.goto(x,y)
    tortue.pendown()

def ecrit(tortue,x,y,texte,fonte):
    origine(tortue,x,y)
    tortue.write(texte,align="center",font=fonte)

def ligne(tortue,x,y,l,angle):
    '''Trace le segment de droite d'origne (x,y) et de longueur l dans la direction angle'''
    origine(tortue,x,y)
    tortue.setheading(angle)
    tortue.forward(l)

def ligne_bis(tortue,x1,y1,x2,y2):
    origine(tortue,x1,y1)
    tortue.goto(x2,y2)

def rectangle(tortue,x,y,lx,ly):
    origine(tortue,x,y)
    tortue.begin_fill()
    for _ in range(2):
        tortue.forward(lx)
        tortue.left(90)
        tortue.forward(ly)
        tortue.left(90)
    tortue.end_fill()

def cercle(tortue,x,y,r,angle=360):
    origine(tortue,x+r,y)
    tortue.setheading(90)
    tortue.pendown()
    tortue.begin_fill()
    tortue.circle(r)
    tortue.end_fill()


def set_crayon(tortue,epaisseur=1,couleur="black",remplissage="white",visible=False):
    tortue.pensize(epaisseur)
    tortue.color(couleur)
    tortue.fillcolor(remplissage)
    if visible:
        tortue.showturtle()
    else:
        tortue.hideturtle()

def start_dessin():
    set_crayon(crayon,epaisseur=E_BORD,couleur=C_BORD,remplissage=C_FOND)
    rectangle(crayon,-LARGEUR_ECRAN//2+E_BORD*2,-HAUTEUR_ECRAN//2+E_BORD*2,LARGEUR_ECRAN-4*E_BORD,HAUTEUR_ECRAN-4*E_BORD)
    ecrit(crayon,0, LIG_TITRE,"Jeu du pendu",fonte=FONTE_TITRE)
    set_crayon(crayon,couleur=C_LETTRE)
    for ind in range(len(ALPHABET)):
        ecrit(crayon,-300+25*ind,LIG_ALPHABET,ALPHABET[ind],FONTE_MOT)

def barre_lettre(lettre):
    col = ALPHABET.index(lettre)
    set_crayon(crayon,epaisseur=E_CORDE,couleur="black")
    ligne(crayon,-300+25*col-10,LIG_ALPHABET+5,25,45)

def init(mot):
    start = -50 * (len(mot)//2)
    set_crayon(crayon,epaisseur=E_CADRE,couleur=C_CADRE,remplissage=F_CADRE)
    for k in range(len(mot)):
        rectangle(crayon,start+k*50-16,LIGNE_MOT-10,30,40)    
    papier.update()

def show_grid():
    p = grille.Pattern(20,(' ','-'),(90,10))
    #a.trace()
    g = grille.Grille(50,p,50,p)
    g.trace()
    a = grille.Axe()
    a.trace()
    grad = grille.Graduation(50,20)
    grad.affiche()
    grad2 =grille.Graduation(10,5,sub=5,show_label=False)
    grad2.affiche()
    papier.update()

def potence1():
    set_crayon(crayon,epaisseur=E_POTENCE,couleur=C_POTENCE)
    ligne(crayon,-200,-150,100,0)
    ligne(crayon,-150,-150,350,90)

def potence2():
    set_crayon(crayon,epaisseur=E_POTENCE,couleur=C_POTENCE)
    ligne(crayon,-150,200,200,0)
    ligne_bis(crayon,-150,150,-100,200)
    
def corde():
    set_crayon(crayon,epaisseur=E_CORDE,couleur=C_CORDE)
    ligne(crayon,0,200,50,270)

def tete():
    set_crayon(crayon,epaisseur=E_CORPS,couleur=C_CORPS)
    cercle(crayon,0,125,25)

def tronc():
    set_crayon(crayon,epaisseur=E_CORPS,couleur=C_CORPS)
    ligne(crayon,0,100,100,270)

def bras():
    set_crayon(crayon,epaisseur=E_CORPS,couleur=C_CORPS)
    ligne(crayon,0,90,50,310)
    ligne(crayon,0,90,50,230)

def jambes():
    set_crayon(crayon,epaisseur=E_CORPS,couleur=C_CORPS)
    ligne(crayon,0,0,70,300)
    ligne(crayon,0,0,70,240)

def bouche():
    set_crayon(crayon,epaisseur=E_CORPS,couleur=C_CORPS)
    ligne(crayon,-5,115,10,0)

def yeux():
    set_crayon(crayon,epaisseur=2,couleur=C_CORPS)
    ligne(crayon,-12,130,14,45)
    ligne(crayon,-12,140,14,-45)
    ligne(crayon,8,130,14,45)
    ligne(crayon,8,140,14,-45)


def valide(proposition,deja_propose):
    if proposition is None or proposition=="": return False
    if len(proposition)==1:
        return type(proposition) is str and proposition in ALPHABET and proposition not in deja_propose
    else:
        return type(proposition) is str and all(l in ALPHABET for l in proposition)

def ecrit_lettre(mot,lettre):
    set_crayon(crayon,couleur=C_MOT)
    start = -50 * (len(mot)//2)
    for l in mot:
        if l==lettre:
            ecrit(crayon,start,LIGNE_MOT,l,FONTE_MOT)
        start = start + 50

def dessine(nb_erreurs):
    parties = { 1 : potence1, 2:potence2, 3:corde, 4:tete, 5:tronc, 6:bras, 7:jambes, 8:bouche, 9:yeux}
    if nb_erreurs!=0:
        parties[nb_erreurs]()
        papier.update()


def lecture_mots():
    mots = []
    for f in FICHIERS_MOTS:
        liste_mot=[]
        with open("/home/fenarius/Travail/ippt/Jeux/Pendu/"+f,"r",encoding="utf-8") as fic_mot:
            for mot in fic_mot:
                liste_mot.append(mot[:-1])
        mots.append(liste_mot)
    return mots

def choix_mot(lmots,niveau):
    return random.choice(lmots[niveau])


def options(mot,niveau):
    nb_erreurs = 9 - niveau
    if niveau==0:
        lettres = mot[0]+mot[-1]
    elif niveau==1:
        lettres = mot[0]
    else:
        lettres = ""
    return lettres,nb_erreurs

def get_level(x,y):
    global level
    yl = -1
    if LIG_TITRE-120<= y <= LIG_TITRE-80:
        yl = 0
    if LIG_TITRE-170<= y <= LIG_TITRE-130:
        yl = 1   
    if LIG_TITRE-220<= y <= LIG_TITRE-180:
        yl = 2    
    if  0<=yl<=2:
        papier.onscreenclick(None)
        level = yl

def get_niveau():
    global level
    lc,hc = 150,20
    t_niv = turtle.Turtle()
    ecrit(t_niv,0,LIG_TITRE-50,"Choisir le niveau",FONTE_MOT)
    for l in range(len(NIVEAU)):
        set_crayon(t_niv,couleur="black")
        rectangle(t_niv,-lc,LIG_TITRE-100-50*l-hc,lc*2,hc*2)
        set_crayon(t_niv,couleur=C_NIVEAU[l])
        ecrit(t_niv,0,LIG_TITRE-100-50*l-12,NIVEAU[l],FONTE_MOT)
    # Attente sélection
    papier.onscreenclick(get_level)
    while level is None:
        set_crayon(t_niv,couleur="red")
        ecrit(t_niv,0,LIG_TITRE-50,"Choisir le niveau",FONTE_MOT)
        time.sleep(0.2)
        set_crayon(t_niv,couleur="black")
        ecrit(t_niv,0,LIG_TITRE-50,"Choisir le niveau",FONTE_MOT)
        time.sleep(0.3)
    t_niv.reset()
    t_niv.hideturtle()

def voir_mot(mot):
    for lettre in mot:
        ecrit_lettre(mot,lettre)

# Lecture des fichiers de mots
lmots = lecture_mots()
end_game = False
# Demarrage partie
while not end_game:
    start_dessin()
    if level is None: get_niveau()
    mot = choix_mot(lmots,level)
    init(mot)
    lettres,erreur_max = options(mot,level)
    nb_erreurs = 0
    mot_trouve = False
    for l in lettres:
        ecrit_lettre(mot,l)
        barre_lettre(l)
    papier.update()
    #show_grid()
    while nb_erreurs<erreur_max and not mot_trouve:
        dessine(nb_erreurs)
        proposition_valide = False
        while not proposition_valide:
            proposition = papier.textinput("Proposition","Proposer une lettre ou le mot")
            proposition_valide = valide(proposition,lettres)
        if len(proposition)==1:
            barre_lettre(proposition)
            lettres = lettres + proposition
            if proposition in mot:
                ecrit_lettre(mot,proposition)
                # Détection mot trouvé
                mot_trouve = all(l in lettres for l in mot)
            else:
                nb_erreurs+=1
        else:
            if proposition==mot:
                mot_trouve=True
            else:
                nb_erreurs+=1
    dessine(nb_erreurs)
    voir_mot(mot)
    set_crayon(crayon,couleur=C_BORD)
    if mot_trouve: 
        ecrit(crayon,0,LIGNE_MOT+100,"Bravo !",FONTE_TITRE)
    else:
        ecrit(crayon,0,LIGNE_MOT+100,"Perdu !",FONTE_TITRE)
    rep = papier.textinput("Nouvelle partie","Rejouer une partie ?")
    if rep=='N': end_game=True
    crayon.reset()
papier.update()
papier.exitonclick()

