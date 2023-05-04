#! /usr/bin/python3
import tkinter
from random import shuffle
import time

NB_CARTES=8
empty_card=8
TITRE_FEN = "Ranger les cartes dans l'ordre"
W_HEIGHT=360
BG_COLOR="navy"
LABEL_COLOR = "white"
BG_BUTTON="#555555"
FG_BUTTON="yellow"
IMG_PATH = "./img/"
OX = 20
LX = 180
H_CARD = 40
H_LABEL=20
NUM = [i for i in range(0,8)]
X_GM,Y_GM,W_GM = 20,320,450
X_EC,Y_EC,W_EC = 800,320,450
F_LABEL=20
FLECHE=chr(0x1F847)
FLECHE_COLOR="red"
REPERE =  chr(0x2B24)
REPERE_COLOR1= "orange"
REPERE_COLOR2= "lime"
CLIG=0.5
R_LABEL = 300



class Jeu:
    
    def __init__(self):
        self.jeu = [i for i in range(1,9)]
        shuffle(self.jeu)
        self.fen = tkinter.Tk()
        self.can = tkinter.Canvas(master=self.fen,width=NB_CARTES*200,height=W_HEIGHT,bg=BG_COLOR)
        self.mfrom = tkinter.IntVar(self.fen,0) #La carte potentiellement échangée avec la suivante
        self.affiche = False
        self.bouton_getmax = tkinter.Button(self.fen, text ="Echanger la carte située à l'emplacement ", command = self.echange,bg=BG_BUTTON,fg=FG_BUTTON,borderwidth=0)
        self.bouton_check = tkinter.Button(self.fen, text ="Vérifier", command = self.check,bg=BG_BUTTON,fg=FLECHE_COLOR,borderwidth=0)
        self.bouton_quit = tkinter.Button(self.fen, text ="Quitter", command = self.quit,bg=BG_BUTTON,fg=FLECHE_COLOR,borderwidth=0)
        self.bouton_init = tkinter.Button(self.fen, text ="Recommencer", command = self.restart,bg=BG_BUTTON,fg=FLECHE_COLOR,borderwidth=0)
        self.choix_getmax = tkinter.OptionMenu(self.fen, self.mfrom, *NUM)
        self.choix_getmax.config(bg=BG_BUTTON,fg=FG_BUTTON,borderwidth=0)
        self.images=[tkinter.PhotoImage(master=self.fen,file="./img/C"+str(i)+'.png') for i in range(0,9)]
        self.cnums = [tkinter.Label(self.fen,text=str(i),fg=LABEL_COLOR,bg=BG_COLOR,font=("Arial",18,"bold")) for i in range(0,8)]
        self.et = tkinter.Label(self.fen,text="avec la carte suivante si elles ne sont pas dans le bon ordre",fg=LABEL_COLOR,bg=BG_COLOR,font=("Arial",14))
        self.repere1 = tkinter.Label(self.fen,text=REPERE,fg=REPERE_COLOR1,bg=BG_COLOR,font=("Arial",18,"bold"))
        self.repere2 = tkinter.Label(self.fen,text=REPERE,fg=REPERE_COLOR2,bg=BG_COLOR,font=("Arial",18,"bold"))
        self.messsage = tkinter.Label(self.fen,text="",fg="red",bg=BG_COLOR,font=("Arial",18,"bold"))
        self.state=False
        self.fen.bind("<Key>",self.cc)

    def quit(self):
        self.fen.destroy()

    def restart(self):
        self.jeu = [i for i in range(1,9)]
        shuffle(self.jeu)
        self.mfrom.set(0)
        self.show()
        self.messsage.config(fg=BG_COLOR)
        self.can.update()
        self.state=False
        self.show_cards()
    
    def cc(self,event):
        if event.char=='$':
            self.state=not self.state 
            self.show_cards(self.state)

    def check(self):
        if all(self.jeu[i] < self.jeu[i+1] for i in range(NB_CARTES-1)):
            self.messsage.config(text='GAGNÉ',fg='red')
        else:
            self.messsage.config(text='PERDU',fg='red')
        self.messsage.place(x=1100,y=Y_EC,anchor=tkinter.N)
        self.show_cards(True)
        self.state=True
        self.can.update()

    def show(self):
        self.fen.title(TITRE_FEN)
        self.can.pack()
        self.bouton_getmax.place(x=X_GM,y=Y_GM,width=W_GM)
        self.choix_getmax.place(x=X_GM+W_GM,y=Y_GM)
        for i in range(0,8):
            self.cnums[i].place(x=OX+LX//2+LX*i,y=H_LABEL,anchor=tkinter.E)
        self.bouton_check.place(x=X_EC+W_EC+230,y=60,height=80,width=100)
        self.bouton_init.place(x=X_EC+W_EC+230,y=160,height=80,width=100)
        self.et.place(x=X_GM+W_GM+300,y=Y_EC,anchor=tkinter.N)
        self.bouton_quit.place(x=X_EC+W_EC+230,y=Y_EC,width=100)

    def show_cards(self,view=False):
        if not view:
            for i in range(NB_CARTES):
                self.can.create_image(LX*i+OX, H_CARD, anchor=tkinter.NW, image=self.images[0]) 
        else:
            for i in range(NB_CARTES):
                self.can.create_image(LX*i+OX, H_CARD, anchor=tkinter.NW, image=self.images[self.jeu[i]]) 

    def loop(self):
        self.fen.mainloop()


    def move(self,ind1,ind2):
        indmini=min(ind1,ind2)
        indmaxi=max(ind1,ind2)
        self.repere1.configure(fg=REPERE_COLOR1)
        self.repere2.configure(fg=REPERE_COLOR2)
        self.repere1.place(x=OX+LX//2+LX*indmini,y=R_LABEL,anchor=tkinter.E)
        self.repere2.place(x=OX+LX//2+LX*indmaxi,y=R_LABEL,anchor=tkinter.E)
        for xt in range(OX+LX//2+LX*indmini,OX+LX//2+LX*indmaxi):
            self.repere1.place(x=xt,y=R_LABEL,anchor=tkinter.E)
            self.repere2.place(x=OX+LX//2+LX*indmaxi+OX+LX//2+LX*indmini-xt,y=R_LABEL,anchor=tkinter.E)
            time.sleep(0.005)
            self.can.update()
        self.repere1.configure(fg=BG_COLOR)
        self.repere2.configure(fg=BG_COLOR)
        self.can.update()

    def echange(self):
        ind = self.mfrom.get()
        if self.jeu[ind]>self.jeu[ind+1]:
            self.jeu[ind],self.jeu[ind+1]=self.jeu[ind+1],self.jeu[ind]
            self.move(ind,ind+1)
            self.show_cards(self.state)
        else:
            self.repere1.place(x=OX+LX//2+LX*ind,y=R_LABEL,anchor=tkinter.E)
            self.repere2.place(x=OX+LX//2+LX*ind+LX,y=R_LABEL,anchor=tkinter.E)
            for _ in range(5):
                self.repere1.config(fg=BG_COLOR)
                self.repere2.config(fg=BG_COLOR)
                self.can.update()
                time.sleep(0.2)
                self.repere2.config(fg=REPERE_COLOR2)
                self.repere1.config(fg=REPERE_COLOR1)
                self.can.update()
                time.sleep(0.2)
            self.repere1.configure(fg=BG_COLOR)
            self.repere2.configure(fg=BG_COLOR)
            self.can.update()


                


un_jeu= Jeu()
un_jeu.show()
un_jeu.show_cards(un_jeu.state)
un_jeu.loop()
