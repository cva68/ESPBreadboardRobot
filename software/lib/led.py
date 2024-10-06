from machine import Pin, I2C
import mcp23017
import time
i2c = I2C(scl=Pin(8), sda=Pin(9))
mcp = mcp23017.MCP23017(i2c, 0x20)

tmp_delay = 10 # need to make this

class Led:
    state_buffer = 0b10001_01010_00100_01010_10001

    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
        print(self.rows)
        print(self.columns)
    
    def plot(self, x, y):
        """ turns on LED on at x and y cords """
        pass

    def unplot(self, x, y):
        #turns on LED on at x and y cords
        pass

    def toggle(self, x, y):
        #turns on LED on at x and y cords
        pass

    def clear(self):
        for col in self.rows:
            mcp[col].output(1)
        for row in self.columns:
            mcp[row].output(1)


    def update_display(self):
        """ To be called every iteration of the paced loop """
        this_state = self.state_buffer
        print(this_state)
        

        for row in self.rows:
            mcp[row].output(1)
            for col in self.columns:
                input(f"> row {row} col {col} -> {bin(this_state)} - > {(this_state & 1) == 0}")
                mcp[col].output((this_state & 1) == 0)
                this_state = this_state >> 1
            mcp[row].output(0)
            time.sleep(tmp_delay / 1000)
        input(">")
            
