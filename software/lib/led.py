from machine import Pin, SoftI2C
import mcp23017
import time
import _thread

i2c = SoftI2C(scl=Pin(8), sda=Pin(9))
mcp = mcp23017.MCP23017(i2c, 0x20)

tmp_delay = 10 # need to make this

class Led:
    state_buffer = 0b10001_01010_00100_01010_10001

    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
        min_col = columns[0]
        max_col = columns[-1]
        min_row = rows[0]
        max_row = rows[-1]

        # _thread.start_new_thread(self.update_display(), ())
    
    def plot(self, x, y):
        mask = get_mask(x, y)
        self.state_buffer |= mask

    def unplot(self, x, y):
        mask = get_mask(x, y)
        self.state_buffer &= ~mask

    def update_buffer(self, buffer):
        self.state_buffer = buffer

    def toggle(self, x, y):
        mask = get_mask(x, y)
        self.state_buffer ^= mask

    def clear(self):
        for col in self.rows:
            mcp[col].output(1)
        for row in self.columns:
            mcp[row].output(0)

    def update_display(self):
        """ To be called every iteration of the paced loop """
        for row_shift, row in enumerate(self.rows):
            for col in self.columns:
                mcp[col].output(0)

            state = self.state_buffer >> (5 * row_shift) & 0b11111
            for column_shift, col in enumerate(self.columns):
                mcp[col].output((state >> column_shift) & 1)
            mcp[row].output(0)
            time.sleep(1/50)
            mcp[row].output(1)

def get_mask(x, y):
    position = y*5 + x
    return 1 << position

# Columns: 8,9,13,14,15
# Rows: 7,6,5,4,3
# Need to set column high, row low, to turn on a LED
# Column low, row high to keep it off