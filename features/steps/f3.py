from behave import given, when, then

def log(file, line):
    with open('dump', 'at') as file:
        file.write(line)
        file.write('\n')


@given(u'the "Add to DataBase" module is opened')
def step_impl(context):
    from StoreBase import db
    context.db=db.DataBase()

@given(u'the "Modify DataBase" module is opened')
def step_impl(context):
    from StoreBase import db
    context.db=db.DataBase()

@given(u'the product with QR code {QR} is stored in the file {FILE}')
def step_impl(context, QR, FILE):
    import csv
    filename=getattr(context.db.parameters, FILE)
    file=open(filename, 'r')
    reader=csv.DictReader(file, delimiter=',')
    ## check if parameter QR is listed
    listed=[]
    for row in reader:
        if QR==row[context.db.parameters.databasefileheader[11]]:
            context.item=row
            listed.append(True)
        else:
            listed.append(False)
    file.close()
    ## passed if True occurs in list
    assert True in listed


@when(u'a product is entered with code {CODE}, name {NAME}, colorcode {COLORCODE}, color {COLOR}, #meters {LENGTH}, #rolls {AMOUNT}, #per_roll {ROLL_QTY}, date {DATE}, price {PRICE}, total price {PRICE_TOT}, total_length {LEN_TOT}, QR code {QR}')
def step_impl(context, CODE, NAME, COLORCODE, COLOR, LENGTH, AMOUNT, ROLL_QTY, DATE, PRICE, PRICE_TOT, LEN_TOT, QR):
    pass
    fieldnames=context.db.parameters.databasefileheader
    context.item={
        fieldnames[0]:CODE,
        fieldnames[1]:NAME,
        fieldnames[2]:COLORCODE,
        fieldnames[3]:COLOR,
        fieldnames[4]:LENGTH,
        fieldnames[5]:AMOUNT,
        fieldnames[6]:ROLL_QTY,
        fieldnames[7]:DATE,
        fieldnames[8]:PRICE,
        fieldnames[9]:PRICE_TOT,
        fieldnames[10]:LEN_TOT,
        fieldnames[11]:QR,
    }


@when(u'a product is enterd by its QR code {QR}')
def step_impl(context, QR):
    context.QR=QR

@when(u'the "add_new_item" function is executed')
def step_impl(context):
    log('dump', str(context.item.keys()))
    context.db.add_new_item(context.item)

@when(u'the "remove_from_database" function is executed')
def step_impl(context):
    context.db.remove_from_database(context.item)


@then(u'the code {CODE}, name {NAME}, colorcode {COLORCODE}, color {COLOR}, #meters {LENGTH}, #rolls {AMOUNT}, #per_roll {ROLL_QTY}, date {DATE}, price {PRICE}, total price {PRICE_TOT}, total_length {LEN_TOT}, QR code {QR} combination should be stored in the file {FILE}')
def step_impl(context, CODE, NAME, COLORCODE, COLOR, LENGTH, AMOUNT, ROLL_QTY, DATE, PRICE, PRICE_TOT, LEN_TOT, QR, FILE):
    import csv
    from StoreBase import parameters
    ## get filename and open and read file
    filename=getattr(parameters, FILE)
    file=open(filename, 'r')
    reader=csv.DictReader(file, delimiter=',')
    ## check for matching code-name
    listed=[]
    for row in reader:
        if [CODE, NAME, COLORCODE, COLOR, LENGTH, AMOUNT, ROLL_QTY, DATE, PRICE, PRICE_TOT, LEN_TOT, QR] == [v for v in row.values()]:
            listed.append(True)
        else:
            listed.append(False)
    file.close()
    ## passed if there is True in the list
    assert True in listed


@then(u'the product with QR code x should be removed from the file databasefilename')
def step_impl(context):
    pass

