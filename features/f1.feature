Feature: Directory initialisation

    As user of the program
    I want to the program to use the specified files and directories
    Such that I know where my files are located

    Scenario Outline: availability of source codes
        Given the program is not started yet
        When the source directory is examined
        Then <FILENAME> should be present
        Examples:
            | FILENAME          |
            | StoreBase.py      |
            | PostColumns.py    |
            | SelectOrder.py    |

    Scenario Outline: properties of the bin files
        Given the program is started
        When <DIRECTORY> is examined
        Then <FILENAME> is should be available with the following <PROPERTIES> 
            | DIRECRORY | FILENAME              | PROPERTIES            |
            | .bin/     | databasefilename      | databasefileheader    |
            | .bin/     | activityfilename      | activityfileheader    |
            | .bin/     | credentialsfilename   | credentialsfileheader |
            | stickers/ | stickersfilename      | stickersfileheader    |
