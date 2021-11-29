import os
import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import wiringpi
# https://learn.adafruit.com/adafruits-raspberry-pi-lesson-8-using-a-servo-motor/software help with servo

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
  else:
    dropweight()
    main()


def liftweight():
  #lift the weight, release servo and then lift weight
  
def dropweight():
  #drop weight, release servo
  # I believe we are dropping to the ground each time so we don't need to do recursion here, someone correct me if I'm wrong
  
