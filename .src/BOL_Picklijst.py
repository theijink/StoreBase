import tkinter as tk
from tkinter import filedialog as fd
import csv

filename = fd.askopenfilename()
fileout = filename.split('.')[0] + '_order.csv'

data = []
file = open(filename, 'r')
reader = csv.DictReader(file, delimiter=';')
for line in reader:
    data.append(line)
file.close()

selectie = []
set = set()
for row in data:
    if row['\ufeffbestelnummer'] in set:
        newline = {
            'bestelnummer': '',
            'voornaam': '',
            'achternaam': '',
            'ref.': row['referentie'],
            'aantal': row['aantal'],
            'alert': '!!' if eval(row['aantal']) > 1 else '',
            'producttitel': row['producttitel'],
        }
    else:
        newline = {
            'bestelnummer': row['\ufeffbestelnummer'],
            'voornaam': row['voornaam_verzending'],
            'achternaam': row['achternaam_verzending'],
            'ref.': row['referentie'],
            'aantal': row['aantal'],
            'alert': '!!!!!!!' if eval(row['aantal']) > 1 else '',
            'producttitel': row['producttitel'],
        }
    set.add(row['\ufeffbestelnummer'])
    selectie.append(newline)

file = open(fileout, 'w')
writer = csv.DictWriter(file, delimiter=';', fieldnames=[i for i in selectie[0]])
writer.writeheader()
for row in selectie:
    writer.writerow(row)
file.close()


