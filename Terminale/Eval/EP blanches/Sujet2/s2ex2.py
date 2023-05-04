def dichotomie(liste,element):
    ''' recherche element dans liste en utilisant la recherche dichotomique'''
    debut = 0
    fin = len(liste)-1
    while debut<=fin:
        milieu = (debut+fin)//2
        if liste[milieu]==element:
            return True
        if liste[milieu]>element:
            fin = milieu-1
        else:
            debut = milieu+1
    return False

print(dichotomie([15, 15,15,18,22,31],15))

print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],27))