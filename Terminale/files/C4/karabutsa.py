def split(n):
    if int(n)<0:
        n=n[1:]
        s=-1
    else:
        s=1
    m = len(n)//2
    return s*int(n[:m]),s*int(n[m:])
    

def karabutsa(n1,n2):
    print(n1,n2)
    assert type(n1)==int, "Le premier nombre n'est pas entier"
    assert type(n2)==int, "Le second nombre n'est pas entier"
    sn1=str(abs(n1))
    sn2=str(abs(n2))
    l1 = len(str((abs(n1))))
    l2 = len(str((abs(n2))))
    k = max(l1,l2)
    if l1>l2:
        sn2="0"*(l1-l2)+str(n2)
    if l2>l1:
        sn1="0"*(l2-l1)+str(n1)
    if k>1:
        a,b = split(sn1)
        c,d = split(sn2)
        p1 = karabutsa(a,c)
        p2 = karabutsa(a-b,c-d)
        p3 = karabutsa(b,d)
        return p1*10**k+(p1+p3-p2)*10**(k//2)+p3
    else:
        return n1*n2


print(karabutsa(5555,1654))