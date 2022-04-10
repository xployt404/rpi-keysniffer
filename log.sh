#this script logs the user input to a text file
char="$1   "
pwd=$(pwd)
previous=$(cat $pwd/keys.txt)
keys=$previous$char
echo $keys > $pwd/keys.txt
