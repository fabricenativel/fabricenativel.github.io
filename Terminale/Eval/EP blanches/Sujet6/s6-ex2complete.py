def unique(liste):
    """Renvoie True si les élements de liste sont uniques, False sinon"""
    deja_vu = []
    for element in liste:
        if element in deja_vu:
            return False
        else:
            deja_vu.append(element)
    return True

