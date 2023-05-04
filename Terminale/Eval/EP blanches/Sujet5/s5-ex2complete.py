def fusion(l1,l2):
    """fusion récursive des deux listes l1 et l2 déjà triées"""
    if l1 == []:
        return l2
    if l2 == []:
        return l1
    if l1[0]<l2[0]:
        return [l1[0]] + fusion(l1[1:],l2)
    else:
        return [l2[0]] + fusion(l1,l2[1:])