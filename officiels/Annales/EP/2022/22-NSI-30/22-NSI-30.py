def rom_to_dec (nombre):

    """ Renvoie l’écriture décimale du nombre donné en chiffres romains """

    dico = {"I":1, "V":5, ...}
    if len(nombre) == 1:
        return ...`

    else:
        ### on supprime le premier caractère de la chaîne contenue dans la variable nombre
		 ### et cette nouvelle chaîne est enregistrée dans la variable nombre_droite
        nombre_droite = nombre[1:]
    
        
        if dico[nombre[0]] >= dico[nombre[1]]:
            return dico[nombre[0]] + ...
        else:
            return ...

assert rom_to_dec("CXLII") == 142
