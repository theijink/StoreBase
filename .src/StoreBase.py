from time import sleep
from parameters import *
import tkinter as tk
from tkinter import messagebox
from datetime import datetime as dt
from datetime import timezone as tz
import csv
import sys

class mainwindow(tk.Tk):
    def __init__(self, mode):
        super().__init__()
        super().geometry()
        self.mode=mode
        self.add_widgets(self.mode)
        self.updateloop(self.mode)
    
    def add_widgets(self, mode):
        if mode=='DBadd':
            self.wm_title("Add Item to DataBase")
            self.newline={}
            lab=tk.Label(self, text="Please enter the credentials and press [Add]")
            lab.grid(row=0, column=0, columnspan=2)
            i=1
            for credential in databasefileheader:
                self.newline[credential]=tk.StringVar()
                labi=tk.Label(self, text=credential)
                labi.grid(row=i, column=0)
                if credential in databaseNotAdjustable:
                    enti=tk.Label(self, textvariable=self.newline[credential])
                    enti.grid(row=i, column=1)
                else:
                    enti=tk.Entry(self, textvariable=self.newline[credential])
                    enti.grid(row=i, column=1)
                i+=1
            btn=tk.Button(self, text="Add", command=lambda:[self.add_newline()])
            btn.grid(row=i, column=3)
            ## autofill for test purposes
            if usePrefilledEntries==True:
                for credential in self.newline:
                    print(self.newline[credential].get())
                    if self.newline[credential].get()=='' and not credential in databaseNotAdjustable:
                        self.newline[credential].set(str(prefill(credential)))
        elif mode=='DBmod':
            self.wm_title("Change Item in DataBase")
            self.newline={}
            i=1
            ## place labels for credential name and value
            for credential in databasefileheader:
                self.newline[credential]=tk.StringVar()
                labi=tk.Label(self, text=credential)
                labi.grid(row=i, column=0)
                if credential=='QR code':
                    enti=tk.Entry(self, textvariable=self.newline[credential])
                    enti.grid(row=i, column=1)
                elif credential=='aantal rollen':
                    enti=tk.Label(self, textvariable=self.newline[credential])
                    enti.grid(row=i, column=1)
                    self.btni=tk.Button(self, text="Change Value", command=lambda:[self.modify_database()])
                    self.btni.grid(row=i, column=2)  
                    self.btni['state']='disabled' 
                else:
                    enti=tk.Label(self, textvariable=self.newline[credential])
                    enti.grid(row=i, column=1)
                i+=1
            ## autofill for test purposes
            if usePrefilledEntries==False:
                for credential in self.newline:
                    if self.newline[credential].get()=='' and not credential in databaseNotAdjustable:
                        self.newline[credential].set(prefill(credential))
        elif mode=='DBmap':
            self.wm_title("Add code-name mapping")
            self.mapping={}    
            i=0
            for credential in credentialsfileheader:
                self.mapping[credential]=tk.StringVar()
                labi=tk.Label(self, text=credential)
                labi.grid(row=i, column=0)
                enti=tk.Entry(self, textvariable=self.mapping[credential])
                enti.grid(row=i, column=1)
                i+=1
            btn=tk.Button(self, text="Add to File", command=lambda:[self.add_credential()])
            btn.grid(row=i, column=2)
            ## autofill for test purposes
            if usePrefilledEntries==True:
                for credential in self.mapping:
                    if self.mapping[credential].get()=='' and not credential in databaseNotAdjustable:
                        self.mapping[credential].set(prefill(credential))
        else:
            self.destroy()

    def modify_database(self):
        self.change_database_window(self.newline)
        self.recalculate()
        self.infiniteloop.set(False) 
        self.destroy()

    def add_newline(self):
        self.write_to_databasefile(self.newline)
        self.update_credentials_mapping(self.newline)
        [self.write_to_stickerfile(self.newline, i+1) for i in range(int(self.newline['aantal rollen'].get()))]
        #self.process_database_change(self.newline, tk.IntVar(value=0), tk.BooleanVar(value=False))
        self.recalculate()
        self.infiniteloop.set(False)
        self.destroy()

    def add_credential(self):
        self.add_credential_to_file(self.mapping['code'], self.mapping['naam'], popup=True)
        self.destroy()

    def updateloop(self, mode):
        if mode=='DBadd':
            ## set the date
            date=dt.now().strftime('%d/%m/%Y')
            self.newline['datum'].set(date)
            ## update for QR code generation
            data=self.acquire_database_content()
            mapping=self.acquire_mapping_data()
            ## make sure data is not an empty array, otherwise the autofill function doesn't work
            data=data if not data==[] else [self.newline]
            ## infinite loop
            self.infiniteloop=tk.BooleanVar(value=True)
            while self.infiniteloop.get()==True:
                self.update()
                ## continuousily generate QR code
                QRcode=self.newline['artikelnummer'].get()+"'"+self.newline['kleurcode'].get()+"'"+self.newline['kleur'].get()+"'"+self.newline['datum'].get()
                self.newline['QR code'].set(QRcode)
                ## update other parameters if available (when entered 'artikelnummer' and 'kleurcode' are not unique)
                for row in data: ## check if the product item is listed in the database
                    if row['artikelnummer']==self.newline['artikelnummer'].get() and row['kleurcode']==self.newline['kleurcode'].get():
                        for credential in ['benaming','kleur','aantal meters','aantal op rol']:#,'datum','prijs per meter','totaal prijs','totaal meters','QR code']:
                            self.newline[credential].set(row[credential])
                    else: ## keep checking for the product and color code to map the names
                        for item in mapping:
                            if item['code']==self.newline['artikelnummer'].get():
                                self.newline['benaming'].set(item['naam'])
                            if item['code']==self.newline['kleurcode'].get():
                                self.newline['kleur'].set(item['naam'])
        elif mode=='DBmod':
            ## update the information for given QR code
            data=self.acquire_database_content()
            mapping=self.acquire_mapping_data()
            self.infiniteloop=tk.BooleanVar(value=True)
            while self.infiniteloop.get()==True:
                self.update()
                ## continuousily get QR code from entry field
                QRcode=self.newline['QR code'].get()
                ## update other parameters if available (when entered 'artikelnummer' and 'kleurcode' are not unique)
                i=0
                for row in data: ## check if the QR code is known and fill in the other fields
                    if row['QR code']==self.newline['QR code'].get():
                        self.btni['state']='normal'
                        self.update()
                        for credential in ['artikelnummer', 'benaming','kleurcode', 'kleur','aantal meters','aantal rollen','aantal op rol','datum','prijs per meter','totaal prijs','totaal meters']:
                            self.newline[credential].set(str(row[credential]))
                    else: ## reset values for unknown QR code
                        self.btni['state']='disabled'    
                        self.update()                  
                        for credential in ['artikelnummer', 'benaming','kleurcode', 'kleur','aantal meters','aantal rollen','aantal op rol','datum','prijs per meter','totaal prijs','totaal meters']:
                            self.newline[credential].set("")
        elif mode=='DBmap':
            pass
        else:
            self.destroy()
            
    def change_database_window(self, product):
        popup=tk.Toplevel()
        popup.title("Quantity")
         ## create label and entry for quantity values
        i=0
        lab1=tk.Label(popup, text="Add or Substract Stock Inventory for Product:")
        lab1.grid(row=i, column=0, columnspan=2)
        i+=1
        ## create labels for product credentials
        for credential in ['artikelnummer', 'benaming', 'kleurcode', 'kleur']:
            lab1=tk.Label(popup, text=credential+': ', justify=tk.RIGHT)
            lab1.grid(row=i, column=0)
            lab2=tk.Label(popup, text=product[credential].get(), justify=tk.LEFT)
            lab2.grid(row=i, column=1)
            i+=1
        ## create entry for quantity
        lab=tk.Label(popup, text="Enter quantity to add.\nUse negative value to substract")
        lab.grid(row=i, column=0)
        change_value=qty_to_change=tk.IntVar()
        ent=tk.Entry(popup, textvariable=change_value)
        ent.grid(row=i, column=1)
        i+=1
        ## create checkbutton for sticker creation
        check_print_stickers=tk.IntVar(value=1)
        cbx=tk.Checkbutton(popup, text="Print stickers", variable=check_print_stickers)
        cbx.grid(row=i, column=2)
        i+=1
        ## create button for confirmation
        btn=tk.Button(popup, text="Confirm", command=lambda:[self.process_database_change(product, change_value, check_print_stickers), popup.destroy()])
        btn.grid(row=i, column=2)       

        
    def acquire_database_content(self):
        data = []
        file=open(databasefilename, 'r')
        reader=csv.DictReader(file, delimiter=',')
        for row in reader:
            data.append(row)
        file.close()
        return data
    
    def acquire_mapping_data(self):
        data = []
        file=open(credentialsfilename, 'r')
        reader=csv.DictReader(file, delimiter=',')
        for row in reader:
            data.append(row)
        file.close()
        return data 
    
    def update_credentials_mapping(self, vars):
        for code,name in zip([vars['artikelnummer'], vars['kleurcode']], [vars['benaming'], vars['kleur']]):
            self.add_credential_to_file(code, name, popup=False)


    def write_to_databasefile(self, vars):
        ## write product with stringvars to database
        newline={}
        ## get values from stringvars
        for credential in databasefileheader:
            newline[credential]=vars[credential].get()
        ## try to just add the line to the database because this requires less writing
        try:                                        
            file=open(databasefilename, 'a')
            writer=csv.DictWriter(file, fieldnames=databasefileheader)
            writer.writerow(newline)
            file.close()
            self.log_to_suitelogfile('info', 'Updated stock with {} items for product {}'.format(newline['aantal rollen'], newline['QR code']), dt.now(tz.utc))
        ## if appending doesn't work the file needs to be overwritten
        except:
            data = self.acquire_database_content()
            data.append(newline)
            file=open(databasefilename, 'w')
            writer=csv.DictWriter(file, fieldnames=databasefileheader)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
            file.close()
            self.log_to_suitelogfile('info', 'Updated stock with {} items for product {}.'.format(newline['aantal rollen'], newline['QR code']), dt.now(tz.utc))
            self.log_to_suitelogfile('warning', 'Unable to append to {} so file is re-written.'.format(databasefilename), dt.now(tz.utc))


    def write_to_stickerfile(self, product, i):
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
            writer=csv.DictWriter(file, fieldnames=stickerfileheader)
            writer.writerow(newsticker)
            file.close()
            self.log_to_suitelogfile('info', 'Wrote {} stickers to file for product {}'.format(newsticker['aantal rollen'], newsticker['QR code']), dt.now(tz.utc))
        except:                                     ## if appending doesn't work the file needs to be overwritten
            data = self.acquire_stickerfile_content()
            data.append(newsticker)
            file=open(stickerfilename, 'w')
            writer=csv.DictWriter(file, fieldnames=stickerfileheader)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
            file.close()
            self.log_to_suitelogfile('info', 'Wrote {} stickers to file for product {}'.format(newsticker['aantal rollen'], newsticker['QR code']), dt.now(tz.utc))
            self.log_to_suitelogfile('warning', 'Unable to append to {} so file is re-written.'.format(stickerfilename), dt.now(tz.utc))
    
    def add_credential_to_file(self, code, name, popup=True):
        newmap={
            'code':code.get(),
            'naam':name.get()
        }
        code.set("")
        name.set("")
        mapping=self.acquire_mapping_data()
        if len(mapping)>0:
            for item in mapping:
                if item['code']==newmap['code']:    ## if the code already exists in the list a warning is shown
                    if popup==True:
                        messagebox.showwarning(title="Code Duplication", message="The code {} is already used by the name {}".format(newmap['code'], newmap['naam']))
                        self.log_to_suitelogfile('warning', 'Failed to add code {} to the list because it was already taken.'.format(newmap['code']), dt.now(tz.utc))
                elif item==mapping[-1]:             ## latest item and none of them was identical so add the new item to the list
                    file=open(credentialsfilename, 'a')
                    writer=csv.DictWriter(file, fieldnames=credentialsfileheader)
                    writer.writerow(newmap)
                    file.close()
                    self.log_to_suitelogfile('info', 'Added code {} with description {} to the list.'.format(newmap['code'], newmap['naam']), dt.now(tz.utc))
        else:                                       ## in case the credentials file is empty
            file=open(credentialsfilename, 'a')
            writer=csv.DictWriter(file, fieldnames=credentialsfileheader)
            writer.writerow(newmap)
            file.close()
            self.log_to_suitelogfile('info', 'File {} was empty.'.format(credentialsfilename), dt.now(tz.utc))
            self.log_to_suitelogfile('info', 'Added code {} with description {} to the list.'.format(newmap['code'], newmap['naam']), dt.now(tz.utc))

    def process_database_change(self, line, change_value, check_print_stickers):
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
                self.write_to_stickerfile(product, i)
        ## update the value in database
        data=self.acquire_database_content()
        for row in data:
            if row['QR code']==product['QR code']:          ## if the QR code is known in the database
                for credential in row:
                    row[credential]=product[credential]     ## overwrite the existing line with the updated line
            elif row==data[-1]:                             ## if the QR code is not known in the database
                data.append(product)                        ## add the row to the database
        ## the complete file needs to be rewritten because of the changes made
        file=open(databasefilename, 'w') 
        writer=csv.DictWriter(file, delimiter=',', fieldnames=databasefileheader)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
        file.close()
        ## recalculate totals 
        self.recalculate()


    def recalculate(self):
        ## read database file
        data=[]
        file=open(databasefilename, 'r')
        reader=csv.DictReader(file, delimiter=',')
        for row in reader:
            data.append(row)
        file.close()
        ## check for rows with matching artikelnummer and kleurcode
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
                totaal_aantal+=eval(item['aantal rollen']) if not item['aantal rollen']=='' else 0
                if item['datum']>=price_per_meter['datum']:
                    price_per_meter['datum']=item['datum']
                    price_per_meter['prijs']=item['prijs per meter']
            ## recalculate totaal aantal and totaal prijs
            prijs_per_meter=price_per_meter['prijs'] if type(price_per_meter['prijs'])==type(0) else eval(price_per_meter['prijs'])
            totaal_prijs=totaal_aantal*eval(product['aantal meters']) if not product['aantal meters']=='' else 0*prijs_per_meter
            product['prijs per meter']=prijs_per_meter
            product['totaal meters']=totaal_aantal*eval(product['aantal meters']) if not product['aantal meters']=='' else 0
            product['totaal prijs']=totaal_prijs
        ## write updated products to database
        file=open(databasefilename, 'w')
        writer=csv.DictWriter(file, fieldnames=databasefileheader)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
        file.close()

    def log_to_suitelogfile(self, level, message, time=''):
        ## apply generic settings
        levels={'info':'[INFO]   ', 'debug':'[DEBUG]  ', 'warning':'[WARNING]', 'error':'[ERROR]  '}
        level=levels[level] if level in levels.keys() else '[UNKNOWN]'
        now = time if not time=='' else dt.now(tz.utc)
        ## write to file
        hdr=suitelogfileheader
        file=open(suitelogfilename, 'a')
        writer=csv.DictWriter(file, fieldnames=hdr)
        writer.writerow({hdr[0]:level, hdr[1]:now, hdr[2]:message})
        file.close()


if __name__=="__main__":
    mode=sys.argv[1]
    root=mainwindow(mode)
    root.mainloop()





