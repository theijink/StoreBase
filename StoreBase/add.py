from __future__ import annotations
from turtle import color
import parameters
import db
import tkinter as tk
from datetime import datetime as dt

class window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.parameters=parameters
        self.db=db.DataBase()
        self.wm_title("Add Product - StoreBase")
        self.item={}
        self.set_widgets()
        self.infiniteloop=tk.BooleanVar(value=True)
        self.updateloop()
    
    def set_widgets(self):
        grid={'row':0, 'col':0}
        ## add labels, create textvariables and link them to entries
        for attribute in self.parameters.databasefileheader:
            self.item[attribute]=tk.StringVar()
            tk.Label(text=attribute).grid(row=grid['row'], column=0)
            tk.Entry(textvariable=self.item[attribute]).grid(row=grid['row'], column=1)
            grid['row']+=1
        ## create ADD button
        self.btn=tk.Button(text="ADD to database", command=lambda:[self.infiniteloop.set(False), self.add_to_db(), self.destroy()])
        self.btn.grid(row=grid['row'], column=2)
        self.btn['state']='disabled'
    
    def add_to_db(self):
        ## create DB item from entries
        self.newitem={}
        for attribute in self.item:
            self.newitem[attribute]=self.item[attribute].get()
        self.db.add_new_item(self.newitem)
        

    def updateloop(self):
        ## set date (attribute 7) initially to today, but don't loop this
        self.item[self.parameters.databasefileheader[7]].set(str(dt.now().strftime('%d/%m/%Y')))
        ## obtain credential mapping info once, don't loop this
        self.mapping=self.db.get_data(self.parameters.credentialsfilename)
        ## obtain database content once, also don't acquire this continuously
        self.data=self.db.get_data(self.parameters.databasefilename)
        ## DO loop over the following functions in order to update the window
        while self.infiniteloop.get():
            ## create QRcode from entered values
            self.set_QRcode()
            ## update the credentials
            self.set_credentials()
            ## if a product is in DB already, or if any entry is empty, keep button disabled
            self.verify_product()
            ## update the tkinter interface
            self.update()


    def set_QRcode(self):
        ## obtain QR code elements
        artno=self.item[self.parameters.databasefileheader[0]].get()
        clrno=self.item[self.parameters.databasefileheader[2]].get()
        clr=self.item[self.parameters.databasefileheader[3]].get()
        date=self.item[self.parameters.databasefileheader[7]].get()
        ## construct QR code from elements
        self.item[self.parameters.databasefileheader[11]].set(artno+"'"+clrno+"'"+clr+"'"+date)


    def set_credentials(self):
        artno=self.item[self.parameters.databasefileheader[0]]
        art=self.item[self.parameters.databasefileheader[1]]
        clrno=self.item[self.parameters.databasefileheader[2]]
        clr=self.item[self.parameters.databasefileheader[3]]
        for row in self.mapping:
            ## if article no. is in mapped, set article name to corresponding value
            if row[self.parameters.credentialsfileheader[0]]==artno.get():
                art.set(row[self.parameters.credentialsfileheader[1]])
            ## if color no. is in mapped, set color name to corresponding value
            if row[self.parameters.credentialsfileheader[0]]==clrno.get():
                clr.set(row[self.parameters.credentialsfileheader[1]])
        

    def verify_product(self):
        ## create DB item from entries
        self.product={}
        for attribute in self.item:
            self.product[attribute]=self.item[attribute].get()
        ## check whether the product as entered is already in the database or has empty entries. In case not, enable button
        if self.product in self.data:
            self.btn['state']='disabled'
        elif '' in [v for v in self.product.values()]:
            self.btn['state']='disabled'
        else:
            self.btn['state']='normal'

        





if __name__=="__main__":
    root=window()
    root.mainloop()




