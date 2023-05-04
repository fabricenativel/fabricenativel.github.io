ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def chiffre_caractere(caractere,cle):
    if caractere in ALPHABET:
        #recuperation du code ascii du caractere (voir la fonction ord de Python)
        code_caractere=ord(caractere)
        #decalage de cle emplacement
        code_caractere = code_caractere + cle
        #on prevoit le cas ou le code depasse celui de Z
        if code_caractere > ord("Z"):
            code_caractere=code_caractere - 26
        if code_caractere < ord("A"):
            code_caractere=code_caractere + 26
        # recuperation du caractere a partir du code  (voir la fonction chr de Python)
        nouveau_caractere = chr(code_caractere)
        return nouveau_caractere
    else:
        return caractere

def chiffre_texte(texte,cle):
    texte_c = ""
    for caractere in texte:
        texte_c += chiffre_caractere(caractere,cle)
    return texte_c

texte = "Ru yxdbbj dw yaxoxwm bxdyra, b'jbbrc mjwb bxw urc, b'jyydhjwc bda bxw yxuxlqxw. Ru yarc dw axvjw, ru u'xdearc, ru udc; vjrb ru w'h bjrbrbbjrc zd'dw rvkaxpurx lxwodb, ru kdcjrc à cxdc rwbcjwc bda dw vxc mxwc ru rpwxajrc uj brpwrorljcrxw.".upper()
print(texte)
for cle in range(9,10):
    print(cle)
    print(chiffre_texte(texte,-cle))
