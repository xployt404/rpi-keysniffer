# raspberrykeysniffer
### **PROJECT IS UNDER MAINTENANCE**
Hak5 Keycroc for people who don't own the wealth of elon musk and just a Raspberry Pi. This project sniffs keyboard input and (SOON: creates an wifi acces point to look at input remotely).
Description will come SOON

What this project does is that it captures usb keystrokes from the one side and sends it to the computer on the other while it logs the input.
## Requirements
1. Raspberry Pi which supports wifi and the usb emulation feature (popular ones for example are Pi Zero W or 3B+)
2. USB cable(s)
**(if you use a Raspberry Pi Zero W)**
3. either be able to solder a second usb connector to the pi zero w's GPIO pins or buy an extension to have more usb ports. 


## Setup
1. flash Raspberry Pi OS Lite (Raspbian Lite) to a micro SD card and insert it into the Pi.
2. connect to it via ssh (doesnt really matter how just be able to connect to it)
3. git clone this repository to your pi
4. start the setup.sh script **(don't run it twice after completed installation)**
5. connect both keyboard to the pi and the pi to the computer
6. start keysniffer.py
7. now it stores the keyboard strokes in a text file **(keys.txt)** usually in your **/home/pi** directory)
8. Wifi Access Point is going to be added soon

Thanks to https://github.com/n0rc for the code to send the key strokes.
