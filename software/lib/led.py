from machine import Pin, I2C
import mcp23017
import time
import threading

i2c = I2C(scl=Pin(8), sda=Pin(9))
mcp = mcp23017.MCP23017(i2c, 0x20)

tmp_delay = 10 # need to make this

class Led:
    state_buffer = [17,10,4,10,17]

    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
        print(self.rows)
        print(self.columns)

        update_thread = threading.Thread(target = self.update_display)
        update_thread.start() #I love python :)
    
    def plot(self, x, y):
        # turns on LED on at x and y cords
        pass

    def unplot(self, x, y):
        # turns on LED on at x and y cords
        pass

    def update_buffer(self, buffer):
        self.state_buffer = buffer

    def toggle(self, x, y):
        # turns on LED on at x and y cords
        pass

    def clear(self):
        for col in self.rows:
            mcp[col].output(1)
        for row in self.columns:
            mcp[row].output(1)


    def update_display(self):
        """ To be called every iteration of the paced loop """
        for row, states in enumerate(self.state_buffer):
            self.clear()
            input("cleared >")
            for shift, col in enumerate(self.columns):
                if ((states >> shift) & 1):
                    print("1")
                    mcp[col].output(0)
                else:
                    print("0")
                    mcp[col].output(1)
            mcp[self.rows[row]].output(0)
            input(">")


# Columns: 8,9,13,14,15
# Rows: 