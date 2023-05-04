from random import randint

def echange(lst,i1,i2):
    lst[i1],lst[i2] = lst[i2],lst[i1]

def melange(lst,ind):
    print(lst)
    if ind>0:
        j=randint(0,ind)
        echange(lst,ind,j)
        melange(lst,ind-1)

def melange_iteratif(lst,ind):
    print(lst)
    while ind>0:
        j=randint(0,ind)
        echange(lst,ind,j)
        ind-=1

lv = [v for v in range(5)]
melange(lv,4)