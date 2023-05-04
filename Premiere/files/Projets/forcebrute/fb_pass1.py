import fitz

FILE = "protege1.pdf"
DOC = fitz.Document(FILE)


def test_password(password):
    '''Renvoie True lorsque password permet d'ouvrir le fichier FILE déclaré ci-dessus'''
    return DOC.authenticate(password)


for x in range(10000):
    if test_password(str(x).zfill(4)):
        print(f"Ok : {x}")