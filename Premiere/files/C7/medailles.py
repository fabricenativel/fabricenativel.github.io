import csv
# Attention : préciser éventuellement le chemin d'accès complet du fichier
fichier_medailles=open("/home/fenarius/Travail/Cours/MkDocs/docs/files/C5/Tokyo2021.csv","r",encoding="utf-8")
# Lecture sous forme de dictionnaire 
medailles = list(csv.DictReader(fichier_medailles,delimiter=','))
fichier_medailles.close()

def total_medailles(pays):
    return int(pays["Total"])


medailles = sorted(medailles,key=total_medailles,reverse=True)
for pays in medailles:
    print(pays["Country"],pays["Total"])
