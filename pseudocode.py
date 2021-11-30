import os
import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import wiringpi
import RPi.GPIO as GPIO  #library to control relays
# https://learn.adafruit.com/adafruits-raspberry-pi-lesson-8-using-a-servo-motor/software help with servo
# MOSFET PWM: https://forums.raspberrypi.com/viewtopic.php?t=122390

# testing to see if I can push

#Setting mode of GPIO pins
GPIO.setmode(GPIO.BOARD)

#Set up and identifying which pins connect to where on raspberry pi
in1 = 1, in2 = 2, in3 = 3, in4 = 4, in5 = 5

GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(in5, GPIO.OUT)

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D22)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
chan0 = AnalogIn(mcp, MCP.P0)

print('Raw ADC Value: ', chan0.value)
print('ADC Voltage: ' + str(chan0.voltage) + 'V')

# use 'GPIO naming'
wiringpi.wiringPiSetupGpio()

# set #18 to be a PWM output
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)

# set the PWM mode to milliseconds stype
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)


def main():
  if chan0.voltage < 4 or chan0.voltage > 6:
    # if height at max, wait for some time and then do recursion with main()
    # else liftweight() and then do main()
    pass
  else:
    dropweight()
    main()


def liftweight():
  #lift the weight, release servo and then lift weight

  #Relay configuration to charge battery and send power to load
  GPIO.output(in1, GPIO.HIGH)
  GPIO.output(in2, GPIO.HIGH)
  GPIO.output(in3, GPIO.HIGH)

  GPIO.output(in4, GPIO.LOW)
  GPIO.output(in5, GPIO.LOW)

  
def dropweight():
  #drop weight, release servo
  # I believe we are dropping to the ground each time so we don't need to do recursion here, someone correct me if I'm wrong
  
  #Relay configuration to send power only from the gravity battery
  GPIO.output(in1, GPIO.LOW)
  GPIO.output(in2, GPIO.LOW)
  GPIO.output(in3, GPIO.LOW)

  GPIO.output(in4, GPIO.HIGH)
  GPIO.output(in5, GPIO.HIGH)
  
