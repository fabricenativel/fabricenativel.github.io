from Crypto.Util import number
from Crypto.Random import get_random_bytes 
from time import time

n_length = 25
p = number.getPrime(n_length,randfunc=get_random_bytes)
q = number.getPrime(n_length,randfunc=get_random_bytes)

print(p,q)

n = p*q

def get_pq(n):
    for f in range(2,n):
        if n%f==0:
            return (f,n//f)
    return None

debut = time()
p,q = get_pq(n)
fin = time()
print(f"Temps d'execution : {fin-debut}")
print(p,q)
