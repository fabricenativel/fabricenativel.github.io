
def tri_insertion(liste):
    """ trie par insertion la liste en paramètre """
    passage = 0
    for indice_courant in range(1,len(liste)):
        passage += 1
        element_a_inserer = liste[indice_courant]
        i = indice_courant - 1
        while i >= 0 and liste[i] > element_a_inserer :
            liste[i+1] = liste[i]
            i = i - 1
        liste[i + 1] = element_a_inserer
        print(passage,liste)

notes = [8, 7, 18, 14, 12, 9, 17, 3]
tri_insertion(notes)
print(notes)