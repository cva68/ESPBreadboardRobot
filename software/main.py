from machine import Pin, SoftI2C
import mcp23017

from lib.setup import setup
kitronik_motor_driver, led, input, basic = setup()

i2c = SoftI2C(scl=Pin(8), sda=Pin(9))
mcp = mcp23017.MCP23017(i2c, 0x20)

mcp[7].output(1)
mcp[6].output(1)
mcp[2].output(1)
mcp[1].output(1)
mcp[3].output(1)
mcp[8].output(0)
mcp[9].output(0)
mcp[10].output(0)
mcp[11].output(0)
mcp[12].output(0)


"""
led = ld.Led((7,6,5,4,3),(8,9,10,11,12))
while 1:
    led.update_display()
"""
"""
motor_driver = md.MotorDriver()
# Turn the right motor on with 50% speed forward
motor_driver.motor_on(motor_driver.Motors.MOTOR2, 512, motor_driver.MotorDirection.REVERSE)

# sleep(2)

# # Turn the left motor on with 75% speed in reverse
# motor_driver.motor_on('left', 768, 'reverse')
# sleep(2)

# # Turn off both motors
# motor_driver.motor_off('right')
# motor_driver.motor_off('left')
"""