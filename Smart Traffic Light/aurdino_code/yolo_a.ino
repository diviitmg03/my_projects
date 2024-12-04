#include <SoftwareSerial.h>



const int redPinA = 10;
const int greenPinA = 8;
const int redPinB = 12;
const int greenPinB = 6;
void setup() {
  // put your setup code here, to run once:
  pinMode(redPinA, OUTPUT);
  pinMode(greenPinA, OUTPUT);
  pinMode(redPinB, OUTPUT);
  pinMode(greenPinB, OUTPUT);
  Serial.begin(9600);

}

void loop() {
  // int response;
  // Read response from Raspberry Pi
  if(Serial.available()>0){
      int response = Serial.parseInt();
      if (response == 1){
    digitalWrite(redPinA, LOW);
    digitalWrite(greenPinA, HIGH);
    digitalWrite(redPinB, HIGH);
    digitalWrite(greenPinB, LOW);
    delay(6000); // Wait for 3 seconds
    
  }
  if(response==2){
    // Yellow light
    digitalWrite(redPinA, HIGH);
    digitalWrite(greenPinA, LOW);
    digitalWrite(redPinB, LOW);
    digitalWrite(greenPinB, HIGH);
    delay(6000); // Wait for 3 seconds
  }


  }
  // Process response as needed
  // put your main code here, to run repeatedly:
  // Red light
  
  else{
    // Green light
    digitalWrite(redPinA, HIGH);
    digitalWrite(greenPinA, LOW);
    digitalWrite(redPinB, HIGH);
    digitalWrite(greenPinB, LOW);
    delay(6000); // Wait for 3 seconds
  
    // // Pedestrian signal
    // digitalWrite(redPin, LOW);
    // digitalWrite(yellowPin, LOW);
    // digitalWrite(greenPin, LOW);
    // digitalWrite(pedestrianPin, HIGH);
    // delay(1000); // Wait for 3 seconds
  }
}
