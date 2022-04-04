# raspberrykeysniffer
### **PROJECT IS UNDER MAINTENANCE**
Hak5 Keycroc for people who don't own the wealth of elon musk and just a Raspberry Pi. This project **sniffs keyboard input and (SOON: creates an wifi acces point to look at input remotely).**

What this project does is that it captures usb keystrokes from the one side and sends it to the computer on the other while it logs the input.
## Requirements
1. Raspberry Pi which supports wifi (popular ones for example are Pi Zero W or 3B+)
2. USB cable (able to transmit data)
3. Arduino (would recommend the pro micro because it's cheap and small)
4. Logic Level Converter (5v to 3.3V)
5. cables to connect circuit for example simple jumper wires 

## Setup
1. wire the circuit as shown in the picture down below ![grafik](https://user-images.githubusercontent.com/101953958/161614461-36f30043-1680-45f8-aa02-786629012f36.png)
2. flash Raspberry Pi OS Lite (Raspbian Lite) to a micro SD card and insert it into the Pi.
3. connect to it via ssh (doesnt really matter how, just be able to connect to it)
4. git clone this repository to your pi
5. start the setup.sh script **(don't run it again after completed installation)**
6. connect both keyboard to the pi and the pi to the computer
7. start keysniffer.py
8. now it stores the keyboard strokes in a text file **(keys.txt)** usually in your **/home/pi** directory) and the victim won't notice anything :) *(if doesnt find the circuit hidden under its table of course)
9. Wifi Access Point is going to be added soon

