def chiffre(texte,cle):
    ''' Renvoie le chiffrement de texte par decalage de cle emplacements'''
    texte_code = ""
    for caractere in texte:
        num = ord(caractere)
        num = num + cle
        if num>ord('Z'):
            num=num-26
        texte_code += chr(num)
    return texte_code


