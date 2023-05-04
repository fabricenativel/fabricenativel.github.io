def rendu_monnaie(somme,systeme_monetaire):
    ''' Renvoie la liste des pieces de systeme_monetaire permettant de former  somme'''
    # Cas de base, la somme à rendre est nulle
    if somme==0:
        return []
    else:
    # Appel récursif selon que la pièce de plus grande valeur (forcément situé en début de systeme_monetaire) est utilisée ou non
        piece = systeme_monetaire[0]
        if somme>=piece:
            # piece utilisée, l'ajouter à liste qu'on renvoie et la soustraire de la somme
            return rendu_monnaie(somme-piece,systeme_monetaire)+[piece]
        else:
            # pièce non utilisée car de trop grande valeur, la supprimer du système monétaire
            systeme_monetaire.pop(0)
            return rendu_monnaie(somme,systeme_monetaire)

print(rendu_monnaie(9,[50,20,10,5,2,1]))
