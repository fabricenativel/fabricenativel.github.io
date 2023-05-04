def est_pair(n):
		''' Renvoie True ou False suivant que n est pair ou non'''
		assert type(n)==int, "le paramètre n'est pas un nombre entier"
		return n%2==0
    

print(est_pair(14))