def separe(liste):
    i = 0
    j = len(liste)-1
    while i<j:
        if liste[i]==0:
            i += 1
        else:
            liste[i],liste[j]=liste[j],liste[i]
            j -= 1
    

liste = [0,1,1,1,0,0,1,0]
separe(liste)
print(liste)