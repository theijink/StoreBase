'''This application can be used to maintain stock. It should cover the following functionalities:
1. By entering the 'artikelnummer', 'kleurcode', 'aantal meters', 'prijs', 'aantal rol', the program should add this to the database (stock log). By previous log lines in the database, the program should calculate what the stock total is (date independent)
2. On top of point 1, the program should add the proper 'sticker row' to the sticker file. This file is used to create DYNO stickers.
3. By entering 'QR code', the program should reduce the amount of that product with 1.
4. The user should be able to search through the database and see product stock. Both total (date independent) amount and (date dependent) amounts should be shown.
'''

import tkinter as tk
from tkinter import messagebox
import csv
from datetime import datetime as dt
import os
import numpy as np
import time as timeset
from time import sleep

class mainwindow(tk.Tk):
    def __init__(self):
        super().__init__()
        super().geometry('480x240')
        super().title('StoreBase')
        self.textvar=tk.StringVar()
        self.textlab=tk.Label(self, textvariable=self.textvar, justify=tk.LEFT)
        self.textlab.grid(row=0, column=0, sticky='w')
        self.initialize(".bin") ## initialize directory /.bin
        timeset.sleep(pausetime)
        self.textvar.set("")
        self.initialize("stickers") ## initialize directory /stickers
        timeset.sleep(pausetime)
        self.textvar.set("")
        self.initialize("database.csv") ## initialize file databasefilename (/.bin/database.csv)
        timeset.sleep(pausetime)
        self.textvar.set("")
        self.initialize("activity.csv") ## initialize file /.bin/activity.csv
        timeset.sleep(pausetime)
        self.textvar.set("")
        self.initialize("credentialsMapping.csv") ## initialize file /.bin/credentialsMapping.csv
        timeset.sleep(pausetime)
        self.textvar.set("Welcome to StoreBase")
        ## create buttons but don't pack yet
        self.btn1 = tk.Button(self, text="Add Product Item to Database")             
        self.btn2 = tk.Button(self, text="Update Stock Inventory")    
        self.btn3 = tk.Button(self, text="Code & Name Mapping")  
        ## label and button for other, non database related applications           
        self.lab_other_apps = tk.Label(self, text="Other Applications:", font=("Calibri", 12, "bold"), justify=tk.LEFT)
        self.btn4 = tk.Button(self, text="CCV stickers from .csv file")
        self.btn5 = tk.Button(self, text="BOL stickers from .xls file")
        self.btn6 = tk.Button(self, text="postNL stickers form .csv file")

        now = self.startup()                        ## start up after initialisation (login, buttons, etc.)

        
    def initialize(self, target):
        path, dirs, files = next(os.walk('.'))
        if target=="stickers": ## handling /stickers directory
            self.textvar.set(self.textvar.get()+'\n'+'# Checking for stickers directory...')
            self.update()
            timeset.sleep(pausetime)
            if "stickers" in dirs: ## stickers dir is found
                self.textvar.set(self.textvar.get()+'\n'+'# \t...found')
                self.update()
                timeset.sleep(pausetime)
            else: ## stickers dir is found
                self.textvar.set(self.textvar.get()+'\n'+"# \tdirectory stickers not found")
                self.update()
                timeset.sleep(pausetime)
                self.textvar.set(self.textvar.get()+'\n'+"# \tcreating stickers directory...")
                self.update()
                timeset.sleep(pausetime)
                os.mkdir("stickers")
                self.textvar.set(self.textvar.get()+'\n'+"# \t\t...done")
                self.update()
                timeset.sleep(pausetime)
        
        if target==".bin": ## handling /.bin directory
            self.textvar.set(self.textvar.get()+'\n'+'# Checking for .bin directory...')
            self.update()
            timeset.sleep(pausetime)
            if ".bin" in dirs: ## bin file is found
                self.textvar.set(self.textvar.get()+'\n'+'# \t...found')
                self.update()
                timeset.sleep(pausetime)
            else: ## bin file is found
                self.textvar.set(self.textvar.get()+'\n'+"# \tdirectory .bin not found")
                self.update()
                timeset.sleep(pausetime)
                self.textvar.set(self.textvar.get()+'\n'+"# \tcreating .bin directory...")
                self.update()
                os.mkdir(".bin")
                timeset.sleep(pausetime)
                self.textvar.set(self.textvar.get()+'\n'+"# \t\t...done")
                self.update()
                timeset.sleep(pausetime)
        
        if target=="database.csv": ## handling database file
            path, dirs, files = next(os.walk('.bin'))
            self.textvar.set(self.textvar.get()+'\n'+'# Checking for'+databasefilename)
            self.update()
            timeset.sleep(pausetime)
            if "database.csv" in files: ## database is found
                self.textvar.set(self.textvar.get()+'\n'+'# \t...found')
                self.update()
                timeset.sleep(pausetime)
            else: ## database file is found
                self.textvar.set(self.textvar.get()+'\n'+"# \tdirectory database file not found")
                self.update()
                timeset.sleep(pausetime)
                self.textvar.set(self.textvar.get()+'\n'+"# \tcreating database file...")
                self.update()
                timeset.sleep(pausetime)
                file=open(databasefilename, 'w')
                writer=csv.DictWriter(file, fieldnames=database_fieldnames, delimiter=',')
                writer.writeheader()
                file.close()
                self.textvar.set(self.textvar.get()+'\n'+"# \t\t...created")
                self.update()
                timeset.sleep(pausetime)

        if target=="activity.csv": ## handling activity file
            path, dirs, files = next(os.walk('.bin'))
            self.textvar.set(self.textvar.get()+'\n'+'# Checking for '+activityfilename)
            self.update()
            timeset.sleep(pausetime)
            if "activity.csv" in files: ## activity log file is found
                self.textvar.set(self.textvar.get()+'\n'+'# \t...found')
                self.update()
                timeset.sleep(pausetime)
            else: ## activity log file is found
                self.textvar.set(self.textvar.get()+'\n'+"# \tactivity log file not found")
                self.update()
                timeset.sleep(pausetime)
                self.textvar.set(self.textvar.get()+'\n'+"# \tcreating activity log file...")
                self.update()
                timeset.sleep(pausetime)
                file=open(activityfilename, 'w')
                writer=csv.DictWriter(file, fieldnames=activity_fieldnames, delimiter=',')
                writer.writeheader()
                file.close()
                self.textvar.set(self.textvar.get()+'\n'+"# \t\t...created")
                self.update()
                timeset.sleep(pausetime)

        if target=="credentialsMapping.csv": ## handling credentials mapping file
            path, dirs, files = next(os.walk('.bin'))
            self.textvar.set(self.textvar.get()+'\n'+'# Checking for '+mappingfilename)
            self.update()
            timeset.sleep(pausetime)
            if "credentialsMapping.csv" in files: ## credentials mapping file is found
                self.textvar.set(self.textvar.get()+'\n'+'# \t...found')
                self.update()
                timeset.sleep(pausetime)
            else: ## credentials mapping file is found
                self.textvar.set(self.textvar.get()+'\n'+"# \tcredentials mapping file not found")
                self.update()
                timeset.sleep(pausetime)
                self.textvar.set(self.textvar.get()+'\n'+"# \tcreating credentials mapping file...")
                self.update()
                timeset.sleep(pausetime)
                file=open(mappingfilename, 'w')
                writer=csv.DictWriter(file, fieldnames=mapping_fieldnames, delimiter=',')
                writer.writeheader()
                file.close()
                self.textvar.set(self.textvar.get()+'\n'+"# \t\t...created")
                self.update()
                timeset.sleep(pausetime)
    
    def startup(self):
        ## get last activity from reader
        activity=[]
        file=open(activityfilename, 'r')
        reader=csv.DictReader(file)
        for row in reader:
            activity.append(row)
        file.close()
        ## show latest activity in mainwindow
        self.textvar.set(self.textvar.get()+'\nLast login: ')
        try:
            latest=activity[-1]
            self.textvar.set(self.textvar.get()+'\t'+latest['date']+' at '+latest['time'])
        except:
            self.textvar.set(self.textvar.get()+'\tunknown')
        self.update()
        ## add this activity by writer
        activity.append({'date':date, 'time':time})     ## append to activity list
        file=open(activityfilename, 'w')             ## write to file
        writer=csv.DictWriter(file, fieldnames=activity_fieldnames, delimiter=',')
        writer.writeheader()
        for row in activity:
            writer.writerow(row)
        file.close()
        ## create stickerfile
        file=open(stickerfilename, 'w')
        writer=csv.DictWriter(file, fieldnames=stickers_fieldnames, delimiter=',')
        writer.writeheader()
        file.close()
        ## create logfile
        file=open(logfilename, 'w')
        writer=csv.DictWriter(file, fieldnames=logfile_fieldnames, delimiter=',')
        writer.writeheader()
        file.close()
        ## create button for add_to_database
        self.btn1.grid(row=1, column=0, sticky='nsew')
        self.btn1['command']=lambda:database.add_to_database()
        ## create button for update_stock_inventory
        self.btn2.grid(row=2, column=0, sticky='nsew')
        self.btn2['command']=lambda:database.update_stock_inventory()
        ## create button for search_database
        self.btn3.grid(row=4, column=0, sticky='nsew')
        self.btn3['command']=lambda:database.new_credential_mapping()
        ## create label for other applications
        self.lab_other_apps.grid(row=5, column=0, sticky='w')
        self.lab_other_apps['justify']=tk.LEFT
        ## create button for CCV stickers
        self.btn4.grid(row=6, column=0, sticky='nsew')
        self.btn4['state']='disabled'
        ## create buttin for BOL stickers
        self.btn5.grid(row=7, column=0, sticky='nsew')
        self.btn5['state']='disabled'
        ## create button for postNL stickers
        self.btn6.grid(row=8, column=0, sticky='nsew')
        self.btn6['state']='disabled'
        


        

