// Wire Slave Receiver
#include <ArduinoSTL.h>
#include <map>
#include <Wire.h>
#include "Keyboard.h"
#include <string>
using namespace std;

// function that is called when handling a modifier key
uint8_t modifiers(char c){
  // modifier dictionary (called map in c++)
  std::map<char, uint8_t> mapModifiers = {
    {1,   KEY_RIGHT_ALT},
    {2,    KEY_LEFT_ALT},
    {3,   KEY_LEFT_CTRL},
    {4, KEY_RIGHT_SHIFT}
  };
  return mapModifiers[c];
}

// function that is called when handling a special key
uint8_t specialKeys(char c){
  // special key dictionary (called map in c++)
  std::map<char, uint8_t> mapSpecial = {
    {17,   KEY_LEFT_ARROW},
    {18,  KEY_RIGHT_ARROW},
    {19,     KEY_UP_ARROW},
    {20,   KEY_DOWN_ARROW},
    {8,     KEY_BACKSPACE},
    {6,        KEY_DELETE},
    {13,       KEY_RETURN},
    {32,               32},
    {7,     KEY_CAPS_LOCK},
    {9,           KEY_TAB}
  };
  return mapSpecial[c];
}

// STARTING CONFIGURATION
void setup() {
  // Join I2C bus as slave with address 4
  Wire.begin(0x20);
  Keyboard.begin(KeyboardLayout_de_DE);
  // Call receiveEvent when data received
  Wire.onReceive(receiveEvent);
}

// Function that executes whenever data is received from master
void receiveEvent(int howMany) {
  while (Wire.available()) {
    char c = Wire.read(); // receive byte as a character
    if (c > 32) {
      Keyboard.print(c);
      Keyboard.releaseAll();
    }else if (c < 5) {
      Keyboard.press(modifiers(c));
    }else {
      Keyboard.press(specialKeys(c));
      Keyboard.releaseAll();
    }
  }
}
// USELESS LOOP
void loop() {
}
