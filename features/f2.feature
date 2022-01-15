Feature: Testing the credential mapping function

    As a user of the program
    I want to be able to add a code-name combination to a list
    Such that the program autofills the name when a code is entered

    Scenario: Adding an item to the list
        Given the program is "started"
        And the module "" is opened
        When the name <NAME> and code <CODE> combination is given
        And the combination is added to the file
        Then the name <NAME> and code <CODE> combination should be stored in the file <FILE>

    Scenario: Autofill function at certain interface
        Given the program is started
        And the module "" us opened
        When the code <CODE> is entered in entry <CODE_ENTRY>
        Then the name <NAME> should be shown in the entry <NAME_ENTRY>