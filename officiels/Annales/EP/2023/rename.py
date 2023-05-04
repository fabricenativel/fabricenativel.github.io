#!/usr/bin/python3

import os

for num  in range(1,46):
    snum=str(num).zfill(2)
    os.system(f"mkdir 23-NSI-{snum}")
    os.system(f"mv {snum}.pdf ./23-NSI-{snum}/23-NSI-{snum}.pdf")
    os.system(f"mv {snum}.py ./23-NSI-{snum}/23-NSI-{snum}.py")
    

