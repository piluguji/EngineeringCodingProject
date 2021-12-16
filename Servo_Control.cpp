#include <Servo.h>
#define echoPin 2 // attach pin D2 Arduino to pin Echo of HC-SR04
#define trigPin 3 //attach pin D3 Arduino to pin Trig of HC-SR04

// defines variables
double duration; // variable for the duration of sound wave travel
double distance; // variable for the distance measurement
int servoPin = 5;
int sensorValue;
float voltage;
Servo Servo1;

void setup() {
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an OUTPUT
  pinMode(echoPin, INPUT); // Sets the echoPin as an INPUT
  Serial.begin(9600); // // Serial Communication is starting with 9600 of baudrate speed
  Serial.println("Ultrasonic Sensor HC-SR04 Test"); // print some text in Serial Monitor
  Serial.println("with Arduino UNO R3");
  Servo1.attach(servoPin);
}
void loop() {
  // Clears the trigPin condition
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin HIGH (ACTIVE) for 10 microseconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  // Calculating the distance
  distance = duration * 0.00034 / 2; // Speed of sound wave divided by 2 (go and back)
  // Displays the distance on the Serial Monitor
  sensorValue = analogRead(A0);
  voltage = sensorValue * 5.0/1023.0;
  if(voltage < MIN_VOLTAGE){
    Servo1.write(180);
    delay(1000);
    analogWrite(PWM_Pin, 0);
  }else{
    if(distance < 0.1){
      Servo1.write(0);
      delay(1000);
      analogWrite(PWM_Pin, 0);
    }else{
      analogWrite(PWM_Pin, STANDARD_FREQUENCY);
      Servo1.write(180);
      delay(1000);
    }
  }
}
  
