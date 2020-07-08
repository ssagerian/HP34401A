# HP34401A
Python Class to support utilizing the HP34401A Digital multimeter 
## Project Origin
This project came about when I needed to automate my HP34401A to read current over a number of days. I found a github project that supported the HP34401A but later discovered that the code didnt work well and was limited in its functionality. 
## Python Modules
The module needs _PySerial_  python modules
## Hardware
The HP34401A utilizes dsr/dtr hardware handshaking to work correctly, for you this means you need to apply approximately 4VDC to 12VDC between Pins 6 (dsr), pin 1 (gnd).
You can do this by using any wall wart with voltage output that is between those two ranges..
## Current Files
* __main__.py is the test driver
* HP34401A.py is the class file
* sample_and_save.py is a program I wrote to continously capture and save measurements. It utilizes the HP34401A.py module/class
* DMM33401A.py is the original continous capture and save measurement python script (non class based). I keep it as a reference. 
