from behave import given, when, then
import StoreBase

def log(file, line):
    with open('dump', 'at') as file:
        file.write(line)
        file.write('\n')

@given(u'the credential mapping module is opened')
def step_impl(context):
    pass


@when(u'the name {NAME} and code {CODE} combination is entered')
def step_impl(context, NAME, CODE):
    pass


@when(u'the "add to list" function is executed')
def step_impl(context):
    pass


@then(u'the name {NAME} and code {CODE} combination should be stored in the file {FILE}')
def step_impl(context, NAME, CODE, FILE):
    pass