from random import randint


def echange(liste,i,j):
    liste[i],liste[j] = liste[j],liste[i]

# Tri par insertion
def tri_insertion(liste):
    for ind in range(1,len(liste)-1):
        j = ind
        while liste[j+1]<liste[j] and j>=0:
            echange(liste,j,j+1)
            j=j-1


ex_liste = [randint(1,100) for _ in range(50)]
tri_insertion(ex_liste)
print(ex_liste)