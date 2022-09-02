'''This file can be used to filter and rearrange columns of a .csv file'''
from parameters import *
import tkinter as tk
from tkinter import filedialog as fd
import csv
from datetime import date

root = tk.Tk()
root.withdraw()
filename = fd.askopenfilename()
outfile = 'stickers/'+filename.split('.')[0]+'_out.csv'

fieldnames = [
    'YourReference',
    'CompanyName',
    'Surname',
    'Firstname',
    'CountryCode',
    'Street',
    'HouseNo',
    'HouseNoSuffix',
    'Postcode',
    'City',
    'Email',
    'MobileNumber',
    'ProductCode',
    'DeliveryToPostnl',
    'Barcode',
    'CODAmount',
    'CODReference',
    'InsuredValue',
]

#reader = csv.DictReader(open(filename, mode='r', encoding='utf-8'), delimiter=';')
reader = csv.DictReader(open(filename, mode='r', encoding='utf-8'), delimiter=',')
writer = csv.DictWriter(open(outfile, 'w'), fieldnames)
writer.writeheader()

for row in reader:
    if 'partnerid' in row: ## bestand van ccv
        newline = {
            'YourReference':row['kenmerk'],
            'CompanyName':row['bedrijfsnaam'],
            'Surname':row['naam'],
            'Firstname':'',
            'CountryCode':row['land'],
            'Street':row['straat'],
            'HouseNo':row['huisnummer'],
            'HouseNoSuffix':row['huisnummertoevoeging'],
            'Postcode':row['postcode'],
            'City':row['woonplaats'],
            'Email':row['email'],
            'MobileNumber':row['mobielnummer'],
            'ProductCode':'6440',
            'DeliveryToPostnl':str(date.today().strftime('%d-%m-%Y')),
            'Barcode':'',
            'CODAmount':'',
            'CODReference':'',
            'InsuredValue':'',
        }
        writer.writerow(newline)
    elif 'bestelnummer' in row: ## bestand van bol
        newline = {
            'YourReference':row['bestelnummer'],
            'CompanyName':row['bedrijfsnaam_verzending'],
            'Surname':row['achternaam_verzending'],
            'Firstname':row['voornaam_verzending'],
            'CountryCode':'BE',
            'Street':row['adres_verz_straat'],
            'HouseNo':row['adres_verz_huisnummer'],
            'HouseNoSuffix':row['adres_verz_huisnummer_toevoeging'],
            'Postcode':row['postcode_verzending'],
            'City':row['woonplaats_verzending'],
            'Email':'',#row['emailadres'],
            'MobileNumber':row['telnummerbezorging'],
            'ProductCode':'6440',
            'DeliveryToPostnl':str(date.today().strftime('%d-%m-%Y')),
            'Barcode':'',
            'CODAmount':'',
            'CODReference':'',
            'InsuredValue':'',
        }
        writer.writerow(newline)
    else: ## neither ccv or bol recognized
        pass
    
    
    
    ## also do the same for bol.com lists, but make sure that douvble orderno are filtered
