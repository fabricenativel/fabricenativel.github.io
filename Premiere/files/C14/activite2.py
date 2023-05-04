import csv

# Données de la table d'Antoine
fichier=open("./docs/files/C14/population_jessica.csv","r",encoding="utf-8")
population = list(csv.DictReader(fichier,delimiter=','))
fichier.close()

# Données de la table de Justine
fichier=open("./docs/files/C14/surface_albert.csv","r",encoding="utf-8")
surface = list(csv.DictReader(fichier,delimiter=','))
fichier.close()

def get_surface(nom):
    for pays in surface:
        if pays['Nom']==nom:
            return pays['Surface (km²)']

# Concaténation des deux tables
fusion = []
for pays in population:
    nom_pays = pays['Nom']
    population_pays = pays['Population']
    surface_pays = get_surface(nom_pays)
    fusion.append({'Nom':nom_pays,'Population':population_pays,'Surface':surface_pays})
    
print(fusion)