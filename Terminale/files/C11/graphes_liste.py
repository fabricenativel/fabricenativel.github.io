class Graphe:

    def __init__(self,sommets):
        self.taille = len(sommets)
        self.listes = {}
        for s in sommets:
            self.listes[s]=[]
    
    def ajoute_arete(self,depart,arrivee):
        assert depart in self.listes.keys(), "Le sommet de départ n'existe pas"
        assert arrivee in self.listes.keys(), "Le sommet d'arrivée n'existe pas"
        if arrivee not in self.listes[depart]:
            self.listes[depart].append(arrivee)
    
    def ajoute_sommet(self,sommet):
        assert sommet not in self.listes.keys(), "Le sommet existe déjà"
        self.taille += 1
        self.listes[sommet]=[]
    
    def voisins(self,sommet):
        return self.listes[sommet]
        