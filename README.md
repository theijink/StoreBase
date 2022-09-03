# StoreBase
A custom database management software program

## Setting to work:
1. make sure to have python installed, preferably version 3.8.7. Also java should be installed. For development, OpenJDK 18.0.2 is used.
2. make sure to have the latest version of pip and use it to install virtualenv.
3. clone this repo and open a terminal at the main directoy (StoreBase/).
4. create a virtual environment with "python3 -m venv .venv".
5. activate the venv by the command "source .venv/bin/activate".
6. Now install the dependencies listed in this README.
7. Use the "deactivate" command to get out of the venv.
8. run the software by the command "./exec". A java application is built and started from which the different applications can be used. Also a parameters file is generated, which is used by the python code.


## Dependencies and Libraries:
### pip
Package         Version
--------------- -------
behave          1.2.6
click           8.0.3
cycler          0.11.0
Flask           2.0.2
fonttools       4.28.5
itsdangerous    2.0.1
Jinja2          3.0.3
kiwisolver      1.3.2
MarkupSafe      2.0.1
matplotlib      3.5.1
numpy           1.22.0
packaging       21.3
parse           1.19.0
parse-type      0.5.2
Pillow          9.0.0
pip             22.2.2
pyparsing       3.0.6
python-dateutil 2.8.2
setuptools      49.2.1
six             1.16.0
Werkzeug        2.0.2

### java
import javax.swing.JButton;  
import javax.swing.JFrame;  
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextArea;
import javax.swing.JScrollPane;
import javax.swing.ImageIcon;
import javax.swing.JFileChooser;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.time.ZonedDateTime;
import java.awt.Image;
import java.time.ZonedDateTime;
import java.time.ZoneId;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStreamReader;
