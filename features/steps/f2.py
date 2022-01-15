from behave import given, when, then

@given(u'the credential mapping module is opened')
def step_impl(context):
    import imp



@when(u'the name <NAME> and code <CODE> combination is given')
def step_impl(context):
    pass


@when(u'the "add to list" function is executed')
def step_impl(context):
    pass


@then(u'the name <NAME> and code <CODE> combination should be stored in the file <FILE>')
def step_impl(context):
    pass