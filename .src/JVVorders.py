import tkinter as tk
from tkinter import filedialog as fd
import csv
import pandas as pd
import numpy as np

def load_xls(filename=''):
    filename=fd.askopenfilename(filetypes=[("Excel Worksheets","*.xls"), ("Excel Worksheets","*.xlsx")], initialdir='.') if filename=='' else filename
    df = pd.read_excel(filename)#, skiprows=[0,1])
    dt = df.to_dict('records')
    return dt, filename

def is_first_row(row):
    '''return True when row is considered "first row" OR when it is the last row'''
    return (str(row['Artikelnr.'])[:2]=='10' or str(row['Artikelnr.'])=='Totaal') if len(str(row['Artikelnr.']))==6 else False

def write(line):
    '''print line. Dit kun je veranderen door het bijvoorbeeld naar een bestand te scrhijven'''
    print(line)

if __name__=="__main__":
    filename="/Users/twanheijink/Documents/GitHub/StoreBase/test/testdata/Bestelling 4682.xlsx"
    data, filename=load_xls(filename)

    for i in range(len(data)-1):
        ## determine the index of the next "first row'"
        j=i+1
        while j<len(data) and not is_first_row(data[j]):
            print(i, j, end='\r')
            j+=1
            break
        ## write data
        if is_first_row(data[i]):
            Artikelnr = data[i]['Artikelnr.']
            Kleur = data[i]['Kleur']
            Lengths = str(data[j]['Artikelnr.']).split(' ')
            Amounts = str(data[j]['Omschrijving']).split(' ')
            for L,A in zip(Lengths, Amounts):
                write('{} {} {}, {}'.format(Artikelnr, Kleur, L, A))
