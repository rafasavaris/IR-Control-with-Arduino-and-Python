# IR Control with Arduino and Python

This project consists of controlling the computer cursor through an IR remote control, Arduino UNO and Python, by sending and reading information through the computer's serial port.
***
## Required Hardware
* 1x IR Remote Control
* 1x IR receptor
* 1x Arduino UNO (or Arduino MEGA)
* Some jumpers
***
## Required Software
To use the IR receiver, I used the [IRremote]([https://docs.arduino.cc/libraries/irremote/) library. To control the mouse and read the serial port, in python, I used the [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) API and the [PySerial](https://pythonhosted.org/pyserial/) library, respectively.
***
## Notes
* When opening the .ino file, you will probably need to create a folder with the same name as the file for it to run.

* If you are using an Arduino with HDI support, it is easier to use the [Mouse.h](https://docs.arduino.cc/libraries/mouse/) library directly on the Arduino.

* In the .py file, on line 34, change the name of the serial port to the one you are using (in my case, it was 'COM 5')
```
ser = serial.Serial(port='COM5', baudrate=9600, timeout=1)
```
***
### If you have any questions, please contact me at my contact addresses.
