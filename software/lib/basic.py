class Basic:
    def __init__(self, led):
        self.led = led
    
    def show_number(self, num):
        #Display number on LED screen.
        return 0
    
    def show_string(self, word):
        #Display word on LED screen.
        return 0

    # takes a string of . and # the size of the LED matrix turn LED on for every # and off for every.
    def show_leds(self, plot):
        rows = grid_str.splitlines()
        row_binarys = []

        for row in rows:
            binary = int(''.join('1' if char == '#' else '0' for char in row))
            row_binarys.append(row_binary)

        led.update_buffer(row_binarys)
    
    def clear_screen(self):
        led.update_buffer([00000, 00000, 00000, 00000, 00000])
    
    def show_arrow(self, direction):
        #takes a direction and displays a arrow in that direction on LEDs
        return 0
    