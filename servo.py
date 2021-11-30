# sudo apt-get install python3-rpi.gpio
# sudo pip3 install gpiozero

from gpiozero import Servo
from time import sleep

servo = Servo(25) # 25 is the pin number so this will be changed  

try:
	while True:
    	servo.min() # moves it the min
    	sleep(0.5)
    	servo.mid()
    	sleep(0.5)
    	servo.max() # moves it to the max
    	sleep(0.5)
except KeyboardInterrupt:
	print("Program stopped")
