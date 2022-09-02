import csv

def get_code(attribuutnaam):
    lengte=eval(attribuutnaam[:-2])
    codes = {'01':[30, 75],
             '02':[80, 120],
             '03':[125, 150],
             '04':[155, 180],
             '05':[185, 200],
             '06':[205, 225],
             '07':[230, 250],
             '08':[255, 275],
             '09':[280, 300],
             '10':[305, 325],
             '11':[330, 350],
             '12':[355, 375],
             '13':[380, 400],
             '14':[405, 425],
             '15':[430, 450],
             '16':[455, 475],
             '17':[480, 500]
             }
    code='@@@'
    for c in codes:
        if lengte>=codes[c][0] and lengte<=codes[c][1]:
            code=c
    return code


def load_csv(filename):
    data=[]
    data_per_order={}
    file=open(filename, 'r')
    reader=csv.DictReader(file, delimiter='\t')
    for row in reader:
        data.append(row)
        data_per_order[row['Ordernummer']]={"CreationDate":row['Datum'].replace('-', '/'), "UnitPrice":[], "Quantity":[], "NavisionCode":[], "PurchPrice":[], "ShopNumber":row['Referentie']}
    for item in data:
        data_per_order[item['Ordernummer']]["UnitPrice"].append(item['Prijs'])
        data_per_order[item['Ordernummer']]["Quantity"].append(item['Aantal'])
        data_per_order[item['Ordernummer']]["NavisionCode"].append(get_code(item['Attribuutnaam']))
        data_per_order[item['Ordernummer']]["PurchPrice"].append(item['Totale prijs'])
    file.close()
    return data_per_order

def write_xml(ordernumber, data):
    file=open("/Users/theboss/Downloads/{}.xml".format(ordernumber), 'w')
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

if __name__=="__main__":
    csvfile="/Users/theboss/Downloads/Export_redcsv.csv"
    data=load_csv(csvfile)
    for ordernumber in data:
        write_xml(ordernumber, data)

