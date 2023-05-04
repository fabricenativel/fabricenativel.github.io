from graphviz import Digraph

    
class ABR:
    ''' Implementation des arbres binaires de recherche avec une seule classe
    L'arbre vide est celui dont la racine est None
    '''

    # Pour l'affichage de l'arbre - ne pas en tenir compte
    vn = 0

    def __init__(self, valeur=None):
        self.valeur = valeur
        if valeur is not None:
            self.gauche = ABR()
            self.droit = ABR()

    def est_vide(self):
        return self.valeur is None

    def insere_une_valeur(self, v):
        if self.est_vide():
            self.valeur = v
            self.gauche = ABR()
            self.droit = ABR()
        elif v > self.valeur:
                self.droit.insere_une_valeur(v)
        elif v < self.valeur:
                self.gauche.insere_une_valeur(v)

    
    # Parcours l'abre en récupérant les noeuds et les arêtes au format utilisé par Digraph
    def arbre_digraph(self):
        noeuds=[]
        aretes=[]
        if not self.est_vide():
            noeuds=[self.valeur]
            if not self.gauche.est_vide():
                aretes.append([self.valeur,self.gauche.valeur])
                noeud_gauches, aretes_gauche = self.gauche.arbre_digraph()
                noeuds = noeuds + noeud_gauches
                aretes = aretes + aretes_gauche
            else:
                noeuds = noeuds + ["V"+str(ABR.vn)]
                aretes.append([self.valeur,"V"+str(ABR.vn)])
                ABR.vn += 1
            if not self.droit.est_vide():
                aretes.append([self.valeur,self.droit.valeur])
                noeud_droits, aretes_droit = self.droit.arbre_digraph()
                noeuds = noeuds + noeud_droits
                aretes = aretes + aretes_droit
            else:
                noeuds = noeuds + ["V"+str(ABR.vn)]
                aretes.append([self.valeur,"V"+str(ABR.vn)])
                ABR.vn += 1
        return noeuds,aretes
    
    def affiche(self):
        # création de l'objet graphviz qui sera renvoyé
        img_arbre = Digraph()
        noeuds, aretes = self.arbre_digraph()
        for n in noeuds:
            if str(n)[0]!="V":
                img_arbre.node(str(n),str(n))
            else:
                img_arbre.node(str(n),"",color="#00FF00000")
        for a in aretes:
            if str(a[1])[0]!="V":
                img_arbre.edge(str(a[0]),str(a[1]))
            else:
                img_arbre.edge(str(a[0]),str(a[1]),color="#FF0000")
        img_arbre.render(view=True)
    

