
import requests
import os

os.makedirs("ECE_NSI", exist_ok=True)
res = requests.get("https://cyclades.education.gouv.fr/delos/api/public/sujets/ece?sort=libelle&order=ASC&page=0&itemsPerPage=100")
for sujet in res.json()["content"]:
    if "NSI" not in sujet["cle"]:
        continue
    id = sujet["id"]
    sdata = requests.get(f"https://cyclades.education.gouv.fr/delos/api/public/sujet/{id}").json()
    spath = os.path.join("ECE_NSI", f"SUJET_{int(sdata['cle'].replace('BCG_NSI_', '')):02}")
    os.makedirs(spath, exist_ok=True)
    for f in sdata["fichiers"]:
        print(f["id"], id)
        sfile = requests.get("https://cyclades.education.gouv.fr/delos/api/public/file/", params=dict(idSujet=id, fileName=f['id']))
        fpath = os.path.join(spath, f["name"])
        with open(fpath, 'wb') as sf:
            sf.write(sfile.content)
        base, ext = os.path.splitext(fpath)
        