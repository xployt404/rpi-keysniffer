#  Raspberry Pi Master for Arduino Slave
#  i2c_master_pi.py
#  Connects to Arduino via I2C
  
#  DroneBot Workshop 2019
#  https://dronebotworkshop.com
 
from smbus import SMBus
 
addr = 0x20 # bus address
bus = SMBus(1) # indicates /dev/ic2-1
 
numb = 1
 
print ("Enter 1 for ON or 0 for OFF")
while numb == 1:
        eingabe=input(">>>>   ")
        eingabe=int(eingabe)
        bus.write_byte(addr, eingabe)
