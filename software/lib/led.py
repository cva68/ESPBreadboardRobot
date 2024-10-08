from machine import Pin, SoftI2C
from lib.mcp import MCPController
import time
import _thread

# Public
class Led:
    """ Class to control the 5x5 LED matrix """
    def __init__(self, mcp, columns, rows, refresh_rate=300):
        self.mcp = mcp
        self.columns = columns
        self.rows = rows
        self.state_buffer = 0
        self.refresh_rate = refresh_rate

        _thread.start_new_thread(self.update_display, ())

    def index_from_coords(self, x, y):
        """ Take an xy coordinate, and return the index of the LED on the matrix (internal) """
        return 24 - (y * 5 + x)
    
    def plot(self, x, y):
        """ Plot an LED at position x, y on the display (public) """
        self.state_buffer |= (1 << self.index_from_coords(x,y))

    def unplot(self, x, y):
        """ Un-plot an LED at position x, y on the display (public) """
        self.state_buffer &= ~(1 << self.index_from_coords(x,y))

    def toggle(self, x, y):
        """ Toggle and LED at position x, y on the display (public) """
        self.state_buffer ^= (1 << self.index_from_coords(x,y))

    def clear(self):
        """ Clear the display (public) """
        self.mcp.clear_bank_1()
        self.mcp.set_bank_0()

    def update_display(self):
        """ Update the display row-by-row (internal) """
        while 1:
            for row_shift, row in enumerate(self.rows):
                self.clear()
                state = self.state_buffer >> (5 * row_shift) & 0b11111
                for column_shift, col in enumerate(self.columns):
                    if (state >> column_shift) & 1:
                        self.mcp.set_bank1_pin(col)
                    else:
                        self.mcp.clear_bank1_pin(col)

                self.mcp.clear_bank0_pin(row)
                time.sleep(1/300)