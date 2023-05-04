from PIL import Image

fuji = Image.open("Mont_Fuji_Message.bmp")
decode = { i : chr(64+i) for i in range(1,27)}
decode[0]=" "
decode["$"]=63

def to_bin(n,size):
    return bin(n)[2:].zfill(size)


def to_dec(bin):
    poids,somme = 1,0
    for i in range(len(bin)-1,-1,-1):
        somme += poids * int(bin[i])
        poids = poids*2
    return somme

def last(n):
    return to_bin(n,2)[-2:]

message = ""
l,c,fin = 0,0,False
while not fin:
    print(f"Pixel en ({l},{c})")
    r,v,b = fuji.getpixel((l,c))
    print(r,v,b)
    code = to_dec(last(r)+last(v)+last(b))
    if code==63:
        fin=True
    else:
        message += decode[code]
        c+=1
        if c>480:
            c=0
            l+=1
print(message)