// Wire Slave Receiver

#include <Wire.h>
#include "Keyboard.h"

void setup() {
  // Join I2C bus as slave with address 4
  Wire.begin(0x20);
  Keyboard.begin();
  // Call receiveEvent when data received                
  Wire.onReceive(receiveEvent);
}
 
// Function that executes whenever data is received from master
void receiveEvent(int howMany) {
  while (Wire.available()) { // loop through all but the last
    char c = Wire.read(); // receive byte as a character
    Keyboard.print(c);
  }
}
void loop() {
  delay(100);
}
