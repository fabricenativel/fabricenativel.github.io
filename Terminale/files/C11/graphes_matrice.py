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








    


