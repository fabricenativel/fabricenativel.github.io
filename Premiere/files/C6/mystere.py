import random

NB_MIN=1
NB_MAX=100

print(f"Choisir un nombre entre {NB_MIN} et {NB_MAX}, je vais tenter de le deviner en vous posant des questions")
debut = NB_MIN
fin = NB_MAX
while fin-debut>0:
    milieu = (fin+debut)//2
    reponse = input(f"Le nombre est-il strictement plus grand que {milieu} ?")
    if reponse=='O':
        debut=milieu+1
    else:
        fin=milieu
print(f"Le nombre était : {debut}")

