from behave import given, when, then
import os
from time import sleep
import imp

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
        time.sleep(10)
    else:
        pass

@when('the directory {directory} is examined')
def step_impl(context, directory):
    context.directory=directory
    context.path, context.dirs, context.files = next(os.walk(directory))
    log('dump', context.path)


@then('the file {filename} should be present')
def step_impl(context, filename):
    #log('dump', str(filename)+','+str(context.files))
    assert filename in context.files

@then('the file {filename} should be available with the following {properties}')
def step_impl(context, filename, properties):
    pass