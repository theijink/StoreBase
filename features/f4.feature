Feature: Modification of an item in the DataBase

    As a user of the program
    I want to be able to find a product by its QR code
    Such that I can review and change the stock quantity

    Scenario Outline: Increasing the stock quantity of a product
        Given the program is "started"
        And the "Modify DataBase" module is opened
        And the product with QR code <QR> is stored in the file <FILE>
        And the product with QR code <QR> has a stock quantity of at least <QTY>
        When a product is enterd by its QR code <QR>
        And the "change_stock_quantity" function is executed with values change <CHANGE>, price <PRICE>, 