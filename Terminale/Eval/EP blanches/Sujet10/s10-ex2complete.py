def binaire(n):
    # On effectue la première division euclidienne, le reste doit être converti en chaine de caractères pour l'ajouter à l'écriture binaire
    ecriture_binaire = str(n%2)
    n = n // 2
    # Tant que le quotient n'est pas nul, on recommence
    while n != 0  :
        ecriture_binaire =  str (n%2) + ecriture_binaire
        n = n // 2
    return ecriture_binaire

print(binaire(77))