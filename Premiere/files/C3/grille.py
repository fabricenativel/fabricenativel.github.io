import turtle

def origine(tortue,x,y):
    tortue.penup()
    tortue.goto(x,y)
    tortue.pendown()

def ecrit(tortue,x,y,texte,fonte,alig="center"):
    origine(tortue,x,y)
    tortue.write(texte,font=fonte,align=alig)

def ligne_bis(tortue,x1,y1,x2,y2):
    origine(tortue,x1,y1)
    tortue.goto(x2,y2)

def ligne(tortue,x,y,l,angle):
    '''Trace le segment de droite d'origne (x,y) et de longueur l dans la direction angle'''
    origine(tortue,x,y)
    tortue.setheading(angle)
    tortue.forward(l)

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

class Pattern:

    tortue_pattern = turtle.Turtle()
    tortue_pattern.hideturtle()
    tortue_pattern.speed(0)
    tortue_pattern.getscreen().tracer(400)

    def __init__(self,size,formes,longueur):
        self.size = size
        self.formes = formes
        self.longueur = longueur
        self.nb = len(formes)

    def dessine(self,ox,oy,l,a):
        origine(Pattern.tortue_pattern,ox,oy)
        Pattern.tortue_pattern.setheading(a)
        k = 0
        while l > k*self.size:
            for ind in range(self.nb):
                # '-' = Trait continu 
                if self.formes[ind]=='-':
                    Pattern.tortue_pattern.forward(self.size*self.longueur[ind]/100)
                # '.' = Dot
                if self.formes[ind]=='.':
                    Pattern.tortue_pattern.right(90)
                    Pattern.tortue_pattern.circle(self.size//2*self.longueur[ind]/100)
                    Pattern.tortue_pattern.left(90)
                    Pattern.tortue_pattern.penup()
                    Pattern.tortue_pattern.forward(self.size*self.longueur[ind]/100)
                    Pattern.tortue_pattern.pendown()
                # ' ' = Espaces
                if self.formes[ind]==" ":
                    Pattern.tortue_pattern.penup()
                    Pattern.tortue_pattern.forward(self.size*self.longueur[ind]/100)
                    Pattern.tortue_pattern.pendown()
            k=k+1

class Grille:

    def __init__(self,xgrad,xpattern,ygrad,ypattern):
        self.xgrad = xgrad
        self.ygrad = ygrad
        self.xpattern = xpattern
        self.ypattern = ypattern
    
    def trace(self):
        # Récupération taille du papier
        hauteur = turtle.window_height()
        largeur = turtle.window_width()
        for x in range(0,largeur//2,self.xgrad):
            self.ypattern.dessine(x,-hauteur//2,hauteur,90)
            self.ypattern.dessine(-x,-hauteur//2,hauteur,90)
        for y in range(0,hauteur//2,self.ygrad):
            self.ypattern.dessine(-largeur//2,y,largeur,0)
            self.ypattern.dessine(-largeur//2,-y,largeur,0)


class Graduation:

    tortue_graduation = turtle.Turtle()
    tortue_graduation.hideturtle()
    tortue_graduation.speed(0)
    tortue_graduation.getscreen().tracer(400)

    def __init__(self,pas,tick,sub=False,show_label=True,label=("Courier",10,"normal"),offset = 15):
        self.pas = pas
        self.tick = tick
        self.sub = sub
        self.show_label = show_label
        self.label = label
        self.offset = offset
    
    def affiche(self):
        # Récupération taille du papier
        hauteur = turtle.window_height()
        largeur = turtle.window_width()
        for x in range(self.pas,largeur//2,self.pas):
            if not self.sub or  (x//self.pas)%self.sub != 0:
                ligne(Graduation.tortue_graduation, x, -self.tick//2,self.tick,90)
                ligne(Graduation.tortue_graduation, -x, -self.tick//2,self.tick,90)
                if self.show_label:
                    ecrit(Graduation.tortue_graduation,x,-self.tick//2-self.offset,x,self.label)
                    ecrit(Graduation.tortue_graduation,-x,-self.tick//2-self.offset,-x,self.label)
        for y in range(self.pas,hauteur//2,self.pas):
            if not self.sub or  (y//self.pas)%self.sub != 0:
                ligne(Graduation.tortue_graduation, -self.tick//2, y,self.tick,0)
                ligne(Graduation.tortue_graduation, -self.tick//2, -y,self.tick,0)
                if self.show_label:
                    ecrit(Graduation.tortue_graduation,-self.tick//2-self.offset,y-self.label[1],y,self.label)
                    ecrit(Graduation.tortue_graduation,-self.tick//2-self.offset,-y-self.label[1],-y,self.label)
                   


class Axe:
    
    tortue_axe = turtle.Turtle()
    tortue_axe.hideturtle()
    tortue_axe.speed(0)
    tortue_axe.getscreen().tracer(400)

    def __init__(self):
        self.hauteur=None
        self.largeur=None
    
    def trace(self):
        # Récupération taille du papier
        self.hauteur = turtle.window_height()
        self.largeur = turtle.window_width()
        xstampsize = Axe.tortue_axe.shapesize()[0] * 5
        ystampsize = 0
        ligne(Axe.tortue_axe,-self.largeur//2,0,self.largeur-xstampsize,0)
        Axe.tortue_axe.stamp()
        ligne(Axe.tortue_axe,0,-self.hauteur//2,self.hauteur-ystampsize,90)
        Axe.tortue_axe.stamp()

    def taille_fleche(self,sizex,sizey):
        Axe.tortue_axe.shapesize(sizex,sizey)


            
        


                
                
    


