from pkgutil import get_data
from StoreBase import parameters
import csv

class DataBase():
    def __init__(self):
        self.parameters = parameters


    def add_credential(self, code, name):
        ## get data
        data = self.get_data(self.parameters.credentialsfilename)
        ## check for duplicate code
        duplicates=[]
        for row in data:
            if code==row[self.parameters.credentialsfileheader[0]]:
                duplicates.append(True)
            else:
                duplicates.append(False)
        if True in duplicates:
            ## error message
            pass
        else:
            ## append newrow
            data.append({self.parameters.credentialsfileheader[0]:code, self.parameters.credentialsfileheader[1]:name})
            ## open and write data to file
            self.write_file(data, self.parameters.credentialsfilename, self.parameters.credentialsfileheader)
            

    def remove_credential(self, code):
        '''item=item'''
        ## aquire data
        data = self.get_data(self.parameters.credentialsfilename)
        ## remove item from data
        for row in data:
            if code==row[self.parameters.credentialsfileheader[0]]:
                data.remove(row)
        ## write data to file
        self.write_file(data, self.parameters.credentialsfilename, self.parameters.credentialsfileheader)




    def add_new_item(self, item):
        '''item=new dict item with databasefileheader attributes'''
        assert [k for k in item.keys()] == self.parameters.databasefileheader
        ## acquire data
        data = self.get_data(self.parameters.databasefilename)
        ## check for duplicate QR
        duplicates=[]
        for row in data:
            if row[self.parameters.databasefileheader[11]]==item[self.parameters.databasefileheader[11]]:
                duplicates.append(True)
            else:
                duplicates.append(False)
        if True in duplicates:
            ## error
            assert False
        else:
            ## append new item
            data.append(item)
            ## write data to file
            self.write_file(data, self.parameters.databasefilename, self.parameters.databasefileheader)
            ## write to stickerfile
            self.write_stickers(item)


    def remove_from_database(self, item):
        '''item=existing dict item with databasefileheader attributes'''
        assert [k for k in item.keys()] == self.parameters.databasefileheader
        ## acquire data
        data = self.get_data(self.parameters.databasefilename)
        for row in data:
            if row==item:
                data.remove(row)
            else:
                pass
        ## write data to file
        self.write_file(data, self.parameters.databasefilename, self.parameters.databasefileheader)

    def get_current_stock(self, QRcode):
        '''return the current stock quantity (attribute 5) of product with given QR code (attribute 11)'''
        ## acquire data
        data = self.get_data(self.parameters.databasefilename)
        ## search data for ID (QR)
        for row in data:
            if row[self.parameters.databasefileheader[11]]==QRcode:
                ## store the stock quantity
                qty=row[self.parameters.databasefileheader[5]]
        ## return stock qty
        return qty
    
    def manipulate_item_qty(self, QRcode, QTY):
        '''for a product with given QRcode (attribute 11), change its stock quantity (attribute 5)'''
        ## acquire data
        data = self.get_data(self.parameters.databasefilename)
        ## search data for ID (=QR code)
        for row in data:
            if row[self.parameters.databasefileheader[11]]==QRcode:
                row[self.parameters.databasefileheader[5]]=eval(row[self.parameters.databasefileheader[5]])+eval(QTY)
        ## write modified dataset to file
        self.write_file(data, self.parameters.databasefilename, self.parameters.databasefileheader)
    
    def modify_content(self, item):
        '''item=modified item'''
        ## get_data(self.parameters.databasefilename)
        ## search data for ID
        ## opt: write to stickerfile
        pass


    def write_stickers(self, newrow):
        '''newrow=added or modified item with '''
        ## convert newrow to stickerfileheader format for each added amount (1/6, 2/6, ..., 6/6)
        ## read -a stickerfilename
        ## append stickers (items in converted newrow)
        ## close file
        pass


    def get_data(self, filename):
        '''read and return content of a given file'''
        data=[]
        file=open(filename, 'r')
        reader=csv.DictReader(file, delimiter=',')
        for row in reader:
            data.append(row)
        file.close()
        return data


    def write_file(self, data, filename, fieldnames):
        '''write data with given layout to specified file'''
        file=open(filename, 'w')
        writer=csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
        ## close file
        file.close()

    def statsgraph(self):
        import matplotlib.pyplot as plt
        from collections import Counter
        dates=[]
        for row in self.get_data(self.parameters.databasefilename):
            if "datum" in self.parameters.databasefileheader:
                dates.append(row["datum"])
            else:
                pass
        chart_data=Counter(dates)
        fig=plt.figure()
        ax=fig.add_subplot()
        ax.barh([i for i in chart_data], [chart_data[i] for i in chart_data])
        ax.set_xlabel("Appearance")
        ax.set_title("Date distribution of all {} items in database".format(len(dates)))
        fig.tight_layout()
        plt.savefig(".bin/statsgraph.png", dpi=720)





