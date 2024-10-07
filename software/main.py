from machine import Pin, SoftI2C
import mcp23017

from lib.setup import setup
kitronik_motor_driver, led, input, basic = setup()

i2c = SoftI2C(scl=Pin(8), sda=Pin(9))
mcp = mcp23017.MCP23017(i2c, 0x20)

led.plot(1,1)
while 1:
    led.update_display()