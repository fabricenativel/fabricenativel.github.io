import csv

# Données de la table d'Antoine
fichier=open("./docs/files/C14/pays_antoine.csv","r",encoding="utf-8")
pays_antoine = list(csv.DictReader(fichier,delimiter=','))
fichier.close()

# Données de la table de Justine
fichier=open("./docs/files/C14/pays_justine.csv","r",encoding="utf-8")
pays_justine = list(csv.DictReader(fichier,delimiter=','))
fichier.close()

# Concaténation des deux tables
pays = pays_justine + pays_antoine

print(pays)