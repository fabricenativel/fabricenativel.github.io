def chiffre_xor(texte,cle):
    texte_chiffre = ""
    for caractere in texte:
        caractere_chiffre = chr(ord(caractere) ^ cle)
        texte_chiffre += caractere_chiffre
    return texte_chiffre

print(chiffre_xor("Bravo, vous avez réussi !",51))
