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