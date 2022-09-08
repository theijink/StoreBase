from generic import load_xls, log_to_suitelogfile
from fileinput import filename
import tkinter as tk
from tkinter import filedialog as fd
import csv
import pandas as pd

data, filename = load_xls()
fileout = filename[:-4]+'_out.csv'

selectie = []
set = set()
for row in data:
    if row['bestelnummer'] in set:
        newline = {
            'bestelnummer': '',
            'voornaam': '',
            'achternaam': '',
            'ref.': row['referentie'],
            'aantal': row['aantal'],
            'alert': '!!' if eval(str(row['aantal'])) > 1 else '',
            'producttitel': row['producttitel'],
        }
    else:
        newline = {
            'bestelnummer': row['bestelnummer'],
            'voornaam': row['voornaam_verzending'],
            'achternaam': row['achternaam_verzending'],
            'ref.': row['referentie'],
            'aantal': row['aantal'],
            'alert': '!!' if eval(str(row['aantal'])) > 1 else '',
            'producttitel': row['producttitel'],
        }
    set.add(row['bestelnummer'])
    selectie.append(newline)

file = open(fileout, 'w')
writer = csv.DictWriter(file, delimiter=';', fieldnames=[i for i in selectie[0]])
writer.writeheader()
for row in selectie:
    writer.writerow(row)
file.close()
log_to_suitelogfile('info', 'Used BOL_Picklijst.py to write pack list for {} orders: {}.'.format(len(selectie), filename), dt.now(tz.utc))

