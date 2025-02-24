'''
 * ****************************************************************** * 
 *                  Mouse control from an IR remote control           *
 *                     with Arduino and Python (PART 2)               *
 * AUTHOR: Rafaela Savaris                                            *
 * DATE: 16/02/2025                                                   *
 *                                                                    *
 * PROJECT DESCRIPTION:                                               *
 *            This project allows controlling the mouse cursor using  *
 *            an IR remote control. The IR receiver, connected to an  *
 *            Arduino, captures the signals emitted by each button    *
 *            press on the remote. The Arduino reads, decodes, and    *
 *            prints the corresponding code to the serial port. A     *
 *            Python program monitors the serial port, interprets the *
 *            received codes, and performs specific actions on the    *
 *            such as moving in different directions or clicking,     *
 *            depending on the button pressed on the remote control.  *
 * ****************************************************************** *
 * CODE DESCRIPTION:                                                  *
 *            This code reads the serial port on which the IR signal  *
 *            for each key on the remote control is being  written.   * 
 *            Depending on which key was pressed, a movement is       *
 *            executed.                                               * 
 * REQUIRED:                                                          *
 *             pyserial (pip install pyserial)                        *
 *             pyAutoGUI (pip install pyautogui)                      *
 * ****************************************************************** * '''

import serial
import pyautogui as mouse
import sys

# Configures the connection to the COM port 5 (baud rate equal to that of the Arduino)
ser = serial.Serial(port='COM5', baudrate=9600, timeout=1)

# Mapping controls to mouse action
commands = {
    "BA45FF00": lambda: mouse.move(0, 10, tween=mouse.easeInOutQuad),
    "B946FF00": lambda: mouse.move(0, -10, tween=mouse.easeInOutQuad),
    "BB44FF00": lambda: mouse.move(-10, 0, tween=mouse.easeInOutQuad),
    "BF40FF00": lambda: mouse.move(10, 0, tween=mouse.easeInOutQuad),
    "BC43FF00": lambda: mouse.click(),
    "F609FF00": lambda: sys.exit()
}

# Previously read data
previous_data = ""

try:
    while True:
        # Read and process data serial
        data = ser.readline().decode('utf-8').strip()
        if data:
            print(f"Received: {data}")

            if data == '0' and previous_data in commands:
                commands[previous_data]()  # Execute the last saved command
            elif data in commands:
                commands[data]()  # Execute the corresponding command
                previous_data = data  # Update the last valid command
except KeyboardInterrupt:
    print("Ending reading.")
finally:
    ser.close()  # Close the serial port when exit
