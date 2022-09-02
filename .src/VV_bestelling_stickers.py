import tkinter as tk
from tkinter import filedialog as fd
import csv

root = tk.Tk()
root.withdraw()
filename = fd.askopenfilename()

# ProductNummer=69
# ProductNaam=70
# Aantal=71

newcontent = {'Product': [], 'Barcode': []}

with open(filename) as csvfile:
    csvreader = csv.reader(csvfile, dialect='excel-tab')
    for row in csvreader:
        if row[71] == 'Aantal':
            pass
        else:
            ## repeat step for 'Aantal'
            for i in range(eval(row[71])):
                product = row[70]
                if 'Yourlaces' in row[70]:
                    product = row[70].replace('Yourlaces', '')
                barcode = row[69]

                newcontent['Product'].append(product)
                newcontent['Barcode'].append(barcode)

[print(p, b) for p, b in zip(newcontent['Product'], newcontent['Barcode'])]

newcsv = filename.split('.csv')[0] + "_stickers.csv"
with open(newcsv, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['Product', 'Barcode'])
    writer.writeheader()
    [writer.writerow({'Product': p, 'Barcode': b}) for p, b in zip(newcontent['Product'], newcontent['Barcode'])]

    # for p,b in zip(newcontent['Product'],newcontent['Barcode']):
    #    writer.writerow([p,b])

# Productnaam - () + Attribuutnaam
# prodcutnummer + attribuutnummer-"cm"
