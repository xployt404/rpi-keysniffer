from re import sub
import subprocess
import pynput.keyboard as Keyboard
import os
from smbus import SMBus

# set bus address and i2c
addr = 0x20 # bus address
bus = SMBus(1) # indicates /dev/ic2-1

# set path to logging script
pathtologSH=f"{os.getcwd()}/log.sh"


# turns typed letters into byte codes readable for arduino
def ConvertStringToBytes(src):
     converted = []
     for i in src:
         converted.append(ord(i))
     return converted

# Callback function whenever a key is pressed
def on_press(key):
    try:
        # only execute when pressed key isnt ALTGR
        if key.char!=None:
            print(f'Key {key.char} pressed!')
            subprocess.run(["/bin/sh", pathtologSH, f"{key.char}"])     # logs chars to keys.txt
            bus.write_byte(addr, ConvertStringToBytes(f"{key.char}"))   # sends to bytes converted char to arduino
    except AttributeError:
        print(f'Special Key {key} pressed!')
        print(key)

        #different texts to be written into keys.txt for certain keys
        if key==Keyboard.Key.space:
            subprocess.run(["/bin/sh", pathtologSH, "SPACE"])
        elif key==Keyboard.Key.enter:
            subprocess.run(["/bin/sh", pathtologSH, "ENTER"])
        elif key==Keyboard.Key.ctrl:
            subprocess.run(["/bin/sh", pathtologSH, "CTRL"])
        elif key==Keyboard.Key.backspace:
            subprocess.run(["/bin/sh", pathtologSH, "BACKSPACE"])
        elif key==Keyboard.Key.alt:
            subprocess.run(["/bin/sh", pathtologSH, "ALT"])
        elif key==Keyboard.Key.shift_r:
            subprocess.run(["/bin/sh", pathtologSH, "SHIFT"])
        elif key==Keyboard.Key.shift:
            subprocess.run(["/bin/sh", pathtologSH, "SHIFT"])
        elif key==Keyboard.Key.delete:
            subprocess.run(["/bin/sh", pathtologSH, "DELETE"])
        elif key==Keyboard.Key.alt_gr:
            subprocess.run(["/bin/sh", pathtologSH, "ALTGR"])
        elif str(key)=="None":
            subprocess.run(["/bin/sh", pathtologSH, "ALTGR"])
        else:
            subprocess.run(["/bin/sh", pathtologSH, f"{key}"])

# Callback function whenever a key is released
def on_release(key):
    print(f'Key {key} released')
    if str(key) == "<65027>":
        subprocess.run(["/bin/sh", pathtologSH, "ALTGR"])

with Keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
