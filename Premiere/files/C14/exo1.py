import csv

fichier_amelie=open("./docs/files/C14/contacts_amelie.csv","r",encoding="utf-8")
contact_amelie = list(csv.DictReader(fichier_amelie,delimiter=','))
fichier_amelie.close()

fichier_florent=open("./docs/files/C14/contacts_florent.csv","r",encoding="utf-8")
contact_florent = list(csv.DictReader(fichier_florent,delimiter=','))
fichier_florent.close()

contacts = contact_amelie + contact_florent

for ca in contact_amelie:
    for cf in contact_florent:
        if ca["Téléphone"]==cf["Téléphone"]:
             print(f"Doublon rencontré : {ca}")


# On récupère les clés du dictionnaire avec la méthode "keys()"
cles_dico = contacts[0].keys()
# On ouvre un fichier en écriture
with open('./docs/files/C14/contacts.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, cles_dico)
    # On y écrit les entêtes(les clés) puis les valeurs 
    dict_writer.writeheader()
    dict_writer.writerows(contacts)