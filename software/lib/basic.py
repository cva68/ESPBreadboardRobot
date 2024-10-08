from time import sleep

class Basic:
    """ Basic functions. Annoyingly, this is mostly LED functions, but to match MakeCode 
        we have put them in here. """
    
    def __init__(self, led=0):
        """ Reference the LED function for later use """
        self.led = led
    
    def show_leds(self, plot):
        """ Take a string of hashes and periods provided by MakeCode and convert it into a binary int,
            then plot it on the display. """
        plot = plot.replace(" ", "")
        plot = plot.replace("\n","")
        print(plot)
        led_binary = 0

        for character in plot:
            led_binary += (character == '#')
            led_binary = led_binary << 1

        led_binary = led_binary >> 1
        self.led.state_buffer = led_binary
        print (bin(led_binary))

    def clear_screen(self):
        """ Clear the LCD """
        self.led.clear()

    def pause(self, duration):
        """ Sleep a duration """
        sleep(duration / 1000)