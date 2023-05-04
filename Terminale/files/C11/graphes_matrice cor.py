class Graphe:

    def __init__(self,sommets):
        self.sommets=sommets
        self.taille = len(sommets)
        self.matrice = [[0]*self.taille for _ in range(self.taille)]
    
    def ajoute_arete(self,depart,arrivee):
        assert depart in self.sommets and arrivee in self.sommets
        lig = self.sommets.index(depart)
        col = self.sommets.index(arrivee)
        self.matrice[lig][col] = 1
    
    def supprime_arete(self,depart,arrivee):
        assert depart in self.sommets and arrivee in self.sommets
        lig = self.sommets.index(depart)
        col = self.sommets.index(arrivee)
        self.matrice[lig][col] = 0
    
    def get_voisin(self,sommet):
        assert sommet in self.sommets
        voisins = []
        lig = self.sommets.index(sommet)
        for col in range(self.taille):
            if self.matrice[lig][col] == 1:
                voisins.append(self.sommets[col])
        return voisins

    def parcours_largeur(self,depart):
        assert depart in self.sommets
        a_traiter = [depart]
        deja_vu = [depart]
        pl  = []
        while a_traiter != []:
            sommet = a_traiter[0]
            voisins = self.get_voisin(sommet)
            for v in voisins:
                if v not in deja_vu:
                    a_traiter.append(v)
                    deja_vu.append(v)
            pl.append(sommet)
            a_traiter.pop(0)
        return pl
    
    def parcours_profondeur(self,start,parcourus=None):
        if parcourus == None:
            parcourus = []
        parcourus.append(start)
        for v in self.get_voisin(start):
            if v not in parcourus:
                self.parcours_profondeur(v,parcourus)
        return parcourus
            


g = Graphe(["A","B","C","D","E"])
g.ajoute_arete("A","B")
g.ajoute_arete("A","C")
g.ajoute_arete("A","D")
g.ajoute_arete("B","D")
g.ajoute_arete("B","E")
print(g.matrice)
print(g.get_voisin("A"))
print(g.parcours_largeur("A"))
print(g.parcours_profondeur("A"))









    


