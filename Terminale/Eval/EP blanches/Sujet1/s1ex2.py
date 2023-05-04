# %%
def insertion(element,liste):
    '''Insère element dans  liste (qui est déjà triée)'''
    liste.append(element)
    pos = len(liste)-1
    while pos>0 and liste[pos]<liste[pos-1]:
        liste[pos],liste[pos-1] =  liste[pos-1],liste[pos]
        pos = pos - 1
