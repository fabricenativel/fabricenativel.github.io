#!/usr/bin/python3

import os

for num  in range(1,30):
    snum=str(num).zfill(2)
    os.system(f"mv ./21-NSI-{snum}/21_NSI_{snum}.pdf ./21-NSI-{snum}/21-NSI-{snum}.pdf ")

