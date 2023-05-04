import csv
from random import shuffle, randint

nombre = 50

# Attention : préciser éventuellement le chemin d'accès complet du fichier
fichier_prenoms=open("./docs/files/C7/Prenoms-974-2000.csv","r",encoding="iso-8859-1")
# Lecture sous forme de dictionnaire 
prenoms = list(csv.DictReader(fichier_prenoms,delimiter=','))
fichier_prenoms.close()


def gen_tel():
    if randint(0,2)==0:
        prefixe = "06 93"
    else:
        prefixe = "06 92"
    suffixe = " "
    for _ in range(3):
        suffixe += str(randint(0,99)).zfill(2)+" "
    return prefixe+suffixe[:-1]

prenoms = [p for p in prenoms if p['preusuel']!='_PRENOMS_RARES' and int(p['nombre'])>5 and p['annais']=='2010']

shuffle(prenoms)
clist = []
for i in range(nombre):
    clist.append({"Prénom":prenoms[i]["preusuel"],"Téléphone":gen_tel()})

keys = clist[0].keys()

with open('./docs/files/C7/contacts.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(clist)
