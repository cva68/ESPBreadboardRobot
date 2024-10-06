from machine import Pin, I2C
import mcp23017
import lib.motor_driver as md
i2c = I2C(scl=Pin(8), sda=Pin(9))
mcp = mcp23017.MCP23017(i2c, 0x20)

mcp[7].output(1)
mcp[6].output(1)
mcp[5].output(1)
mcp[4].output(1)
mcp[3].output(1)
mcp[8].output(1)
mcp[9].output(1)
mcp[10].output(1)
mcp[11].output(1)
mcp[12].output(1)

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
