
def recherche(motif,chaine):
    lm,lc = len(motif),len(chaine)
    for i in range(lc-lm+1):
        i_motif,i_chaine = 0,i
        while i_motif<lm and chaine[i_chaine] == motif[i_motif]:
            i_motif += 1
            i_chaine += 1
        if i_motif == lm:
            return True
    return False

