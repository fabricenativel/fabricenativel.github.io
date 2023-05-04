from PIL import Image

def partage_quart(image):
    n = image.width
    if n > 1:
        q1 = image.crop((0,0,n//2,n//2))
        q2 = image.crop((n//2,0,n,n//2))
        q3 = image.crop((0,n//2,n//2,n))
        q4 = image.crop((n//2,n//2,n,n))
        return q1,q2,q3,q4

def quart_tour(image):
    n = image.width
    # Partage de l'image en quatre quarts
    if n>1:
        q1,q2,q3,q4 = partage_quart(image)
        # Rotation de chacun des quarts
        rq1 = quart_tour(q1)
        rq2 = quart_tour(q2)
        rq3 = quart_tour(q3)
        rq4 = quart_tour(q4)
        # Reconstruction de l'image
        resultat = Image.new('RGB',image.size)
        resultat.paste(rq2,(0,0))
        resultat.paste(rq4,(n//2,0))
        resultat.paste(rq1,(0,n//2))
        resultat.paste(rq3,(n//2,n//2))
        return resultat
    else:
        return image
    

img_test = Image.open("/home/fenarius/Travail/Cours/Terminale/docs/files/C4/Jess.jpg")
rimage_test=quart_tour(img_test)
rimage_test.show()