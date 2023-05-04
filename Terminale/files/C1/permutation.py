def permutation(liste):
    if liste==[]:
        return [[]]
    else:
        for index in range(len(liste)):
            element=liste.pop(index)
            nperm=[]
            for perm in permutation(liste):
                for position in range(len(perm)+1):
                    lperm=insere(perm,element,position)
                    nperm.append(lperm)
            return nperm

def insere(liste,element,position):
    new_liste = liste.copy()
    new_liste.insert(position,element)
    return new_liste

print(permutation([1,2,3,4]))
            
            