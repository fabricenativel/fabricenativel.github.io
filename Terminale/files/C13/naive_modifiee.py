
def recherche(motif,chaine):
    lm,lc = len(motif),len(chaine)
    nb_comparaisons = 0
    for i in range(lc-lm+1):
        i_motif,i_chaine = 0,i
        nb_comparaisons+=1
        while i_motif<lm and chaine[i_chaine] == motif[i_motif]:
            nb_comparaisons += 1
            i_motif += 1
            i_chaine += 1
        if i_motif == lm:
            return True , nb_comparaisons
    return False , nb_comparaisons

print(recherche("aaaaaaaaab","a"*10000))

