from machine import Pin, I2C
import mcp23017
i2c = I2C(scl=Pin(8), sda=Pin(9))
mcp = mcp23017.MCP23017(i2c, 0x20)

mcp[7].output(0)
mcp[6].output(0)
mcp[5].output(0)
mcp[4].output(0)
mcp[3].output(0)
mcp[8].output(0)
mcp[9].output(0)
mcp[10].output(0)
mcp[11].output(0)
mcp[12].output(0)


