import tkinter as tk
from tkinter import filedialog as fd
import csv

root = tk.Tk()
root.withdraw()
filename = fd.askopenfilename()

# ProductNummer=69
# ProductNaam=70
# Aantal=71
# Attribuutnaam=80

newcontent = {'Product': [], 'Barcode': []}

with open(filename) as csvfile:
    csvreader = csv.reader(csvfile, dialect='excel-tab')
    for row in csvreader:
        ## check if 'cm' in 'Attribuutnaam'
        if 'cm' in row[80]:
            ## repeat step for 'Aantal'
            for i in range(eval(row[71])):
                ## check if 'Productnaam' contains '(...)'
                if '(' in row[70]:
                    product = row[70].split('(')[0] + row[80]
                else:
                    product = row[70] + row[80]
                if len(row[80].split('cm')[0]) == 3:
                    barcode = row[69] + ' ' + row[80].split('cm')[0]
                elif len(row[80].split('cm')[0]) == 2:
                    barcode = row[69] + ' 0' + row[80].split('cm')[0]
                else:
                    barcode = 'unknown'
                newcontent['Product'].append(product)
                newcontent['Barcode'].append(barcode)
        else:
            pass
        # product=
        # print(row)
        # print(row[69], row[70], row[71], row[80])

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
