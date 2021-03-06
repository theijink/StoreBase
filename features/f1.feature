Feature: Directory initialisation

    As user of the program
    I want to the program to use the specified files and directories
    Such that I know where my files are located

    @implemented
    Scenario Outline: availability of source codes
        Given the program is "not started yet"
        When the directory <DIRECTORY> is examined
        Then the file <FILENAME> should be present
        Examples:
            | DIRECTORY | FILENAME          |
            | .src/     | StoreBase.py      |
            | .src/     | PostColumns.py    |
            | .src/     | SelectOrders.py   |

    @implemented
    Scenario Outline: properties of the standard files
        Given the program is "started"
        When the directory <DIRECTORY> is examined
        Then the file <FILENAME> should be available with properties <PROPERTIES> 
        Examples:
            | DIRECTORY | FILENAME              | PROPERTIES            |
            | .bin/     | databasefilename      | databasefileheader    |
            | .bin/     | activityfilename      | activityfileheader    |
            | .bin/     | credentialsfilename   | credentialsfileheader |
            | stickers/ | stickerfilename       | stickerfileheader     |


