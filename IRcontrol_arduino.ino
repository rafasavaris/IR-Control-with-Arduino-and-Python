/* ****************************************************************** * 
 *                Mouse control from an IR remote control             *
 *                   with Arduino and Python (PART 1)                 *
 * AUTHOR: Rafaela Savaris                                            *
 * DATE: 16/02/2025                                                   *
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
 *            This code reads IR signals sent by a remote control and *
 *            received by an IR receiver, writing the signal in HEX   *
 *            to the serial port.                                     * 
 * REQUIRED LIBRARY:                                                  *
 *             IRremote.h                                             *
 * COMPONENTS:                                                        *
 *             1x - IR receiver                                       *
 *             1x - Arduino UNO                                       *
 *             3x - Jumper                                            *
 * ****************************************************************** */

#include <IRremote.h>

int RECV_PIN = 2;  // IR receiver pine

void setup() {
  Serial.begin(9600); // baudrate in 9600
  IrReceiver.begin(RECV_PIN);  // Starts the IR receptor
}

void loop() {
  if (IrReceiver.decode()) {  // Decodes the IR signal
    Serial.println(IrReceiver.decodedIRData.decodedRawData, HEX);  // Print the decoded signal in HEX
    IrReceiver.resume();  // Prepare to the next reading
    delay(100); // Wait 0.1 seconds
  }
}
