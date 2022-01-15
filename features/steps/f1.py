from behave import given, when, then
import os
from time import sleep

def log(file, line):
    with open('dump', 'at') as file:
        file.write(line)
        file.write('\n')


@given('the program is {state}')
def step_impl(context, state):
    context.state=state
    #log('dump', str(context.state))
    if state=="not started yet":
        pass
    elif state=="started":
        os.system("./exec")
        sleep(10)
    else:
        pass

@when('the directory {directory} is examined')
def step_impl(context, directory):
    context.directory=directory
    context.path, context.dirs, context.files = next(os.walk(directory))
    #log('dump', context.path)


@then('the file {filename} should be present')
def step_impl(context, filename):
    #log('dump', str(filename)+','+str(context.files))
    assert filename in context.files

@then('the file {filename} should be available with properties {properties}')
def step_impl(context, filename, properties):
    import imp
    import csv
    with open ('.src/parameters.py', 'rb') as fp:
        parameters = imp.load_module('.src/', fp, '.src/parameters.py', ('.py', 'rb', imp.PY_SOURCE))
    context.filename=getattr(parameters, filename)
    context.properties=getattr(parameters, properties)
    with open (context.filename, 'rt') as file:
        reader=csv.reader(file, delimiter=',')
        i=0
        for row in reader:
            if i==0:
                properties=row
            else:
                break
            i+=1
    #log('dump', str(properties)+'|'+str(context.properties))
    assert properties == context.properties