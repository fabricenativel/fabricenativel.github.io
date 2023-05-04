import os

BASE = "/home/fenarius/Travail/Cours/fabricenativel.github.io/docs/officiels/Annales/"

# Vérifie la présence des fichiers pdf et py pour les épreuves pratiques
annee = input("Quelle année ?")
nbr = int(input("Nombres de sujets ?"))

def get_file(annee,extension,numero):
    num = str(numero).zfill(2)
    return f"{BASE}/EP/{annee}/{annee[-2:]}-NSI-{num}/{annee[-2:]}-NSI-{num}.{extension}"

bug = False
for i in range(1,nbr+1):
    for ext in ["pdf","py"]:
        if not os.path.isfile(get_file(annee,ext,i)):
            print(f"*** Manquant : sujet {i} {ext}")
            bug = True

if not bug:
    print("Tous les fichiers sont présents")
