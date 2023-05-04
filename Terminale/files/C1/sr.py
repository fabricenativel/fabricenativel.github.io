def somme_recursive(n):
    if n==0: 
        return 0
    else:
        return n + somme_recursive(n-1)

test =  somme_recursive(3000)
