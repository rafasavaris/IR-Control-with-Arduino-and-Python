# IR Control with Arduino and Python

This project demonstrates how to control the computer mouse cursor using an **IR remote control**, an **Arduino board**, and **Python**. The system works by transmitting IR signals to the Arduino, which then sends commands to the computer via the serial port. A Python script reads these commands and translates them into mouse movements and actions.

---

## 🔧 How It Works

1. The IR remote sends signals to the IR receiver.  
2. The Arduino decodes the received IR commands.  
3. The decoded data is sent to the computer through the serial interface.  
4. A Python script reads the serial data and controls the mouse using software automation.

---

## 🧰 Required Hardware

- 1× IR Remote Control  
- 1× IR Receiver  
- 1× Arduino UNO (or Arduino MEGA)  
- Jumper wires  

Connect the **VCC** pin to the Arduino **5V** and the **GND** pin to **GND**.  
The **data/output** pin can be connected to any digital pin on the Arduino — in my case, I used **pin X**.

You can check the sensor pinout in the image below:

<img
  alt="IR Receptor Pin"
  src="IR_Receptor_pin.jpg"
  width="420px"
/>

---

## 💻 Required Software

### Arduino
- **[IRremote](https://docs.arduino.cc/libraries/irremote/)** — used to decode IR signals from the remote control.

### Python
- Python Version: 3.12.7
- **[PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)** — used to control mouse movement and clicks.  
- **[PySerial](https://pythonhosted.org/pyserial/)** — used to read data from the serial port.

---

## ⚙️ Setup & Usage

1. Upload the `.ino` file to your Arduino board;
2. Connect the IR receiver to the Arduino according to the pin definitions in the code;
3. Open the Python script and update the serial port name to match your system:
```python
   ser = serial.Serial(port='COM5', baudrate=9600, timeout=1)
```
4. Run the Python script;
5. Use the IR remote to control the mouse cursor.

## 📝 Notes

1. When opening the .ino file in the Arduino IDE, make sure it is placed inside a folder with the same name as the file;
2. If you are using an Arduino board with HID support, you may control the mouse directly using the '''Mouse.h''' library, without Python;
3. The serial port name may vary depending on your operating system (e.g., COMx on Windows or /dev/ttyUSBx on Linux).

---
