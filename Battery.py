import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import keyboard

spi = busio.SPI(clock = board.SCK, MISO = board.MISO, MOSI = board.MOSI)
cs = digitalio.DigitalInOut(board.D22)

mcp = MCP.MCP3008(spi, cs)
while True:
  if keyboard.is_pressed():
    break
  chan0 = AnalogIn(mcp, MCP.P0)
  print(str(chan0.voltage) + 'V')
  time.sleep(0.2)
