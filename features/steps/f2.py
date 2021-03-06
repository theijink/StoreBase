from behave import given, when, then
import StoreBase

def log(file, line):
    with open('dump', 'at') as file:
        file.write(line)
        file.write('\n')


@given(u'the credential mapping module is opened')
def step_impl(context):
    from StoreBase import db
    context.db=db.DataBase()


@when(u'the name {NAME} and code {CODE} combination is entered')
def step_impl(context, NAME, CODE):
    context.name=NAME
    context.code=CODE


@when(u'the "add_credential" function is executed')
def step_impl(context):
    context.db.add_credential(context.code, context.name)


@then(u'the name {NAME} and code {CODE} combination should be stored in the file {FILE}')
def step_impl(context, NAME, CODE, FILE):
    import csv
    from StoreBase import parameters
    ## get filename and open and read file
    filename=getattr(parameters, FILE)
    file=open(filename, 'r')
    reader=csv.DictReader(file, delimiter=',')
    ## check for matching code-name
    listed=[]
    for row in reader:
        if [CODE, NAME] == [v for v in row.values()]:
            listed.append(True)
        else:
            listed.append(False)
    file.close()
    ## passed if there is True in the list
    assert True in listed


@given(u'the {NAME} and {CODE} combination is stored in the {FILE}')
def step_impl(context, NAME, CODE, FILE):
    from StoreBase import parameters
    import csv
    filename=getattr(parameters, FILE)
    file=open(filename, 'r')
    reader=csv.DictReader(file, delimiter=',')
    ## confirm that the combination is in the file
    listed=[]
    for row in reader:
        if [CODE, NAME] == [v for v in row.values()]:
            listed.append(True)
        else:
            listed.append(False)
    file.close()
    ## passed if there is True in the list
    assert True in listed


@when(u'the "remove_credential" function is executed')
def step_impl(context):
    context.db.remove_credential(context.code)


@then(u'the name {NAME} and code {CODE} combination should be removed from the file {FILE}')
def step_impl(context, NAME, CODE, FILE):
    from StoreBase import parameters
    import csv
    filename=getattr(parameters, FILE)
    file=open(filename, 'r')
    reader=csv.DictReader(file, delimiter=',')
    ## confirm that the combination is in the file
    listed=[]
    for row in reader:
        if [CODE, NAME] == [v for v in row.values()]:
            listed.append(True)
        else:
            listed.append(False)
    file.close()
    ## passed if there is no True in the list
    assert not True in listed