from math import floor, log10

def nb_chiffres(n):
    if n>0:
        return floor(log10(n))+1
    else:
        return 1

def split(n):
    s=n//abs(n)
    if abs(n)>9:
        nbc = nb_chiffres((abs(n)))
        n1 = int(abs(n)/10**(nbc//2))
        return n1,n-n1*10**(nbc//2)
    else:
        return 0,s*n

def karabutsa(n1,n2):
    assert type(n1)==int, "Le premier nombre n'est pas entier"
    assert type(n2)==int, "Le second nombre n'est pas entier"
    k =max(nb_chiffres(n1),nb_chiffres(n2))
    if k>1:
        a,b = split(n1)
        c,d = split(n2)
        p1 = karabutsa(a,c)
        p2 = karabutsa(a-b,c-d)
        p3 = karabutsa(b,d)
        return p1*10**k+(p1+p3-p2)*10**(k//2)+p3
    else:
        return n1*n2


print(karabutsa(1237,2587))