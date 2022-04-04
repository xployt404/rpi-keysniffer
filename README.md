# raspberrykeysniffer
### **PROJECT IS UNDER MAINTENANCE**
Hak5 Keycroc for people who don't own the wealth of elon musk and just a Raspberry Pi. Go see for yourself how expensive that stuff is: https://shop.hak5.org/products/key-croc. This project **sniffs keyboard input and (SOON: creates an wifi acces point to look at input remotely).**

What this project does is that it captures usb keystrokes from the one side and sends it to the computer on the other while it logs the input.
## Requirements
1. Raspberry Pi which supports wifi (popular ones for example are Pi Zero W or 3B+)
2. USB cable (able to transmit data)
3. Arduino (would recommend the pro micro because it's cheap and small)
4. Logic Level Converter (5v to 3.3V)
5. cables to connect circuit for example simple jumper wires 

## Setup
First of all wire the circuit as shown down below. You can see the Pinouts of each device in the following pictures. Just wire the Logic Level Converter inbetween. <br/>
  Raspberry Pi -->  Logic Level Converter -->  Arduino<br/>
  GND --> GND -->                   GND<br/>
  3.3V Pin -->      LV/HV   -->               VCC<br/>
  SDA Pin -->       LV1/HV1 -->               SDA (on Pro Micro it is Pin A2)<br/>
  SCL Pin -->       LV2/HV2 -->               SCL (on Pro Micro it is Pin A3)<br/>
  <br/>
  ![PI](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.5w6o5TavjJgsAIlh1BZNBQHaFM%26pid%3DApi&f=1)
  <br/>
  ![Arduino](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.4ccj1-oQ7_8lGOeUml67cQHaGL%26pid%3DApi&f=1)
  <br/>
  ![LogicLevel](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.jq4Lwx2Q2INxi24Z5HDjzAHaHa%26pid%3DApi&f=1)
  **NOTE THAT YOU CONNECT THE LV SIDE TO THE RASPBERRY PI AND THE HV SIDE TO THE ARDUINO OTHERWISE YOU MIGHT DESTROY YOUR PI** <br/>
1. flash Raspberry Pi OS Lite (Raspbian Lite) to a micro SD card and insert it into the Pi.
2. connect to it via ssh (doesnt really matter how, just be able to connect to it)
3. git clone this repository to your pi
4. start the setup.sh script **(don't run it again after completed installation)**
5. connect both keyboard to the pi and the pi to the computer
6. start keysniffer.py
7. now it stores the keyboard strokes in a text file **(keys.txt)** usually in your **/home/pi** directory) and the victim won't notice anything :) <br/>*if it doesnt find the circuit hidden under its table of course 
