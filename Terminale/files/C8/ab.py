from graphviz import Digraph


# Classe noeud pour un arbre binaire
class Noeud:
    
    def __init__(self, etiquette, gauche=None, droit=None):
        self.etiquette = etiquette
        self.gauche = gauche
        self.droit = droit
    
    def est_feuille(self):
        return self.gauche==None and self.droit==None
        

class ArbreBinaire:
    
    def __init__(self,racine):
        # racine est soit None (arbre vide) soit un objet de la classe noeud
        self.racine=racine
    
    def est_vide(self):
        return self.racine == None
    
    # Parcours l'abre en récupérant les noeuds et les arêtes au format utilisé par Digraph
    def arbre_digraph(self):
        noeuds=[]
        aretes=[]
        if self!=None:
            noeuds=[self.racine.etiquette]
            if self.racine.gauche!=None:
                aretes.append([self.racine.etiquette,self.racine.gauche.etiquette])
                sag = ArbreBinaire(self.racine.gauche)
                pg = sag.arbre_digraph()
                noeuds = noeuds + pg[0]
                aretes = aretes + pg[1]
            if self.racine.droit!=None:
                aretes.append([self.racine.etiquette,self.racine.droit.etiquette])
                sad = ArbreBinaire(self.racine.droit)
                pd = sad.arbre_digraph()
                noeuds = noeuds + pd[0]
                aretes = aretes + pd[1]
        return noeuds,aretes
            
    def affiche(self):
        # création de l'objet graphviz qui sera renvoyé
        img_arbre = Digraph()
        noeuds, aretes = self.arbre_digraph()
        for n in noeuds:
            img_arbre.node(n,n)
        for a in aretes:
            img_arbre.edge(a[0],a[1])
        img_arbre.render(view=True)
    
    def taille(self):
        if self.racine==None:
            return 0
        else:
            sag = ArbreBinaire(self.racine.gauche)
            sad = ArbreBinaire(self.racine.droit)
            return 1+sag.taille()+sad.taille()
    
    def hauteur(self):
        if self.racine==None:
            return 0
        else:
            sag = ArbreBinaire(self.racine.gauche)
            sad = ArbreBinaire(self.racine.droit)
            return 1+max(sag.hauteur(),sad.hauteur())

n =  Noeud('5')
a = ArbreBinaire(n)
a.affiche()