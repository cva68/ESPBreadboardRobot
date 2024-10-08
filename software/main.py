from machine import SoftI2C, Pin
from lib.mcp import MCPController
from lib.led import Led
from lib.motor_driver import MotorDriver
from lib.basic import Basic
from lib.input import Button, Input

## Constants

# Motor pins
MOTOR_1_PINS = (2, 10)
MOTOR_2_PINS = (6, 7)

# Virtual display pins
DISPLAY_COLUMN_PINS = (0,1,5,6,7)
DISPLAY_ROW_PINS = (3,4,5,6,7)

# MCP I2C configuration
MCP_ADDRESS = 0x20
MCP_SCL_PIN = 8
MCP_SDA_PIN = 9


## Class references

# Start i2c protocol
i2c = SoftI2C(scl=Pin(MCP_SCL_PIN), sda=Pin(MCP_SDA_PIN))

# Initialise the MCP 
mcp = MCPController(i2c, MCP_ADDRESS)
mcp.set_all_output()

# Create reference to LED functions, and initialise the display
led = Led(mcp, DISPLAY_COLUMN_PINS, DISPLAY_ROW_PINS)

# Create reference to motor driver functions
kitronik_motor_driver = MotorDriver(MOTOR_1_PINS, MOTOR_2_PINS)

# Create reference to basic functions
basic = Basic()

# Unfortunate naming, but input() is unused.
input = Input()


""" Your code here! """
