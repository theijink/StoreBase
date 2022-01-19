Feature: Database Manpulation

    As user of the application
    I should be able to add a new item to the database
    Such that it creates a QR code, prints stickers, and the quantity is maintained

    @implemented
    Scenario Outline: Adding an item to the database
        Given the program is "started"
        And the "Add to DataBase" module is opened
        When a product is entered with code <CODE>, name <NAME>, colorcode <COLORCODE>, color <COLOR>, #meters <LENGTH>, #rolls <AMOUNT>, #per_roll <ROLL_QTY>, date <DATE>, price <PRICE>, total price <PRICE_TOT>, total_length <LEN_TOT>, QR code <QR>
        And the "add_new_item" function is executed
        Then the code <CODE>, name <NAME>, colorcode <COLORCODE>, color <COLOR>, #meters <LENGTH>, #rolls <AMOUNT>, #per_roll <ROLL_QTY>, date <DATE>, price <PRICE>, total price <PRICE_TOT>, total_length <LEN_TOT>, QR code <QR> combination should be stored in the file <FILE>
        Examples:
            | CODE  | NAME  | COLORCODE | COLOR | LENGTH    | AMOUNT    | ROLL_QTY  | DATE          | PRICE | PRICE_TOT | LEN_TOT   | QR    | FILE              |
            | T0    | test  | C0        | clr   | 1000      | 3         | 0         | 01/01/2022    | 0     | 0         | 0         | x     | databasefilename  |

    @testing
    Scenario Outline: Increasing the stock quantity of a product
        Given the program is "started"
        And the "Modify DataBase" module is opened
        And the product with QR code <QR> is stored in the file <FILE>
        And the "initial stock quantity" of the product with QR code <QR> is known
        When a product is enterd by its QR code <QR>
        And the "change_stock_quantity" function is executed with quantity <QTY>
        Then the "final stock quantity" should equal the "initial stock quantity" plus <QTY>
        Examples:
            | QR    | QTY   | FILE              |
            | x     | -1    | databasefilename  |

    @skip @implemented
    Scenario Outline: Removing an item from the database
        Given the program is "started"
        And the "Modify DataBase" module is opened
        And the product with QR code <QR> is stored in the file <FILE>
        When a product is enterd by its QR code <QR>
        And the "remove_from_database" function is executed
        Then the product with QR code <QR> should be removed from the file <FILE>
        Examples:
            | QR    | FILE              |
            | x     | databasefilename  |
    
    @not_implemented
    Scenario Outline: Autocreation of QR code
        Given the program is "started"
    
    @not_implemented
    Scenario Outline: Autocreation of stickers
        Given the program is started
        And an item is added to the database

    @not_implemented
    Scenario Outline: Automapping of new credentials
        Given the program is started
        And an item is added to the database

    @not_implemented
    Scenario Outline: Autofill of mapped credentials
        Given the program is "started"

    @not_implemented
    Scenario Outline: Autofill of date
        Given the program is "started"