class database():
## popup window functions
    def add_to_database():
        popup=tk.Toplevel(root)
        popup.title("Add New Product Item")
        lab=tk.Label(popup, text="Please enter the credentials and press [Add]")
        lab.grid(row=0, column=0, columnspan=2)
        i=1
        newline={}
        for credential in database_fieldnames:
            newline[credential]=tk.StringVar()
            labi=tk.Label(popup, text=credential)
            labi.grid(row=i, column=0)
            if credential in ['QR code', 'totaal prijs', 'totaal meters']:
                enti=tk.Label(popup, textvariable=newline[credential])
                enti.grid(row=i, column=1)
            else:
                enti=tk.Entry(popup, textvariable=newline[credential])
                enti.grid(row=i, column=1)
            i+=1
        btn=tk.Button(popup, text="Add", command=lambda:[database.write_to_databasefile(newline), [database.write_to_stickerfile(newline, i+1) for i in range(int(newline['aantal rollen'].get()))], infiniteloop.set(False), database.process_database_change(newline, tk.IntVar(value=0), tk.BooleanVar(value=False)), popup.destroy()])
        btn.grid(row=i, column=3)
        ## set the date
        date=dt.now().strftime('%d/%m/%Y')
        newline['datum'].set(date)
        ## update for QR code generation
        data=database.acquire_database_content()
        mapping=database.acquire_mapping_data()
        ## make sure data is not an empty array, otherwise the autofill function doesn't work
        data=data if not data==[] else [newline]
        ## infinite loop
        infiniteloop=tk.BooleanVar(value=True)
        while infiniteloop.get()==True:
            popup.update()
            ## continuousily generate QR code
            QRcode=newline['artikelnummer'].get()+"'"+newline['kleurcode'].get()+"'"+newline['kleur'].get()+"'"+newline['datum'].get()
            newline['QR code'].set(QRcode)
            ## update other parameters if available (when entered 'artikelnummer' and 'kleurcode' are not unique)
            for row in data: ## check if the product item is listed in the database
                if row['artikelnummer']==newline['artikelnummer'].get() and row['kleurcode']==newline['kleurcode'].get():
                    for credential in ['benaming','kleur','aantal meters','aantal op rol']:#,'datum','prijs per meter','totaal prijs','totaal meters','QR code']:
                        newline[credential].set(row[credential])
                else: ## keep checking for the product and color code to map the names
                    for item in mapping:
                        if item['code']==newline['artikelnummer'].get():
                            newline['benaming'].set(item['naam'])
                        if item['code']==newline['kleurcode'].get():
                            newline['kleur'].set(item['naam'])
            #try:
            #    popup.update()
            #except tk.TclError:
            #    break



    def write_to_databasefile(vars):                ## write product with stringvars to database
        newline={}
        for credential in database_fieldnames:
            newline[credential]=vars[credential].get()

        try:                                        ## try to just add the line to the database because this requires less writing
            file=open(databasefilename, 'a')
            writer=csv.DictWriter(file, fieldnames=database_fieldnames)
            writer.writerow(newline)
            file.close()
        except:                                     ## if appending doesn't work the file needs to be overwritten
            data = database.acquire_database_content()
            data.append(newline)
            file=open(databasefilename, 'w')
            writer=csv.DictWriter(file, fieldnames=database_fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
            file.close()



    def update_stock_inventory():
        popup=tk.Toplevel()
        popup.title("Update Stock Inventory")
        lab=tk.Label(popup, text="Please scan the QR code.\nPress [Change Value] to add or substract.")
        lab.grid(row=0, column=0, columnspan=3)
        i=1
        newline={}
        ## place labels for credential name and value
        for credential in database_fieldnames:
            newline[credential]=tk.StringVar()
            labi=tk.Label(popup, text=credential)
            labi.grid(row=i, column=0)
            if credential=='QR code':
                enti=tk.Entry(popup, textvariable=newline[credential])
                enti.grid(row=i, column=1)
            elif credential=='aantal rollen':
                enti=tk.Label(popup, textvariable=newline[credential])
                enti.grid(row=i, column=1)
                btni=tk.Button(popup, text="Change Value", command=lambda:[database.change_database_window(newline), infiniteloop.set(False), popup.destroy()])
                btni.grid(row=i, column=2)  
                btni['state']='disabled'  
            else:
                enti=tk.Label(popup, textvariable=newline[credential])
                enti.grid(row=i, column=1)
            i+=1
        ## update the information for given QR code
        data=database.acquire_database_content()
        mapping=database.acquire_mapping_data()
        infiniteloop=tk.BooleanVar(value=True)
        while infiniteloop.get()==True:
            ## continuousily get QR code from entry field
            QRcode=newline['QR code'].get()
            ## update other parameters if available (when entered 'artikelnummer' and 'kleurcode' are not unique)
            i=0
            for row in data: ## check if the QR code is known and fill in the other fields
                if row['QR code']==newline['QR code'].get():
                    btni['state']='normal'
                    for credential in ['artikelnummer', 'benaming','kleurcode', 'kleur','aantal meters','aantal rollen','aantal op rol','datum','prijs per meter','totaal prijs','totaal meters']:
                        newline[credential].set(str(row[credential]))
                else: ## reset values for unknown QR code
                    pass
                    #btni['state']='disabled'                      
                    #for credential in ['artikelnummer', 'benaming','kleurcode', 'kleur','aantal meters','aantal rollen','aantal op rol','datum','prijs per meter','totaal prijs','totaal meters']:
                    #    newline[credential].set("")
            popup.update()                
                  



    def search_database():
        popup=tk.Toplevel()
        popup.title("Search Database")
        lab=tk.Label(popup, text="test")
## below the actual writing functions

    def change_database_window(product): ## window for entering the change in quantity
        popupup=tk.Toplevel()
        popupup.title("Quantity")
        ## create label and entry for quantity values
        i=0
        lab1=tk.Label(popupup, text="Add or Substract Stock Inventory for Product:")
        lab1.grid(row=i, column=0, columnspan=2)
        i+=1
        ## create labels for product credentials
        for credential in ['artikelnummer', 'benaming', 'kleurcode', 'kleur']:
            lab1=tk.Label(popupup, text=credential+': ', justify=tk.RIGHT)
            lab1.grid(row=i, column=0)
            lab2=tk.Label(popupup, text=product[credential].get(), justify=tk.LEFT)
            lab2.grid(row=i, column=1)
            i+=1
        ## create entry for quantity
        lab=tk.Label(popupup, text="Enter quantity to add.\nUse negative value to substract")
        lab.grid(row=i, column=0)
        change_value=qty_to_change=tk.IntVar()
        ent=tk.Entry(popupup, textvariable=change_value)
        ent.grid(row=i, column=1)
        i+=1
        ## create checkbutton for sticker creation
        check_print_stickers=tk.IntVar(value=1)
        cbx=tk.Checkbutton(popupup, text="Print stickers", variable=check_print_stickers)
        cbx.grid(row=i, column=2)
        i+=1
        ## create button for confirmation
        btn=tk.Button(popupup, text="Confirm", command=lambda:[database.process_database_change(product, change_value, check_print_stickers), popupup.destroy()])
        btn.grid(row=i, column=2)
    
    def process_database_change(line, change_value, check_print_stickers):
        ## obtain values from popupup window where this is entered
        val=change_value.get()
        prt=check_print_stickers.get()
        product={}
        for credential in line:
            product[credential]=line[credential].get()
        ## update the values of product credentials 'aantal rollen', 'totaal prijs', 'totaal meters'
        product['aantal rollen']=str(int(product['aantal rollen'])+val)
        product['totaal meters']=str(int(product['aantal meters'])*int(product['aantal rollen']))
        product['totaal prijs']=str(float(product['prijs per meter'])*int(product['aantal rollen']))
        ## show warning if stock inventory is less than one
        if int(product['aantal rollen'])<=0:                
            messagebox.showwarning(title="Stock Inventory Warning", message="The current stock inventory for this product item is {}".format(product['aantal rollen']))
        ## send correct amount of stickers
        if val>0:
            for i in range(1, val+1):
                database.write_to_stickerfile(product, i)
        ## update the value in database
        data=database.acquire_database_content()
        for row in data:
            if row['QR code']==product['QR code']:          ## if the QR code is known in the database
                for credential in row:
                    row[credential]=product[credential]     ## overwrite the existing line with the updated line
            elif row==data[-1]:                             ## if the QR code is not known in the database
                data.append(product)                        ## add the row to the database
        ## the complete file needs to be rewritten because of the changes made
        file=open(databasefilename, 'w') 
        writer=csv.DictWriter(file, delimiter=',', fieldnames=database_fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
        file.close()
        ## recalculate totals 
        database.recalculate()

    def recalculate():
        ## read database file
        data=[]
        file=open(databasefilename, 'r')
        reader=csv.DictReader(file, delimiter=',')
        for row in reader:
            data.append(row)
        file.close()
        ## check for rows with matching artikelnummer en kleurcode
        for product in data:
            ## check for doubles in the database
            doubles=[]
            for check in data:
                if product['artikelnummer']==check['artikelnummer'] and product['kleurcode']==check['kleurcode']:
                    doubles.append(check)
            ## get the latest price per meter:
            price_per_meter={'datum':'', 'prijs':''}
            totaal_aantal=0
            for item in doubles:
                totaal_aantal+=eval(item['aantal rollen'])
                if item['datum']>=price_per_meter['datum']:
                    price_per_meter['datum']=item['datum']
                    price_per_meter['prijs']=item['prijs per meter']
            ## recalculate totaal aantal and totaal prijs
            prijs_per_meter=price_per_meter['prijs'] if type(price_per_meter['prijs'])==type(0) else eval(price_per_meter['prijs'])
            totaal_prijs=totaal_aantal*eval(product['aantal meters'])*prijs_per_meter
            product['prijs per meter']=prijs_per_meter
            product['totaal meters']=totaal_aantal*eval(product['aantal meters'])
            product['totaal prijs']=totaal_prijs
        ## write updated products to database
        file=open(databasefilename, 'w')
        writer=csv.DictWriter(file, fieldnames=database_fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
        file.close()
        


    def acquire_stickerfile_content():
        data=[]
        file=open(stickerfilename, 'r')
        reader=csv.DictReader(file, delimiter=',')
        for row in reader:
            data.append(row)
        file.close()
        return data        

    def acquire_database_content():
        data = []
        file=open(databasefilename, 'r')
        reader=csv.DictReader(file, delimiter=',')
        for row in reader:
            data.append(row)
        file.close()
        return data

    def acquire_mapping_data():
        data = []
        file=open(mappingfilename, 'r')
        reader=csv.DictReader(file, delimiter=',')
        for row in reader:
            data.append(row)
        file.close()
        return data      
  
    def new_credential_mapping():
        popup=tk.Toplevel()
        popup.title("Add new Code")
        i=0
        lab1=tk.Label(popup, text="Code")
        lab1.grid(row=i, column=0)
        lab2=tk.Label(popup, text="Name")
        lab2.grid(row=i, column=1)
        i+=1
        code=tk.StringVar()
        ent1=tk.Entry(popup, textvariable=code)
        ent1.grid(row=i, column=0)
        name=tk.StringVar()
        ent2=tk.Entry(popup, textvariable=name)
        ent2.grid(row=i, column=1)
        i+=1
        btn=tk.Button(popup, text="Add to File", command=lambda:[database.add_credential_to_file(code, name), popup.destroy()])
        btn.grid(row=i, column=2)

    def add_credential_to_file(code, name):
        newmap={
            'code':code.get(),
            'naam':name.get()
        }
        code.set("")
        name.set("")
        mapping=database.acquire_mapping_data()
        if len(mapping)>0:
            for item in mapping:
                if item['code']==newmap['code']:    ## if the code already exists in the list a warning is shown
                    messagebox.showwarning(title="Code Duplication", message="The code {} is already used by the name {}".format(item['code'], item['naam']))
                elif item==mapping[-1]:             ## latest item and none of them was identical so add the new item to the list
                    file=open(mappingfilename, 'a')
                    writer=csv.DictWriter(file, fieldnames=mapping_fieldnames)
                    writer.writerow(newmap)
                    file.close()
        else:                                       ## in case the credentials file is empty
            file=open(mappingfilename, 'a')
            writer=csv.DictWriter(file, fieldnames=mapping_fieldnames)
            writer.writerow(newmap)
            file.close()

    def write_to_stickerfile(product, i):
        ## fix the sticker format from database format
        try:                                        ## in case <product> still contains stringvars
            newsticker={
                'artikelnummer':product['artikelnummer'].get(),
                'kleurcode':product['kleurcode'].get(),
                'benaming':product['benaming'].get(),
                'benaming kleur':product['kleur'].get(),
                'hoeveelheid per rol':product['aantal op rol'].get(),
                'datum':product['datum'].get(), 
                'aantal rollen':str(i)+'/'+product['aantal rollen'].get(),
                'QR code':product['QR code'].get()
            }            
        except:                                     ## in case <product> contains just strings
            newsticker={
                'artikelnummer':product['artikelnummer'],
                'kleurcode':product['kleurcode'],
                'benaming':product['benaming'],
                'benaming kleur':product['kleur'],
                'hoeveelheid per rol':product['aantal op rol'],
                'datum':product['datum'], 
                'aantal rollen':str(i)+'/'+product['aantal rollen'],
                'QR code':product['QR code']
            }
        ## add the new line to the sticker file
        try:                                        ## try to just add the line to the sticker file because this requires less writing
            file=open(stickerfilename, 'a')
            writer=csv.DictWriter(file, fieldnames=stickers_fieldnames)
            writer.writerow(newsticker)
            file.close()
        except:                                     ## if appending doesn't work the file needs to be overwritten
            data = database.acquire_stickerfile_content()
            data.append(newsticker)
            file=open(stickerfilename, 'w')
            writer=csv.DictWriter(file, fieldnames=stickers_fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
            file.close()



if __name__=='__main__':
    ## settings
    pausetime=0.01
    ## parameters
    now = dt.now()                                  ## get current date and time
    date = now.strftime("%Y/%m/%d")                 ## take only date values
    time = now.strftime("%H:%M:%S")                 ## take only time values
    unique_filename=str(now)                        ## create unique ID for files based on date and time
    ## files headers
    database_fieldnames=['artikelnummer','benaming','kleurcode','kleur','aantal meters','aantal rollen','aantal op rol','datum','prijs per meter','totaal prijs','totaal meters','QR code']
    stickers_fieldnames=['artikelnummer', 'kleurcode', 'benaming', 'benaming kleur', 'hoeveelheid per rol', 'datum', 'aantal rollen', 'QR code']
    logfile_fieldnames=['ReportCode', 'Message']
    activity_fieldnames=["date", "time"]
    mapping_fieldnames=['code', 'naam']
    ## files names
    stickerfilename="1.csv"#"stickers/"+unique_filename+".csv"
    databasefilename=".bin/database.csv"
    activityfilename=".bin/activity.csv"
    mappingfilename=".bin/credentialsMapping.csv"
    logfilename=".bin/"+unique_filename+".csv"
    ## main application 
    root=mainwindow()
    root.mainloop()
