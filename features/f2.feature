Feature: Testing the credential mapping function

    As a user of the program
    I want to be able to add a code-name combination to a list
    Such that the program autofills the name when a code is entered

    @implemented
    Scenario Outline: Adding an item to the list
        Given the program is "started"
        And the credential mapping module is opened
        When the name <NAME> and code <CODE> combination is entered
        And the "add_credential" function is executed
        Then the name <NAME> and code <CODE> combination should be stored in the file <FILE>
        Examples:
            | NAME  | CODE  | FILE                  |
            | test  | 1234  | credentialsfilename   |

    @not_implemented
    Scenario Outline: Autofill function at certain interface
        Given the program is started
        And the module "" us opened
        When the code <CODE> is entered in entry <CODE_ENTRY>
        Then the name <NAME> should be shown in the entry <NAME_ENTRY>
    
    @implemented
    Scenario Outline: Remove an item from the list
        Given the program is "started"
        And the credential mapping module is opened
        And the <NAME> and <CODE> combination is stored in the <FILE>
        When the name <NAME> and code <CODE> combination is entered
        And the "remove_credential" function is executed
        Then the name <NAME> and code <CODE> combination should be removed from the file <FILE>
        Examples:
            | NAME  | CODE  | FILE                  |
            | test  | 1234  | credentialsfilename   |