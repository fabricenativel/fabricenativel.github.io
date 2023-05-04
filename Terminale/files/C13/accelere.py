

def traite(motif):
    ''' Construction d'un dictionnaire donnant l'indice de la dernière occurence d'un caractère dans le motif'''
    emplacement = {}
    for i  in range(len(motif)):
        caractere = motif[i]
        emplacement[caractere] = i
    return emplacement

def recherche(motif,chaine):
    lm,lc = len(motif),len(chaine)
    i_chaine = lm
    emplacement = traite(motif)
    print(emplacement)
    while i_chaine<lc:
        print(f"Indice dans la chaine : {i_chaine}")
        a=input("ok")
        i = 1
        print(f"Comparaisons '{motif[lm-i]}' et '{chaine[i_chaine-i]}'")
        while i<lm and motif[lm-i]==chaine[i_chaine-i]:
            print(f"Comparaisons '{motif[lm-i]}' et '{chaine[i_chaine-i]}'")
            i+=1
        if i==lm:
            return True
        else:
            if chaine[i_chaine-i]  in emplacement:
                i_chaine += lm - emplacement[chaine[i_chaine-i]] -1
            else:
                i_chaine += lm
    return False

print(recherche("exemple","un excellent exemple et un exercice extraordinaire"))