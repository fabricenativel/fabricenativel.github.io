import csv
import matplotlib.pyplot as plt
from math import sqrt


FICHIER = "countries_ext.csv"

def get_data(fichier):
    with open(fichier,"r",encoding="utf-8") as f:
        data=list(csv.DictReader(f,delimiter=","))
    return data

def get_xy(data,gdp):
    x = [float(d['Population']) for d in data if d['Richesse']==gdp]
    y = [float(d['Area']) for d in data if d['Richesse']==gdp]
    return x,y

def distance(x1,y1,x2,y2):
    return sqrt((x1-x2)**2+(y1-y2)**2)

def ldistance(x,y,data,k):
    ld = [(distance(x,y,float(d["Population"]),float(d["Area"])),d["Richesse"],d['Country']) for d in data]
    ld = sorted(ld,key = lambda x : x[0])
    return ld[:k]




pays = get_data(FICHIER)

print(ldistance(60876136,547030,pays,12))

xr,yr = get_xy(pays,"Elevée")
xm,ym = get_xy(pays,"Moyenne")
xp,yp = get_xy(pays,"Faible")
plt.scatter(xr,yr,label='Riche',color='red')
plt.scatter(xm,ym,label='Moyenne',color='blue')
plt.scatter(xp,yp,label='Pauvre',color='green')
plt.legend()
plt.show()
