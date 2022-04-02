# rpi-keysniffer
**PROJECT IS UNDER MAINTENANCE**
Hak5 Keycroc for people who don't own the wealth of elon musk. Sniffs Keyboard Input and (SOON: creates an wifi acces point to look at input).
Description will come SOON

What this project does is that it captures usb keystrokes from the one side and sends it to the computer on the other while it logs the input.
## Requirements
1. Raspberry Pi which supports wifi and the usb emulation feature (popular ones for example are Pi Zero W or 3B+)
2. USB cable(s)
(if you use a Raspberry Pi Zero W)
3. either be able to solder a second usb connector to the pi zero w's GPIO pins or buy an extension to have more usb ports. 


## Setup
1. Flash Raspberry Pi OS Lite (Raspbian Lite) to a micro SD card and insert it into the Pi.
2. connect to it via ssh (doesnt really matter how just be able to connect to it)
3. start the setup.sh script
4. connect both keyboard to the pi and the pi to the computer
5. now it stores the keyboard strokes in a text file (when installed normally in your home directory)
6. Wifi Access Point is going to be added soon

## How it works
Thanks to https://github.com/n0rc for the code to send the key strokes.
