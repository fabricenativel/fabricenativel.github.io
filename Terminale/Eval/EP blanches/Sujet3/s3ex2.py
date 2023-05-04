def rendre_monnaie(s,pieces):
    indice_piece = len(pieces)-1
    a_rendre = []
    while s != 0:
        if pieces[indice_piece]<=s:
            s=s-pieces[indice_piece]
            a_rendre.append(pieces[indice_piece])
        else:
            indice_piece -= 1
    return a_rendre

print(rendre_monnaie(128,[1,2,5,10,20,50]))
        