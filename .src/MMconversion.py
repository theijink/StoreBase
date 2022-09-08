import sys
import tkinter as tk
from tkinter.filedialog import askopenfilename
from parameters import *
from generic import *
import csv


class Window(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        super().geometry()
        self.wm_title('MisterMinit')
        self.data=self.load_csv()
        for ordernumber in self.data:
            self.write_xml(ordernumber, self.data)
        self.set_widgets()

    def get_code(self, attribuutnaam):
        lengte=eval(attribuutnaam[:-2])
        codes=codesMisterMinit
        code='@@@'
        for c in codes:
            if lengte>=codes[c][0] and lengte<=codes[c][1]:
                code=c
        return code

    def load_csv(self):
        try:
            filename='test/testdata/Export_redcsv.csv' #defaultFilenameMisterMinit
            file=open(filename, 'r')
            log_to_suitelogfile('warning', 'Default file {} not found. File dialog will be opened.'.format(filename), dt.now(tz.utc))
        except Exception as e:
            filename=askopenfilename(filetypes=[("Comma Separated Files","*.csv")], initialdir='.')
            file=open(filename, 'r')
        self.filename=filename
        self.filepath="".join([i+'/' for i in filename.split('/')[:-1]])
        data=[]
        data_per_order={}
        reader=csv.DictReader(file, delimiter='\t')
        for row in reader:
            data.append(row)
            data_per_order[row['Ordernummer']]={"CreationDate":row['Datum'].replace('-', '/'), "UnitPrice":[], "Quantity":[], "NavisionCode":[], "PurchPrice":[], "ShopNumber":row['Referentie']}
        for item in data:
            data_per_order[item['Ordernummer']]["UnitPrice"].append(item['Prijs'])
            data_per_order[item['Ordernummer']]["Quantity"].append(item['Aantal'])
            data_per_order[item['Ordernummer']]["NavisionCode"].append(self.get_code(item['Attribuutnaam']))
            data_per_order[item['Ordernummer']]["PurchPrice"].append(item['Totale prijs'])
        file.close()
        return data_per_order

    def write_xml(self, ordernumber, data):
        self.xmlfile="{}/{}.xml".format(self.filepath, ordernumber)
        file=open(self.xmlfile, 'w')
        file.write('<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>\n')
        [yyyy, mm, dd] = data[ordernumber]['CreationDate'].split (' ')[0].split('/')
        time = data[ordernumber]['CreationDate'].split(' ')[1]
        file.write('<Order ID="{}" CreationDate="{}">\n'.format(ordernumber, dd+'/'+mm+'/'+yyyy+' '+time))
        file.write('\t<OrderItems>\n')
        for i in range(len(data[ordernumber]['UnitPrice'])):
            file.write('\t\t<OrderItem UnitPrice="{}" Quantity="{}" NavisionCode="{}" PurchPrice="{}" />\n'.format(data[ordernumber]['UnitPrice'][i], data[ordernumber]['Quantity'][i], data[ordernumber]['NavisionCode'][i], data[ordernumber]['PurchPrice'][i]))
        file.write('\t</OrderItems>\n')
        file.write('\t<User ShopNumber="{}" />\n'.format(data[ordernumber]['ShopNumber']))
        file.write('</Order>\n')
        file.close()
        log_to_suitelogfile('info', 'Converted file {} into {} using {}.'.format(self.filename, self.xmlfile, sys.argv[0]), dt.now(tz.utc))

    def set_widgets(self):
        i,j=1,0
        for item in self.data:
            colnames = [i for i in self.data[item].keys()]
            j=0
            for attr in self.data[item]:
                tk.Label(text=attr).grid(row=i,column=j)
                j+=1
                #columns = [k for k in self.data[item[ordernumber]].keys()]
                #for attr in item[ordernumber]:
                #    tk.Label(text=self.data[item[ordernumber]][attr]).grid(row=i, column=j, sticky='nsew')
                #    j+=1
        self.update()



if __name__=="__main__":
    root=Window()
    root.mainloop()

