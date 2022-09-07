ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    return ALPHABET.find(lettre)

def cesar(message, decalage):
    resultat = ''
    for lettre in message : #(1)
        if lettre in ALPHABET :
            indice = (position_alphabet(lettre) + decalage)%26 #(2)
            resultat = resultat + ALPHABET[indice]
        else:
            resultat = resultat + lettre #(3)
    return resultat
