from machine import Pin, SoftI2C
import mcp23017
#import lib.motor_driver as md
import lib.led as ld
i2c = SoftI2C(scl=Pin(8), sda=Pin(9))
mcp = mcp23017.MCP23017(i2c, 0x20)


# Columns: 8,9,13,14,15
# Rows: 7,6,5,4,3
led = ld.Led((8,9,13,14,15),(7,6,5,4,3))
while 1:
    led.update_display()

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