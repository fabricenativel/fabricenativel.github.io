def envers(chaine):
    resultat = ""
    for caractere in chaine:
        resultat = caractere + resultat
    return resultat

print(envers("super"))