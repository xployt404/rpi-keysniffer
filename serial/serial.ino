// Wire Slave Receiver

#include <Wire.h>
#include "Keyboard.h"

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

    // SPACE
    if (c==32) {
      Keyboard.print(" ");

    // ENTER
    }else if (c==13){
      Keyboard.write(KEY_RETURN);
      Keyboard.releaseAll();

    // SHIFT
    }else if(c==15){
      Keyboard.press(KEY_RIGHT_SHIFT);

    // ALT
    }else if (c==2) {
      Keyboard.press(KEY_LEFT_ALT);

    }else if (c==3) {
      Keyboard.press(KEY_RIGHT_CTRL);

    // ALT GR
    }else if (c==1) {
      Keyboard.press(KEY_RIGHT_ALT);

    // BACKSPACE
    }else if (c==8) {
      Keyboard.write(KEY_BACKSPACE);
      Keyboard.releaseAll();

    // TAB
    }else if(c==9){
      Keyboard.write(KEY_TAB);

    // CAPS LOCK
    }else if (c==178) {
      Keyboard.press(KEY_CAPS_LOCK);
      Keyboard.releaseAll();
    // DELETE
    }else if (c==127) {
      Keyboard.write(KEY_DELETE);

    // Ö
    }else if (c==246) {
      Keyboard.press(148);
      Keyboard.releaseAll();

    // Y
    }else if (c==122) {
      Keyboard.print("y");
      Keyboard.releaseAll();
      
    // X
    }else if (c==121) {
      Keyboard.print("z");
      Keyboard.releaseAll();

    // LEFT_ARROW
    }else if (c==17) {
      Keyboard.press(KEY_LEFT_ARROW);
      Keyboard.releaseAll();

    // RIGHT_ARROW
    }else if (c==18) {
      Keyboard.press(KEY_RIGHT_ARROW);
      Keyboard.releaseAll();

    // UP_ARROW
    }else if (c==19) {
      Keyboard.press(KEY_UP_ARROW);
      Keyboard.releaseAll();

    // DOWN_ARROW
    }else if (c==20) {
      Keyboard.press(KEY_DOWN_ARROW);
      Keyboard.releaseAll();

    }else{
        Keyboard.print(c);
        Keyboard.releaseAll();
    }
  }
}
void loop() {
  delay(1);
}
