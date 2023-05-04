#!/usr/bin/python3

import os

for num  in range(1,40):
    snum=str(num).zfill(2)
    os.system(f"mv ./22_NSI_{snum} ./22-NSI-{snum}")

