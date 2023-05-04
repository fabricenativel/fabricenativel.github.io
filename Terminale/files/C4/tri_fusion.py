
from random import randint

def split(l):
    n=len(l)//2
    return l[:n],l[n:]

def fusion(l1,l2):
    ind1=0
    ind2=0
    l = []
    while ind1<len(l1) and ind2<len(l2):
        if l1[ind1]<l2[ind2]:
            l.append(l1[ind1])
            ind1+=1
        else:
            l.append(l2[ind2])
            ind2+=1
    if ind1==len(l1):
        for k in range(ind2,len(l2)):
            l.append(l2[k])
    else:
        for k in range(ind1,len(l1)):
            l.append(l1[k])
    return l

def tri_fusion(liste):
    # Condition d'arrêt : une liste ayant moins de deux éléments est déjà triée
    if len(liste)<2:
        return liste
    # Sinon : on partage la liste en deux
    l1,l2 = split(liste)
    # On tri récursivement chaque moitiée
    l1_tri = tri_fusion(l1)
    l2_tri = tri_fusion(l2)
    # On fusionne
    return fusion(l1_tri,l2_tri)

l = [10,6,3,9,7,5]
print(l)
t = tri_fusion(l)
print(t)