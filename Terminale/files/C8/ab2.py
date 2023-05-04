from graphviz import Digraph


# Classe noeud pour un arbre binaire
class ArbreBinaire:
    
    empty = 0

    def __init__(self, etiquette=None):
        self.etiquette = etiquette
        if self.etiquette is not None:
            self.gauche = ArbreBinaire()
            self.droit = ArbreBinaire()
    
    def est_feuille(self):
        return self.gauche==None and self.droit==None
        
    def est_vide(self):
        return self.etiquette is None
    
    def taille(self):
        if self.etiquette==None:
            return 0
        else:
            return 1+self.gauche.taille()+self.droit.taille()
    
    def hauteur(self):
        if self.etiquette==None:
            return 0
        else:
            return 1+max(self.gauche.taille(),self.droit.taille())
    
    def insere(self,valeur):
        if self.etiquette == None:
            return ArbreBinaire(valeur)
        elif valeur <= self.etiquette:
            self.gauche = self.gauche.insere(valeur)
        else:
            self.droit = self.droit.insere(valeur)
        return self
    
    def insere_liste(self,valeurs):
        for v in valeurs:
            self.insere(v)
    
    # Parcours l'abre en récupérant les noeuds et les arêtes au format utilisé par Digraph
    def arbre_digraph(self):
        noeuds=[]
        aretes=[]
        if self!=None:
            noeuds=[str(self.etiquette)]
            if not self.gauche.est_vide():
                aretes.append([str(self.etiquette),str(self.gauche.etiquette)])
                noeuds_gauches,aretes_gauches = self.gauche.arbre_digraph()
                noeuds = noeuds + noeuds_gauches
                aretes = aretes + aretes_gauches
            else:
                noeuds.append("V"+str(ArbreBinaire.empty))
                aretes.append([str(self.etiquette),"V"+str(ArbreBinaire.empty)])
                ArbreBinaire.empty += 1
            if not self.droit.est_vide():
                aretes.append([str(self.etiquette),str(self.droit.etiquette)])
                noeuds_droits,aretes_droits = self.droit.arbre_digraph()
                noeuds = noeuds + noeuds_droits
                aretes = aretes + aretes_droits
            else:
                aretes.append([str(self.etiquette),"V"+str(ArbreBinaire.empty)])
                noeuds.append("V"+str(ArbreBinaire.empty))
                ArbreBinaire.empty += 1
        return noeuds,aretes
            
    def affiche(self):
        # création de l'objet graphviz qui sera renvoyé
        img_arbre = Digraph(engine='neato')
        img_arbre.graph_attr['rankdir'] = 'TD'
        noeuds, aretes = self.arbre_digraph()
        p = 0
        for n in noeuds:
            if n[0]=='V':
                img_arbre.node(n,"",color="#FF00000")
            else:
                img_arbre.node(n,n)
                p += 1
        img_arbre.node("t","test",pos="5,5!")
        for a in aretes:
            if a[1][0]=="V":
                img_arbre.edge(a[0],a[1],label=None,color="#FF0000")
            else:
                img_arbre.edge(a[0],a[1],label=None)
        img_arbre.render(view=True)
    

   

a = ArbreBinaire(5)
a.insere_liste([1,7,2,10,11,4,8,9,13,6])
a.affiche()