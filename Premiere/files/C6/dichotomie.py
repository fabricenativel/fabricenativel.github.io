import time
import matplotlib.pyplot as plt


def recherche(element,liste):
    ''' Renvoie True si element est dans liste, False sinon '''
    for x in liste:
        # Si x est bien égal à élément renvoyer True sinon continuer le parcours
        if x==element: 
            return True
    # Si on atteint la ligne suivante on renvoie False puisqu'aucun élément n'est égal à celui recherché
    return False

def temps_execution(n):
    # On crée la liste des n premiers entiers
    liste = [i for i in range(0,n)]
    # On y recherche -1 (qui n'y est pas !) en mesurant le temps d'exécution
    debut = time.time()
    recherche(-1,liste)
    fin = time.time()
    return fin-debut

def recherche_dichotomie(element,liste):
    debut = 0
    fin = len(liste)-1
    while fin-debut>0:
        milieu = (debut+fin)//2
        if element>liste[milieu]:
            debut=milieu+1
        else:
            fin=milieu
    if element==liste[debut]:
        return True
    else:
        return False

def temps_execution_dicho(n):
    # On crée la liste des n premiers entiers
    liste = [i for i in range(0,n)]
    # On y recherche -1 (qui n'y est pas !) en mesurant le temps d'exécution
    debut = time.time()
    recherche_dichotomie(-1,liste)
    fin = time.time()
    return fin-debut


x = [100000*k for k in range(1,21)]
y = [temps_execution(l) for l in x]
y_dicho = [temps_execution_dicho(l) for l in x]

plt.xlabel("Taille des donnés")
plt.ylabel("Temps d'exécution")
plt.suptitle("Comparaison recherche simple et recherche par dichotomie")
g1 = plt.plot(x, y,label="Recherche simple")
g2 = plt.plot(x,y_dicho,label="Recherche dichotomique")
plt.legend()
plt.show()