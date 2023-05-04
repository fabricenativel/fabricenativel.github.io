import fitz
from time import time

# Pour proteger un pdf avec mot de passe : pdftk source.pdf output destination.pdf user_pw password
# Fichier 1 : le mot de passe est un code de carte bancaire : XXXX : 0991
# Fichier 2 : le mot de passe est une date de naissance : jjmmaaaa (aaaa > 1900) : 28121969
# Fichier 3 : le mot de passe est un mot de 7 lettres (écrit en minuscule) figurant dans le dictionnaire : carotte
# Fichier 4 : mot de passe faible issu du projet Richelieu (https://github.com/tarraschk/richelieu/blob/master/french_passwords_top20000.txt)  : blackangel 
# Fichier 5 : le mot de passe est un prénom suivi d'un numéro de département : Gabriel77

FILE = "/home/fenarius/Travail/Cours/fabricenativel.github.io/docs/Premiere/files/Projets/forcebrute/protege2.pdf"
DOC = fitz.Document(FILE)


def tp(file,password):
    return DOC.authenticate(password)

debut = time()
for jj in range(1,32):
    for mm in range(1,13):
        for aaaa in range(1900,2023):
            test_mdp = str(jj)+str(mm)+str(aaaa)
            if tp(FILE,test_mdp):
                print(f"Mot de passe trouvé : {test_mdp}")
fin = time()

print(fin-debut)

