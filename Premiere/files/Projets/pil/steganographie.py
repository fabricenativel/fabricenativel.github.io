from PIL import Image

fuji = Image.open("Mont_Fuji.jpg")
code = { chr(64+i) : i for i in range(1,27)}
code[" "]=0
code["$"]=63

def to_bin(n,size):
    return bin(n)[2:].zfill(size)


def to_dec(bin):
    poids,somme = 1,0
    for i in range(len(bin)-1,-1,-1):
        somme += poids * int(bin[i])
        poids = poids*2
    return somme


to_encode = "FELICITATIONS CETTE PARTIE DU PROJET ETAIT VRAIMENT DIFFICILE ET TU AS REUSSI CONTINUE SUR CETTE VOIE ET TU DEVIENDRAS SANS DOUTE UN EXCELLENT PROGRAMMEUR$"
for i in range(len(to_encode)):
    print(f"Encodage du {to_encode[i]} en (0,{i})")
    r,v,b = fuji.getpixel((0,i))
    print(f"Valeur actuelle du pixel : ({r},{v},{b})")
    code_bin = to_bin(code[to_encode[i]],6)
    print(f"Encodage du {to_encode[i]} = {code_bin}")
    dr,dv,db = code_bin[0:2],code_bin[2:4],code_bin[4:6]
    nr,nv,nb =  to_dec(to_bin(r,8)[0:6]+dr),to_dec(to_bin(v,8)[0:6]+dv),to_dec(to_bin(b,8)[0:6]+db)
    print(f"Valeur modifiée du pixel : ({nr},{nv},{nb})")
    fuji.putpixel((0,i),(int(nr),int(nv),int(nb)))

fuji.save("Mont_Fuji_Message.bmp")
