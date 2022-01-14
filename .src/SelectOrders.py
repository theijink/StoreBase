import tkinter as tk
from tkinter import filedialog
import csv

tk.Tk().withdraw()
filename = filedialog.askopenfilename()
fileout = filename.split('.')[0]+'_order.csv'

data = []
file = open(filename, 'r')
reader = csv.DictReader(file, delimiter=';')
for line in reader:
    data.append(line)
file.close()

selectie=[]
set=set()
for row in data:
    if row['bestelnummer'] in set:
        newline={
            'bestelnummer':'',
            'voornaam_verzending':'',
            'achternaam_verzending':'',
            'referentie':row['referentie'],
            'producttitel':row['producttitel'],
            'aantal':row['aantal'],
            'alert':'!!' if eval(row['aantal'])>1 else ''
        }
    else:        
        newline={
            'bestelnummer':row['bestelnummer'],
            'voornaam_verzending':row['voornaam_verzending'],
            'achternaam_verzending':row['achternaam_verzending'],
            'referentie':row['referentie'],
            'producttitel':row['producttitel'],
            'aantal':row['aantal'],
            'alert':'!!' if eval(row['aantal'])>1 else ''
        }
    set.add(row['bestelnummer'])
    selectie.append(newline)

file = open(fileout, 'w')
writer = csv.DictWriter(file, delimiter=';', fieldnames=[i for i in selectie[0]])
writer.writeheader()
for row in selectie:
    writer.writerow(row)
file.close()
    

